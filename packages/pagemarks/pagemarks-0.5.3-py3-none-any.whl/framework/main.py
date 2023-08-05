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

import sys

import click
import pkg_resources

from commands.add import CmdAdd
from commands.build import CmdBuild
from commands.importer import CmdImport
from commands.init import CmdInit
from commands.locate import CmdLocate
from framework.cmdline import CmdLine

# import sys
# for path in sys.path:
#     print(path)

pass_config = click.make_pass_decorator(CmdLine, ensure=True)


@click.group()
@click.option('--repo', type=click.Path(), required=False, help='Path to pagemarks repository')
@click.option('--collection', '-c', type=click.STRING, default=None, required=False,
              help='The name of the collection to operate on. Defaults to \'default\' or all, depending on the command')
@click.option('--yes', '-y', is_flag=True, help='Answer all prompts with \'yes\'')
@click.version_option(pkg_resources.require('pagemarks')[0].version, prog_name='pagemarks',
                      message='%(prog)s v%(version)s')
@pass_config
def app(config: CmdLine, repo, collection: str, yes: bool):
    """pagemarks.org: Free git-based, self-hosted bookmarks on the web and via command line"""
    config.repo_dir = repo
    config.collection_name = collection
    config.yes = yes


@app.command('build')  # TODO option and template for analytics
@click.option('--base-url', default='', required=False, help='leading path fragment in internal URLs')
@click.option('--output-dir', '-o', default='build/site', required=False, help='generated site output directory')
@pass_config
def cmd_build(config, base_url, output_dir):
    """Build a pagemarks website with all your bookmarks"""
    rc = CmdBuild(config, base_url, output_dir).run_command()
    if rc != 0:
        sys.exit(rc)


@app.command('check')
def cmd_check():
    """Access every bookmark to check it's still valid"""
    # TODO maybe check repo for validity, too? or extra validate command?
    click.echo('command: check')


@app.command('import')
@click.option('--no-private', is_flag=True, help='Exclude bookmarks flagged as \'private\'')
@click.argument('input_path', required=True)
@pass_config
def cmd_import(config: CmdLine, no_private: bool, input_path: str):
    """Import from an nb repository or from a Netscape bookmarks file"""
    rc = CmdImport(config, not no_private, input_path).run_command()
    if rc != 0:
        sys.exit(rc)


@app.command('add')
@click.option('--encrypt', '-e', is_flag=True, help='Encrypt bookmark')
@click.option('--tag', '-t', multiple=True, required=False, default=[],
              help='Tags for the new bookmark, specify multiple times for more tags')
@click.argument('url', required=True)
@pass_config
def cmd_add(config: CmdLine, encrypt: bool, tag: list[str], url: str):
    """Add a bookmark to the repository"""
    rc = CmdAdd(config, tag, url).run_command()
    if rc != 0:
        sys.exit(rc)


@app.command('init')
@click.option('--user-name', type=click.STRING, default=None, required=False,
              help='User name to set in Git local config for the new repo')
@click.option('--user-email', type=click.STRING, default=None, required=False,
              help='User email to set in Git local config for the new repo')
@pass_config
def cmd_init(config: CmdLine, user_name, user_email):
    """Initialize a new pagemarks repository with a default collection"""
    rc = CmdInit(config, user_name, user_email).run_command()
    if rc != 0:
        sys.exit(rc)


@app.command('locate')
@click.argument('url', required=True)
@pass_config
def cmd_locate(config: CmdLine, url: str):
    """Locate the bookmark file for the given URL"""
    rc = CmdLocate(config, url).run_command()
    if rc != 0:
        sys.exit(rc)
