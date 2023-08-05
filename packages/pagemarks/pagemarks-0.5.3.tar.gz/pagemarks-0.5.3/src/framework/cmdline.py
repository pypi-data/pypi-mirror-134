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

from typing import Optional


class CmdLine(object):
    """Command line options applicable to all commands."""
    repo_dir: Optional[str]
    yes: bool
    collection_name: Optional[str]
    overwrite_all_bookmarks: bool

    def __init__(self):
        self.repo_dir = None
        self.yes = False
        self.collection_name = None
        self.overwrite_all_bookmarks = False
