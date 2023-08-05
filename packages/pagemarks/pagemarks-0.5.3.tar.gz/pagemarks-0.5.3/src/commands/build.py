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
import re
import shutil
from typing import Optional

import click
import pkg_resources
from genshi.template import NewTextTemplate

from commands.framework import PagemarksCommand
from framework.cmdline import CmdLine
from framework.data import Bookmark, PagemarksCollection, RepoReader
from framework.render import GenshiBookmarkContext, GenshiCollectionContext
from framework.util import locate_repo



class CmdBuild(PagemarksCommand):
    """Generate a Pagemarks website for the repo"""
    base_url: str
    output_dir: str


    def __init__(self, config: CmdLine, base_url: str, output_dir: str):
        super().__init__(config)
        self.base_url = base_url
        self.output_dir = output_dir


    def invalid_args(self) -> Optional[str]:
        return None


    # noinspection PyUnusedLocal
    @staticmethod
    def ignore_python(src: str, names: list[str]) -> list[str]:
        return [s for s in names if not s.endswith('.js')]


    # noinspection PyUnusedLocal
    @staticmethod
    def ignore_gitkeep(src: str, names: list[str]) -> list[str]:
        return [s for s in names if s == '.gitkeep']


    def execute(self):
        extracted_css = pkg_resources.resource_filename('resources', 'css')
        shutil.copytree(extracted_css, self.output_dir + '/css', dirs_exist_ok=True, ignore=self.ignore_gitkeep)
        extracted_fonts = pkg_resources.resource_filename('resources', 'fonts')
        shutil.copytree(extracted_fonts, self.output_dir + '/fonts', dirs_exist_ok=True, ignore=self.ignore_gitkeep)
        extracted_js = pkg_resources.resource_filename('js', '')
        shutil.copytree(extracted_js, self.output_dir + '/js', dirs_exist_ok=True, ignore=self.ignore_python)
        # TODO register pkg_resources.cleanup_resources() as an atexit function

        colls = RepoReader(locate_repo(self.config)).read_repo()
        css_themes = self.load_theme_list()
        for coll_name in colls:
            # TODO build only self.config.collection_name, unless that's None
            html = self.build_collection(colls[coll_name], css_themes)
            click.echo(
                    'Read ' + str(
                            len(colls[coll_name].bookmarks)) + ' bookmarks from collection \'' + coll_name + '\'.')
            coll_filename = os.path.join(self.output_dir, ('index' if coll_name == 'default' else coll_name) + '.html')
            with open(coll_filename, 'w', encoding='utf-8') as coll_outfile:
                coll_outfile.write(html)
                click.echo('Collection generated: ' + coll_filename)


    @staticmethod
    def load_theme_list() -> dict:
        jsonc = pkg_resources.resource_string(__name__, '../resources/html/css-themes.json') \
            .replace(b'\r\n', b'\n').decode('utf-8')
        return json.loads(re.sub("^\s*//.*", "", jsonc, flags=re.MULTILINE))


    def build_collection(self, coll_data: PagemarksCollection, css_themes: dict) -> str:
        template = pkg_resources.resource_string(__name__, '../resources/html/index.html') \
            .replace(b'\r\n', b'\n').decode('utf-8')
        html_template = NewTextTemplate(template, encoding='utf-8')
        genshi_context = GenshiCollectionContext(self.base_url, css_themes, coll_data).to_context()
        index_html = html_template.generate(genshi_context).render()
        bookmark_html = self.build_bookmarks(coll_data.bookmarks)
        index_html = index_html.replace('<!-- //BOOKMARKS// -->', '\n'.join(bookmark_html))
        return index_html


    def build_bookmarks(self, bookmarks: list[Bookmark]) -> list[str]:
        template = pkg_resources.resource_string(__name__, '../resources/html/bookmark.html') \
            .replace(b'\r\n', b'\n').decode('utf-8')
        html_template = NewTextTemplate(template, encoding='utf-8')
        empty_line_pattern = re.compile('^\s*$\n', re.MULTILINE)
        result: list[str] = []
        for bm in bookmarks:
            genshi_context = GenshiBookmarkContext(self.base_url, bm).to_context()
            html = html_template.generate(genshi_context).render()
            html = re.sub(empty_line_pattern, '', html)
            result.append(html)
        return result
