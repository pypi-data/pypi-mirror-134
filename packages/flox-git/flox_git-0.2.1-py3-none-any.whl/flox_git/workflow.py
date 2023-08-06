from git import Repo, GitCommandError

from floxcore.context import Flox
from floxcore.exceptions import PluginException


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


def push_changes(flox: Flox, out, **kwargs):
    """Push changes to remote"""
    repo = Repo(flox.working_dir)
    origin = repo.remote("origin")
    try:
        repo.git.push("--set-upstream", origin, repo.head.ref)
        out.success(f"Pushed to remote origin")
    except GitCommandError as e:
        raise PluginException("Failed to push to origin")


def workflow_finish(flox: Flox, out, **kwargs):
    """Switch back to default branch"""
    repo = Repo(flox.working_dir)
    repo.git.checkout("master")

    out.success(f"Switched back to default branch")
