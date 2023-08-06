import os
import os.path
import time
import subrun
from shared import Jason
from backstage.core.funcs import get_app_pkg
from backstage.core import versioning
from backstage import error


def release(project_dir, app_pkg=None):
    app_pkg = app_pkg if app_pkg else get_app_pkg(project_dir)
    # version
    version = versioning.get_version(project_dir)
    command = "twine upload --skip-existing dist/*"
    info = subrun.run(command, cwd=project_dir)
    if info.return_code == 0:
        _update_build_report(project_dir, app_pkg, version)
    else:
        raise error.Error


def _update_build_report(project_dir, app_pkg, version):
    backstage_data_path = os.path.join(project_dir, app_pkg,
                                       ".pyrustic",
                                       "backstage",
                                       "data")
    jason = Jason("build_report.json", default=[],
                  location=backstage_data_path)
    if not jason.data:
        raise error.Error("Missing valid 'build_report.json' !")
    latest_build_report = jason.data[-1]
    if not latest_build_report["release_timestamp"]:
        latest_build_report["release_timestamp"] = int(time.time())
        jason.save()
