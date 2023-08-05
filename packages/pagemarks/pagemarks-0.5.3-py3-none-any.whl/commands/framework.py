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

import abc
from typing import final, Optional

import click

from framework.cmdline import CmdLine
from framework.util import PagemarksError, PagemarksAbort, PagemarksFailure


# TODO move to framework.basecmd
class PagemarksCommand(object):
    """Abstract superclass of all Pagemarks commands"""
    __metaclass__ = abc.ABCMeta
    config: CmdLine

    def __init__(self, config: CmdLine):
        self.config = config

    @final
    def run_command(self) -> int:
        try:
            err_msg = self.invalid_args()
            if err_msg is not None:
                click.echo(f"Error: {err_msg}", err=True)
                return 2
            self.execute()
            return 0
        except PagemarksError as e:
            click.echo(f"Error: {e.error_message}", err=True)
            return 1
        except PagemarksFailure as e:
            click.echo(e.error_message, err=True)
            return 1
        except PagemarksAbort as e:
            if e.message is not None:
                click.echo(e.message)
                return 0

    @abc.abstractmethod
    def execute(self):
        """Execute the command"""
        pass

    @abc.abstractmethod
    def invalid_args(self) -> Optional[str]:
        """Validate the arguments passed into the command. An error found is immediately returned.

        :returns: the error message, in case something was wrong, or ``None`` if all is well
        """
        pass
