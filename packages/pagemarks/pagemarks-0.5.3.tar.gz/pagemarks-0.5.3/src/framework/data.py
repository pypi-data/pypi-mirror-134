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
from datetime import datetime, timezone
from functools import cmp_to_key
from typing import Optional

import commentjson

from framework.globals import BOOKMARK_ID_LEN
from framework.util import PagemarksError, normalize_tags


class Bookmark:
    id: str
    name: Optional[str]
    url: str
    date_added: Optional[datetime]
    tags: list[str]
    notes: Optional[str]

    def __init__(self, bmid: str, url: str):
        if len(url) < 3:
            raise PagemarksError("bug: empty url")
        self.url = url
        if len(bmid) != BOOKMARK_ID_LEN:
            raise PagemarksError("bug: invalid bookmark id")
        self.id = bmid
        self.name = None
        self.tags = []
        self.date_added = None
        self.notes = None


class PagemarksCollection(object):
    title: Optional[str]
    pinned_filters: list[str]
    bookmarks: list[Bookmark]

    def __init__(self):
        self.title = None
        self.pinned_filters = []
        self.bookmarks = []


class RepoReader:
    repo_dir: str

    def __init__(self, repo_dir: str):
        self.repo_dir = repo_dir
        self.date_formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d',
            '%Y-%m-%d %I:%M:%S %p',
            '%Y-%m-%d %I:%M %p'
        ]

    def parse_timestamp(self, s: str) -> datetime:
        for fmt in self.date_formats:
            try:
                return datetime.strptime(s, fmt)
            except ValueError:
                pass
        raise ValueError(f"time data '{s}' does not match format '{self.date_formats[0]}'")

    def read_repo(self) -> {}:
        result = {}
        for f in os.listdir(self.repo_dir):
            coll_path = os.path.join(self.repo_dir, f)
            if self.is_collection(coll_path):
                coll = self.read_collection(coll_path)
                if coll is not None:
                    result[f] = coll
        if len(result) < 1:
            raise PagemarksError('No pagemarks collections found in directory: ' + self.repo_dir)
        return result

    @staticmethod
    def is_collection(coll_path: str) -> bool:
        return os.path.isdir(coll_path) and os.path.isfile(os.path.join(coll_path, 'pagemarks.json'))

    def read_collection(self, coll_path: str) -> PagemarksCollection:
        result = PagemarksCollection()
        for root, dirs, files in os.walk(coll_path):
            for f in files:
                relative_path = os.path.join(root, f)
                if f == 'pagemarks.json':
                    with open(relative_path, "r") as json_file:
                        json_obj = commentjson.load(json_file)
                    if 'title' in json_obj and len(json_obj['title']) > 0:
                        result.title = json_obj['title'].strip()
                    if 'pinned-filters' in json_obj and isinstance(json_obj['pinned-filters'], list):
                        for expr in json_obj['pinned-filters']:
                            if isinstance(expr, str):
                                result.pinned_filters.append(expr.strip())
                            else:
                                raise PagemarksError('Pinned filter is not a string in ' + relative_path)
                else:
                    with open(relative_path, "r", encoding='utf-8') as json_file:
                        json_obj = json.load(json_file)
                    bmid = f[:-5]  # cut .json extension
                    bm = Bookmark(bmid, json_obj['url'].strip())
                    if 'name' in json_obj and isinstance(json_obj['name'], str):
                        bm.name = json_obj['name'].strip()
                    if 'date_added' in json_obj and isinstance(json_obj['date_added'], str):
                        bm.date_added = self.parse_timestamp(json_obj['date_added'].strip())
                    if 'tags' in json_obj and isinstance(json_obj['tags'], list):
                        bm.tags = normalize_tags(json_obj['tags'])
                    if 'notes' in json_obj and isinstance(json_obj['notes'], str):
                        bm.notes = json_obj['notes'].strip()
                    result.bookmarks.append(bm)
        result.bookmarks.sort(key=cmp_to_key(self.compare_by_date_added_desc))
        return result

    @staticmethod
    def compare_by_date_added_desc(a: Bookmark, b: Bookmark) -> int:
        date_a: int = int(a.date_added.replace(tzinfo=timezone.utc).timestamp()) if a.date_added is not None else 0
        date_b: int = int(b.date_added.replace(tzinfo=timezone.utc).timestamp()) if b.date_added is not None else 0
        if date_a > date_b:
            return -1
        elif date_a == date_b:
            if a.url > b.url:
                return 1
            elif a.url < b.url:
                return -1
            else:
                return 0
        else:
            return 1
