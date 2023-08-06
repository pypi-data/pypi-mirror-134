# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.2.8, copyright Friday, 14 January 2022
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from logging import log, INFO

from os import walk, getcwd
from os.path import join, basename
from zipfile import ZipFile

from auxilium.tools.const import ICONS


def archive(name=basename(getcwd()), path=getcwd(), venv=None):
    """ archive project in zip file to '..' """
    log(INFO, ICONS["archive"] + 'archive project in zip file ')
    raise NotImplementedError()
    with ZipFile(join(path, '..', name + '.zip'), 'w') as z:
        for root, dirs, files in walk(path):
            print(root)
            if not root.startswith('.'):
                for file in files:
                    print(file)
                    z.write(join(root, file))
                # for directory in dirs:
                #     if not directory.startswith('.'):
                #         z.write(join(root, directory))
