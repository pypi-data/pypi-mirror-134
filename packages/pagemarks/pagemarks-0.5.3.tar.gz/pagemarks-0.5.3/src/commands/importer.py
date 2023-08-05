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

import os
import re
from typing import Optional

import click
from bs4 import BeautifulSoup
from bs4.element import Doctype, Tag
from git import Repo

from commands.add import CmdAdd, JsonTagList
from commands.framework import PagemarksCommand
from framework.cmdline import CmdLine
from framework.globals import DEFAULT_COLL_NAME
from framework.util import PagemarksError, PagemarksAbort, normalize_timestamp, normalize_tags, locate_repo


class ImportStats(object):
    num_bookmarks_imported: int = 0
    num_notes_imported: int = 0
    tags_imported: set[str] = set()
    num_private_bookmarks: int = 0
    files_added: list[str] = []


class CmdImport(PagemarksCommand):
    """Import a Netscape bookmarks file or an nb repo into a Pagemarks collection."""
    include_private: bool
    input_path: str

    def __init__(self, config: CmdLine, include_private: bool, input_path: str):
        super().__init__(config)
        self.include_private = include_private
        self.input_path = input_path

    def invalid_args(self) -> Optional[str]:
        if self.input_path is None or len(self.input_path.strip()) == 0:
            return 'Missing argument \'INPUT_PATH\'.'
        if not self.is_nbm_html() and not self.is_nb_repo():
            return f"\'{self.input_path}\' is neither a Netscape Bookmark file nor an nb repo. Import not supported."
        return None

    def execute(self):
        if self.is_nbm_html():
            self.import_nbm_html()
        elif self.is_nb_repo():
            self.import_nb_repo()

    def is_nbm_html(self) -> bool:
        """The ``input_path`` is considered a Netscape Bookmark File (NBM) if it's an HTML file."""
        return os.path.isfile(self.input_path) and self.input_path.lower().endswith('.html')

    def is_nb_repo(self) -> bool:
        """The ``input_path`` is considered an bn repo if it's a directory with TODO how to recogize nb repos?"""
        return os.path.isdir(self.input_path)

    def import_nbm_html(self):
        stats = ImportStats()
        with open(self.input_path, 'r', encoding='utf-8') as nbm_file:
            soup = BeautifulSoup(nbm_file, features='html5lib')
        self.check_nbm_doctype(soup)
        elems = soup.select('dt')
        for dt in elems:
            a = dt.a
            if a is None:
                continue
            is_private = 'private' in a.attrs and a.attrs['private'] == '1'
            if is_private:
                stats.num_private_bookmarks += 1
                if not self.include_private:
                    continue  # skip private bookmark

            record = self.html2record(dt, stats)
            if record is None:
                continue

            filename = CmdAdd(self.config, record['tags'], record['url']).add_file(record, git=False)
            stats.files_added.append(filename)
            stats.num_bookmarks_imported += 1

        self.commit_imported_files(stats.files_added)
        self.print_stats(stats)

    def check_nbm_doctype(self, soup: BeautifulSoup):
        ok = False
        for item in soup.contents:
            if isinstance(item, Doctype) and item.lower().startswith('netscape-bookmark-file'):
                ok = True
                break
        if not ok:
            raise PagemarksError(f"\'{self.input_path}\' is not a Netscape Bookmark file")

    @staticmethod
    def html2record(dt: Tag, stats: ImportStats) -> Optional[dict]:
        a = dt.a
        record = {  # dicts keep insertion order
            "name": a.text,
            "url": None,
            "tags": []
        }
        if a.text is not None and len(a.text.strip()) > 0:
            record['name'] = a.text.strip()
        if 'href' in a.attrs:
            record['url'] = a.attrs['href']
        else:
            return None  # not a bookmark (could be an icon, webslice, or feed)
        if 'tags' in a.attrs:
            record['tags'] = JsonTagList(normalize_tags(re.split(',|\\s', a.attrs['tags'])))
            stats.tags_imported.update(record['tags'].tag_list)
        if 'add_date' in a.attrs:
            record['date_added'] = normalize_timestamp(a.attrs['add_date'])

        dd = dt.next_sibling
        if dd is not None and dd.name == 'dd' and dd.text is not None:
            record['notes'] = dd.text.strip()
            stats.num_notes_imported += 1
        return record

    def commit_imported_files(self, files_added: list[str]):
        if len(files_added) == 0:
            return
        repo_dir = locate_repo(self.config)
        repo = Repo.init(repo_dir)
        for f in files_added:
            repo.index.add(f)
        coll_name = DEFAULT_COLL_NAME if self.config.collection_name is None else self.config.collection_name
        repo.index.commit(f"Import Netscape Bookmark file into \'{coll_name}\' collection")

    def print_stats(self, stats: ImportStats):
        click.echo(f"{stats.num_bookmarks_imported} bookmarks imported, "
                   f"containing {stats.num_notes_imported} notes and {len(stats.tags_imported)} different tags.")
        if self.include_private:
            click.echo(f"Of those, {stats.num_private_bookmarks} were bookmarks flagged as 'private'. "
                       f"They are now the same as the other bookmarks.")
        else:
            click.echo(f"{stats.num_private_bookmarks} private bookmarks were skipped.")

    def import_nb_repo(self):
        # TODO
        raise PagemarksAbort('Importing nb repos is not yet implemented.')
