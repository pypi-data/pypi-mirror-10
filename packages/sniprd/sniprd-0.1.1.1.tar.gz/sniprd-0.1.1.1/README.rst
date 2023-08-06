
======================
    sniprd
======================

.. image:: https://badge.fury.io/py/sniprd.svg
    :target: http://badge.fury.io/py/sniprd

.. image:: https://travis-ci.org/kejbaly2/sniprd.svg?branch=master
    :target: https://travis-ci.org/kejbaly2/sniprd

.. image:: https://coveralls.io/repos/kejbaly2/sniprd/badge.svg 
    :target: https://coveralls.io/r/kejbaly2/sniprd

.. image:: https://img.shields.io/pypi/dm/sniprd.svg
    :target: https://pypi.python.org/pypi/sniprd/

.. image:: https://img.shields.io/pypi/l/sniprd.svg
    :target: https://pypi.python.org/pypi/sniprd/
 
.. image:: https://landscape.io/github/kejbaly2/sniprd/master/landscape.svg
    :target: https://landscape.io/github/kejbaly2/sniprd/master


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Track your activities, comfortably.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DESCRIPTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comfortably archive snips of the stuff you get done. Compatible 
with status-report. Beautiful. Made for Humans.


EXAMPLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Save a basic snippet with now() timestamp::

    snip #home #car I went to the post-office to buy stamps

Save a snippet as completed yesterday::

    snip yesterday #project_x reported 36 bugs in BZ, 14 in JIRA

Save a snippet as completed on a specific date in the past::

    snip 2015-01-01 pushed 14 code #commits

Save a snippet and connect with others involved::

    snip washed dads car today @philly @dad #allowance

Save multiple snippets at once completed the day before yesterday::

    snip -1 #project_x did this; #private arrived 30m late

See snippet --help for complete list of available commands.


To retrieve your current week's saved snippets, use status-report::

    status-report --snippets project_x

To sync your current week's saved snippets with a remote db::

    snip sync project_x [https://kejbaly2.sniprd.com]


INSTALLATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install directly from Fedora/Copr repository or use PIP::

    # Basic dependencies for buiding/installing pip packages
    sudo yum install gcc krb5-devel
    sudo yum install python-devel python-pip python-virtualenv

    # Upgrade to the latest pip/setup/virtualenv installer code
    sudo pip install -U pip setuptools virtualenv

    # Install into a python virtual environment (OPTIONAL)
    virtualenv --no-site-packages ~/virtenv_sniprd
    source ~/virtenv_sniprd/bin/activate

    # Install sniprd (sudo required if not in a virtualenv)
    pip install sniprd


CONFIGURATION - sniprd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The config file ~/.sniprd is used to store general settings::

    [general]
    uri = ~/.sniprd.db  # DEFAULT

    # push (sync) ALL sniprd to another db
    [push]
    uri = postgresql://user:pass@sniphub.com/shared
    exclude_tags = ["private", "confidential"]
    exclude_regex = ["secret_code", "fsck"]

    # push sniprd with hashtag #home to another db
    [push-home]
    uri = postgresql://user:pass@server.com/db:5432

    # email #project_x sniprd to someone
    [push-project_x]
    uri = email://get@it.done
    include_tags = ["project_x"]

    [at-philly]
    uri = email://philly@cheeze.com


DOCKER INSTALL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To build and execute in a docker container, run::

    make run_docker

See LINKS section below for more docker resources.


GIT COMMIT HOOKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you're planning to make commits to this project, please enable
the following git hooks::

    # UPDATE according to the correct absolute git path
    PATH = ~/sniprd/git-hooks
    ln -s $(PATH)/pre-commit.py .git/hooks/pre-commit
    ln -s $(PATH)/commit-msg.py .git/hooks/commit-msg


TESTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run tests using pytest::

    # sudo required if not in a virtualenv
    pip install pytest coveralls
    coverage run --source=sniprd -m py.test source/tests
    coverage report


LINKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Release notes:
# LINK TO READTHEDOCS.COM/README

Git repo:
https://github.com/cward/sniprd

PIP repo:
https://pypi.python.org/pypi/sniprd/

Docker Guides:
https://fedoraproject.org/wiki/Getting_started_with_docker
https://fedoraproject.org/wiki/Docker


AUTHORS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chris Ward


COPYRIGHT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2015 Red Hat, Inc. All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of
the License, or (at your option) any later version.
