from git import Repo, GitCommandError

from floxcore.context import Flox
from floxcore.exceptions import PluginException

from loguru import logger

def create_branch(flox: Flox, out, flow_id, **kwargs):
    """Create branch"""
    repo = Repo(flox.working_dir)

    try:
        repo.git.checkout(flow_id)
        out.info(f"Switched to existing branch '{flow_id}'")
    except GitCommandError:
        branch = repo.create_head(flow_id)
        branch.checkout()
        out.success(f"Created and switched to new branch '{flow_id}'")


def add_files(flox: Flox, out, message, **kwargs):
    """Add current state to git repository"""
    repo = Repo(flox.working_dir)

    try:
        repo.git.add("-A")
        repo.git.commit("-m", message)
        out.success("Committed current state of work")
    except GitCommandError:
        pass


def pull_changes(flox: Flox, out, branch, **kwargs):
    """Pull changes from remote"""
    repo = Repo(flox.working_dir)
    try:
        logger.debug("pull")
        repo.git.branch(f"--set-upstream-to=origin/{branch}", branch)
        repo.git.pull()
        out.success(f"Pulled from remote origin")
    except GitCommandError as e:
        raise PluginException(f"Failed to pull")


def push_changes(flox: Flox, out, **kwargs):
    """Push changes to remote"""
    repo = Repo(flox.working_dir)
    origin = repo.remote("origin")
    try:
        repo.git.push("--set-upstream", origin, repo.head.ref)
        out.success(f"Pushed to remote origin")
    except GitCommandError as e:
        raise PluginException(f"Failed to push to origin. {e.stderr}")


def workflow_finish(flox: Flox, out, **kwargs):
    """Switch back to default branch"""
    repo = Repo(flox.working_dir)
    repo.git.checkout("master")

    out.success(f"Switched back to default branch")
