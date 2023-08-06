"""Project Backstage API"""
from backstagetasks.core.initialization import initialized, initialize
from backstagetasks.core.building import build
from backstagetasks.core.lite_test_runner import run_tests
from backstagetasks.core.versioning import get_version, set_version, interpret_version
from backstagetasks.core.funcs import get_app_pkg, get_project_name, ask_for_confirmation
from backstagetasks.core.dist import dist_version, dist_info, get_setup_config


__all__ = ["initialized", "initialize", "build",
           "run_tests", "get_version", "set_version", "interpret_version",
           "get_app_pkg", "get_project_name", "ask_for_confirmation", "dist_version",
           "dist_info", "get_setup_config"]
