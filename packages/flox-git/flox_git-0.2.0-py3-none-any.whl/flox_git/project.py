import re
from os.path import isdir, join, isfile

import click
from git import Repo, GitCommandError, rmtree

from floxcore.context import Flox

from loguru import logger


def init_repository(flox: Flox, out, **kwargs):
    """Initialise Git repository"""
    if isdir(join(flox.working_dir, ".git")):
        out.info("Using already initialised repository")
        return

    Repo.init(flox.working_dir)
    out.success("Initialised git repository")


def clone_repository(flox: Flox, out, **kwargs):
    """Clone remote repository"""
    if "git_repository" not in kwargs:
        out.warning("Unable to clone remote repository. Consider installing flox-github plugin.")
        return

    remote = kwargs.get("git_repository")
    repo = Repo(flox.working_dir)

    if "origin" not in repo.remotes:
        repo.create_remote('origin', remote)
        out.success(f"Added new remote origin with {re.sub('.*@', '', remote)}")

    origin = repo.remote("origin")
    origin.fetch()

    if "master" not in repo.branches:
        try:
            repo.git.pull("origin", "master")
        except GitCommandError as e:
            if "The following untracked working tree files would be overwritten by" in e.stderr \
                    and ".flox/metadata" in e.stderr:
                rmtree(flox.local_config_dir)
            repo.git.pull("origin", "master")

        out.success(f"Created new master branch")
    else:
        repo.git.checkout("master")

    out.success(f"Switched to master branch")


def create_default_gitignore(flox: Flox, out, **kwargs):
    """Create default .gitignore"""
    ignore_file = join(flox.local_config_dir, ".gitignore")
    if isfile(ignore_file):
        out.info(".gitignore already exists")
        return

    with open(ignore_file, "w+") as f:
        f.write("\n".join((
            "local",
            ".cache"
        )))

    out.success(f"Created default .gitignore: {click.format_filename(ignore_file)}")


def commit_flox_files(flox: Flox, out, **kwargs):
    """Add flox meta files to git repository"""
    repo = Repo(flox.working_dir)
    try:
        repo.git.add("-A", ".flox")
        repo.git.commit("-m", "Add flox meta files")
        out.success("Added flox meta files to git repository")
    except GitCommandError as e:
        pass

    try:
        for f in kwargs.get("bootstrap_generated", []):
            repo.git.add("-A", f)

        repo.git.commit("-m", "Add flox bootstrapped files")
        out.success("Added flox bootstrapped files to git repository")
    except GitCommandError as e:
        pass


def configure_branches(flox: Flox, out, **kwargs):
    """Configure Git branches"""
    from flox_git import push_changes
    repo = Repo(flox.working_dir)
    for branch_name in flox.settings.git.required_branches or []:
        if branch_name in repo.branches:
            out.info(f"Skipping branch {branch_name} as branch already exists")
        else:
            repo.git.checkout("-b", branch_name)
            push_changes(flox=flox, out=out, **kwargs)
            out.success(f"Created branch {branch_name}")

    repo.git.checkout("master")
