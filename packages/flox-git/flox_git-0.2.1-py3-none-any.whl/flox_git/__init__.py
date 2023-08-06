from flox_git.project import configure_branches, clone_repository, init_repository, create_default_gitignore, \
    commit_flox_files
from flox_git.workflow import create_branch, add_files, push_changes, workflow_finish

from floxcore.command import Stage
from floxcore.config import Configuration, ParamDefinition
from floxcore.context import Flox
from floxcore.plugin import Plugin


class GitConfiguration(Configuration):
    def parameters(self):
        return (
            ParamDefinition("required_branches", "Required branches", default=["master", "develop"], multi=True),
        )

    def schema(self):
        pass


class GitPlugin(Plugin):
    def configuration(self):
        return GitConfiguration()

    def handle_project(self, flox: Flox):
        return (
            Stage(init_repository, 1950),
            Stage(clone_repository, 1950),
            Stage(create_default_gitignore),
            Stage(commit_flox_files),
            Stage(configure_branches),
            Stage(push_changes, priority=-100),
        )

    def handle_workflow_start(self, flox: Flox, **kwargs):
        return (
            Stage(create_branch),
        )

    def handle_workflow_publish(self, flox: Flox, **kwargs):
        return (
            Stage(add_files, priority=200),
            Stage(push_changes, priority=200),
        )

    def handle_workflow_finish(self, flox: Flox, **kwargs):
        return (
            Stage(workflow_finish, priority=1),
        )


def plugin():
    return GitPlugin()
