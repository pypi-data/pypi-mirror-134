import os
import os.path
import backstage
from backstage import error
from backstage.core.releaser import release


def main():
    target = os.getcwd()
    app_pkg = backstage.get_app_pkg(target)
    try:
        release(target, app_pkg)
    except error.Error as e:
        print("Failed to upload a distribution package to PyPI")
        exit(1)
    except Exception:
        print("Unknown error while uploading a distribution package to PyPI")
        exit(1)


if __name__ == "__main__":
    main()
