#!/usr/bin/python
# -*- coding: utf-8 -*-

# pkg_find.py file is part of slpkg.

# Copyright 2014-2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# Slpkg is a user-friendly package manager for Slackware installations

# https://github.com/dslackw/slpkg

# Slpkg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from messages import Msg
from pkg.manager import PackageManager
from __metadata__ import MetaData as _m


def find_from_repos(pkg):
    '''
    Find packages from enabled repositories
    '''
    cache = ""
    count_pkg = count_repo = 0
    print("\nPackages with name matching [ {0}{1}{2} ]\n".format(
        _m.color['CYAN'], ", ".join(pkg), _m.color['ENDC']))
    Msg().template(78)
    print("| {0}  {1}{2}{3}".format("Repository", "Package", " " * 54, "Size"))
    Msg().template(78)
    for repo in _m.repositories:
        PACKAGES_TXT = PackageManager(pkg).list_lib(repo)
        packages, sizes = PackageManager(pkg).list_greps(repo, PACKAGES_TXT)
        for find, size in zip(packages, sizes):
            for p in pkg:
                if p in find:
                    if cache != repo:
                        count_repo += 1
                    cache = repo
                    count_pkg += 1
                    print("  {0}{1}{2} {3}{4:>11}".format(
                        repo, " " * (12 - len(repo)),
                        find, " " * (53 - len(find)),
                        size))
    print("\n{0}Total found {1} packages in {2} repositories.{3}\n".format(
        _m.color['GREY'], count_pkg, count_repo, _m.color['ENDC']))
