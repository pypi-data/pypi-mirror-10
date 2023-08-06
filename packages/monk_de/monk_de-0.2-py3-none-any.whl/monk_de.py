# -*- coding: utf-8 -*-
#
# MONK Automated Development Environment
#
# Copyright (C) 2015 DResearch Fahrzeugelektronik GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 2 of the License, or (at your option) any later version.
#

""" MONK Automated Development Environment

See Readme
"""

import os.path as op
import configparser as cp
import json
import argparse

def require_dir(path):
    """ check if a directory exist and create it otherwise

    :param path: the dir to check
    """
    print("test ! -d {} && mkdir {}".format(
        path,
        path,
    ))

def cd(path):
    """ a simple wrapper for the shell command cd

    :param path: could be anything you can give 'cd' in bash
    """
    print("cd {}".format(path))

def comment(txt):
    """ a simple wrapper for a bash comment

    :param txt: the comment text
    """
    print()
    print("# {}".format(txt))

def start_session():
    """ creates a tmux session

    The name of the session is set to "monk-<timestamp>". Automatic renaming is
    deactived because we want to control the names of our sessions ourselves.
    """
    print("SESSION=\"monk-$(date +\"%H%M%s\")\"")
    print("tmux new-session -d -s $SESSION")
    print()
    print("tmux set-window-option -t $SESSION -g automatic-rename off")

def init_venv(name, venv_path=None):
    """ initialize a virtualenv

    pretty much calls teh source .../activate for the virtualenv

    :param name: name of the virtualenv to activate
    :param venv_path: where all the virtualenvs are
    """
    # TODO vpath, rpath and co be replaced by shell variables?
    vpath = venv_path or "venvs"
    print("tmux send-keys 'source {}/{}/bin/activate' Enter".format(
        vpath,
        name,
    ))

def init_devenv_window(name, venv, post_cmd=None, project_path=None, repo_path=None, venv_path=None):
    """ create a window and send initial commands

    :param name: how the window will be called
    :param venv: name of the corresponding virtualenv; separating this from
            name is valuable, if you want to run different venvs from the same
            repository.
    :param post_cmd: a shell command that will be executed at the end of the
            window creation.
    :param project_path: the path where all the code and venvs are
    :param repo_path: the path in project_path where the repos are
    :param venv_path: the path in project_path where the venvs are
    """
    ppath = project_path or op.expanduser("~/monk_de")
    rpath = repo_path or "repos"
    vpath = venv_path or "venvs"

    comment("initialize {}".format(name))
    print("tmux new-window -k -n \"{}\"".format(name))
    print("tmux send-keys 'cd {}' Enter".format(ppath))
    init_venv(venv)
    print("tmux send-keys 'cd {}' Enter".format(rpath))
    print("tmux send-keys 'cd {}' Enter".format(name))
    print("tmux send-keys 'git fetch' Enter")
    print("tmux send-keys 'clear' Enter")
    if post_cmd:
        print("tmux send-keys '{}' Enter".format(post_cmd))
    print("tmux send-keys 'git log --oneline --graph --decorate --all --max-count=10' Enter")

def finalize():
    """ the last steps to take

    goes bakc to the first window and attaches to the session
    """
    comment("finish it up")
    print("tmux select-window -t 0")
    print("tmux send-keys 'tmux rename-window overview' Enter")
    print("tmux send-keys 'clear' Enter")
    print()
    print("tmux -2 attach -t $SESSION")

class Path(object):
    """ a context manager, makes sure to leave the entered path in the end
    """

    def __init__(self, path):
        """
        :param path: the path that you want to cd to
        """
        self.path = path
        self.backup_var = "RETURN_FROM_{}".format(self.path.upper())

    def __enter__(self):
        print("{}=\"$(pwd)\"".format(self.backup_var))
        cd(self.path)

    def __exit__(self, *args, **kwargs):
        cd("${}".format(self.backup_var))
        print("{}=".format(self.backup_var))


def require_venv(name, venv_path=None):
    """ pyvenv if it doesn't exist yet

    :param name: the name of the venv to be checked
    :param venv_path: where the venvs are in the monk_de dir
    """
    comment("require venv {}".format(name))
    vpath = venv_path or "venvs"
    require_dir(vpath)
    with Path(vpath):
        print("test ! -d {} && pyvenv {}".format(
            name,
            name,
        ))

def require_repo(name, remote, repo_path=None):
    """ git clone if it doesn't exist yet

    :param name: the name of the repo to be checked
    :param repo_path: where the repos are in the monk_de dir
    """
    comment("require repo {}".format(name))
    rpath = repo_path or "repos"
    require_dir(rpath)
    with Path(rpath):
        print("test ! -d {} && git clone {} {}".format(
            name,
            remote,
            name,
        ))

def create(project, project_path=None, repo_path=None, venv_path=None, sources=None):
    """ create the bash script for a given project

    Creates an executable shell script as prints. Can be redirected to a file
    and then executed.
    """
    ppath = project_path or op.expanduser("~/monk_de")
    rpath = repo_path or "repos"
    vpath = venv_path or "venvs"
    sources = sources or [
        op.expanduser("."),
        op.expanduser("~"),
        ppath,
    ]
    config = cp.ConfigParser()
    for src in sources:
        if op.isdir(src):
            config.read(op.join(
                ppath,
                project+".ini",
            ))
            break

    print("#!/bin/bash")
    comment("start project environment")
    require_dir(ppath)
    cd(ppath)
    comment("creates repos when needed")
    for s in config.sections():
        section=config[s]
        require_repo(section["path"], section["repo"], rpath)
        require_venv(section["venv"], vpath)
    comment("start new session")
    start_session()
    comment("initialize devenvs")
    for s in config.sections():
        section=config[s]
        init_devenv_window(s, section["venv"], section.get("post", ""), ppath, rpath)
    finalize()

def main():
    parser = argparse.ArgumentParser(
            description="create a tmux environment to develop your python projects in")
    parser.add_argument("project", type=str,
            help="The name of the project to load. You should have an ini file with the same name, either in \".\" in \"~\" or in your project location (\"~/monk_de\")")
    args = parser.parse_args()
    if not args.project:
        raise Exception("A project is needed to initialize it")
    create(args.project)

if __name__ == "__main__":
    main()
