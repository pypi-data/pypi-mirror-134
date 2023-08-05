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

import base64
import os.path
from hashlib import sha1
from typing import Optional

import click

from commands.framework import PagemarksCommand
from framework.cmdline import CmdLine
from framework.globals import BOOKMARK_ID_LEN
from framework.util import normalize_url, locate_repo, PagemarksFailure


class CmdLocate(PagemarksCommand):
    """Locate the bookmark file for the given URL."""
    url: str
    must_exist: bool

    def __init__(self, config: CmdLine, url: str, must_exist: bool = True):
        super().__init__(config)
        self.url = url
        self.must_exist = must_exist

    def invalid_args(self) -> Optional[str]:
        if self.url is None or len(self.url.strip()) == 0:
            return 'Missing argument \'URL\'.'
        return None

    def execute(self):
        filename = self.url_to_filename()
        if self.must_exist:
            repo_dir = locate_repo(self.config)
            # TODO look in all collections
            if not os.path.isfile(os.path.join(repo_dir, 'default/' + filename)):
                raise PagemarksFailure('not found')
        click.echo('default/' + filename)

    def url_to_filename(self) -> str:
        normalized_url = normalize_url(self.url)
        m = sha1()
        m.update(
            normalized_url.encode('utf-8'))  # TODO use encoding of URLs or system encoding (b/c called from cmdline)?
        digest = m.digest()
        hashcode = base64.b32encode(digest).decode('ascii').lower()[:BOOKMARK_ID_LEN]
        foldernum = digest[len(digest) - 1] % pow(2, 5)
        folderstr = str(foldernum)
        if foldernum < 10:
            folderstr = '0' + folderstr
        return folderstr + '/' + hashcode + '.json'
