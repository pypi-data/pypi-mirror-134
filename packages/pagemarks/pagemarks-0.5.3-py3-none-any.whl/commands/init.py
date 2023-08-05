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
from typing import Optional

import pkg_resources
from genshi.template import Context, NewTextTemplate
from git import Repo

from commands.framework import PagemarksCommand
from framework.cmdline import CmdLine
from framework.globals import DEFAULT_COLL_NAME
from framework.util import locate_repo, PagemarksError



class CmdInit(PagemarksCommand):
    """
    Initialize a new Pagemarks repository.

    A new repo contains exactly one collection, named either 'default' or something else specified by
    ``config.collection_name``.
    """
    user_name: Optional[str]
    user_email: Optional[str]


    def __init__(self, config: CmdLine, user_name: Optional[str], user_email: Optional[str]):
        super().__init__(config)
        self.user_name = user_name
        self.user_email = user_email


    def invalid_args(self) -> Optional[str]:
        return None


    def execute(self):
        repo_dir = locate_repo(self.config, use_env=False)
        if self.dir_not_empty(repo_dir):
            raise PagemarksError('Directory not empty: ' + repo_dir)

        repo = Repo.init(repo_dir)

        self.configure_git_repo(repo)
        self.create_readme_md(repo_dir)
        self.create_git_attributes(repo_dir)
        self.create_gitlabci_yaml(repo_dir)
        self.create_initial_coll(repo_dir)
        self.commit_initial(repo)


    def configure_git_repo(self, repo: Repo):
        with repo.config_writer('repository') as cw:
            # Tell Git to automatically use system-specific line endings.
            cw.set_value('core', 'autocrlf', 'true')

            # Turn off the CRLF safety check. Since we know that we only have generated JSON files, the potential
            # corruption is impossible. Any warnings would only mislead or annoy users.
            cw.set_value('core', 'safecrlf', 'false')

            # Turn off rename detection, which would make no sense in our use case, because we compute file names from
            # the bookmark URLs. Therefore, a different file name will *always* indicate a different bookmark, so
            # rename detection could only find false positives by definition.
            cw.set_value('diff', 'renames', 'false')

            # Rebase local commits onto the pulled branch, so we have a clean git history.
            cw.set_value('pull', 'rebase', 'true')

            # Set user name and email as specified on command line.
            if self.user_name is not None and len(self.user_name) > 0:
                cw.set_value('user', 'name', self.user_name)
            if self.user_email is not None and len(self.user_email) > 0:
                cw.set_value('user', 'email', self.user_email)


    def create_readme_md(self, repo_dir: str) -> None:
        template_src = self.read_resource('../resources/repo/README.md')
        username = 'someone' if self.user_name is None or len(self.user_name.strip()) == 0 else self.user_name
        template = NewTextTemplate(template_src, encoding='utf-8')
        readme_md = template.generate(Context(username=username)).render()
        self.write_resource(repo_dir, '../README.md', readme_md)


    @staticmethod
    def create_git_attributes(repo_dir: str):
        content = '* text=auto\n*.sh text eol=lf\n*.bat text eol=crlf\n'
        with open(os.path.join(repo_dir, '.git/info/attributes'), 'w', newline='\n') as attr_file:
            attr_file.write(content)


    def create_initial_coll(self, repo_dir: str) -> None:
        # TODO extract collection name finding logic (used in other modules, too)
        coll_name = DEFAULT_COLL_NAME if self.config.collection_name is None else self.config.collection_name
        os.makedirs(os.path.join(repo_dir, coll_name))
        coll_templ_json = self.read_resource('../resources/repo/collection-template.json')
        self.write_resource(repo_dir, 'pagemarks.json', coll_templ_json)


    def create_gitlabci_yaml(self, repo_dir: str) -> None:
        gitlabci_yml = self.read_resource('../resources/repo/gitlab-ci.yml')
        self.write_resource(repo_dir, '../.gitlab-ci.yml', gitlabci_yml)


    def commit_initial(self, repo: Repo) -> None:
        coll_name = DEFAULT_COLL_NAME if self.config.collection_name is None else self.config.collection_name
        repo.index.add('README.md')
        repo.index.add('.gitlab-ci.yml')
        repo.index.add(coll_name + '/pagemarks.json')
        repo.index.commit('Initial Commit')


    @staticmethod
    def dir_not_empty(dir_name: str) -> bool:
        return os.path.isdir(dir_name) and os.listdir(dir_name)


    @staticmethod
    def read_resource(path: str) -> str:
        return pkg_resources.resource_string(__name__, path) \
            .replace(b'\r\n', b'\n') \
            .decode('utf-8')


    def write_resource(self, repo_dir: str, path: str, content: str) -> None:
        coll_name = DEFAULT_COLL_NAME if self.config.collection_name is None else self.config.collection_name
        with open(os.path.join(repo_dir, coll_name, path), 'w') as f:
            f.write(content)
