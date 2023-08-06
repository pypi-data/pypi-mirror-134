import os
import os.path
import shlex
import subrun
from shared import Jason
from backstage.core import constant
from backstage import error
from backstage.core.funcs import get_app_pkg


def run_tasks(operation, project_dir, app_pkg=None):
    app_pkg = app_pkg if app_pkg else get_app_pkg(project_dir)
    tasks_file = os.path.join(project_dir, app_pkg, ".pyrustic",
                              "backstage", "config",
                              "{}.tasks".format(operation))
    if not os.path.exists(tasks_file):
        tasks_file = os.path.join(constant.BACKSTAGE_HOME, "config",
                                  "{}.tasks".format(operation))
    if not os.path.exists(tasks_file):
        raise error.NoTasksError
    tasks = parse_tasks_file(tasks_file)
    if not tasks:
        raise error.NoTasksError
    for task in tasks:
        info = subrun.run(task.strip(), cwd=project_dir)
        if info.return_code != 0:
            return


def parse_tasks_file(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def OLDrun_tasks(operation, project_dir, app_pkg=None):
    app_pkg = app_pkg if app_pkg else get_app_pkg(project_dir)
    local_config = os.path.join(project_dir, ".pyrustic", "backstage", "config")
    local_config_file = os.path.join(local_config,
                                     "{}.json".format(operation))
    if os.path.isfile(local_config_file):
        jason = Jason("init.json", default=[], location=local_config)
    else:
        jason = Jason("{}.json".format(operation), default=[],
                      location=constant.BACKSTAGE_CONFIG)
    if not jason.data:
        raise error.NoTasksError
    for item in jason.data:
        cmd = shlex.split(item)
        cmd.insert(0, "-m")
        info = subrun.run(cmd, cwd=project_dir)
        if info.return_code != 0:
            return
