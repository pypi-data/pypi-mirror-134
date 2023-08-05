#
# pagemarks - Free git-based, self-hosted bookmarks on the web and via command line
# Copyright (c) 2019-2021 the pagemarks contributors
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License, version 3, as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/gpl.html>.
#

import json
import os
from datetime import datetime
from json import JSONEncoder
from typing import Optional, Tuple

import click
from bs4 import BeautifulSoup
from requests import request

from commands.framework import PagemarksCommand
from commands.locate import CmdLocate
from framework.cmdline import CmdLine
from framework.globals import DEFAULT_COLL_NAME
from framework.util import normalize_tags, locate_repo, normalize_date, PagemarksError, prompt, PromptAnswer, \
    PagemarksAbort


class JsonTagList:
    tag_list = None

    def __init__(self, tl):
        self.tag_list = tl


class JsonTagListEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JsonTagList):
            return "##<{}>##".format(obj.tag_list).replace('\'', '"')


class CmdAdd(PagemarksCommand):
    """Add a bookmark to a collection."""
    tags: list[str]
    url: str

    def __init__(self, config: CmdLine, tags: list[str], url: str):
        super().__init__(config)
        self.tags = tags
        self.url = url

    def invalid_args(self) -> Optional[str]:
        return None

    def execute(self):
        record = {
            "url": self.url,
            "date_added": normalize_date(datetime.now())
        }  # FIXME the order of keys is not preserved in the final JSON
        nt = normalize_tags(self.tags)
        if len(nt) > 0:
            record['tags'] = JsonTagList(nt)
        name, notes = self.parse_page()
        if name is not None:
            record['name'] = name
        if notes is not None:
            record['notes'] = notes
        self.add_file(record, git=True)

    @staticmethod
    def clean_nones(record: dict) -> dict:
        """Remove the None values from the given dictionary."""
        return {
            key: val
            for key, val in record.items()
            if val is not None
        }

    def to_json(self, record: dict) -> str:
        doc = json.dumps(self.clean_nones(record), indent=4, cls=JsonTagListEncoder, ensure_ascii=False)
        doc = doc.replace('"##<', '').replace('>##"', '')
        lines = doc.split('\n')
        doc = ''
        for line in lines:
            if line.strip().startswith('"tags":'):
                doc += line.replace('\\"', '"') + '\n'
            else:
                doc += line + '\n'
        return doc

    def parse_page(self) -> Tuple[Optional[str], Optional[str]]:
        html = self.fetch_page()
        if html is None:
            return None, None
        soup = BeautifulSoup(html, features='html5lib')
        elem = soup.select_one("head > title")
        name = elem.text if elem is not None else None

        notes = None
        elem = soup.select('head > meta[name]')
        for t in elem:
            if (str(t['name']).lower() == 'description') and ('content' in t.attrs):
                notes = t['content']
                break
        return name, notes

    def fetch_page(self) -> Optional[str]:
        try:
            response = request("GET", self.url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"ERROR: Failed to access URL: {self.url} (Error {response.status_code} - {response.text})")
        except IOError as e:
            print(f"ERROR: Failed to access URL: {self.url} (IOError: {e})")
        # TODO in case of errors, prompt to continue
        return None

    def add_file(self, record: dict, git: bool) -> str:
        repo_dir = locate_repo(self.config)
        coll_name = DEFAULT_COLL_NAME if self.config.collection_name is None else self.config.collection_name
        if not os.path.isdir(os.path.join(repo_dir, coll_name)):
            raise PagemarksError(f"Collection \'{coll_name}\' does not exist in repository \'{repo_dir}\'.")

        filename = os.path.join(repo_dir, coll_name, CmdLocate(self.config, self.url, False).url_to_filename())
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        rel_path = os.path.relpath(filename, start=repo_dir)
        if self.skip_existing_file(filename, record['url']):
            return rel_path

        doc = self.to_json(record)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(doc)

        # TODO commit to git if git==True
        return rel_path

    def skip_existing_file(self, filename: str, url: str) -> bool:
        if os.path.isfile(filename):
            if self.config.yes or self.config.overwrite_all_bookmarks:
                return False
            click.echo('Bookmark exists: ' + url)
            answer = prompt('Overwrite?')
            if answer == PromptAnswer.YES:
                return False
            elif answer == PromptAnswer.NO:
                click.echo('Skipping.')
                return True
            elif answer == PromptAnswer.ALL:
                self.config.overwrite_all_bookmarks = True
                return False
            elif answer == PromptAnswer.QUIT:
                # TODO git reset --hard HEAD, possibly after another prompt, or check clean at start
                raise PagemarksAbort()
            else:
                raise PagemarksError('Bug: missed branch')
        return False
