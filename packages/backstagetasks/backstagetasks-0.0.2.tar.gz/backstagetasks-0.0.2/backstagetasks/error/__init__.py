class Error(Exception):
    pass


class NoTasksError(Error):
    pass


class BuildError(Error):
    pass


class MissingSysExecutableError(Error):
    pass
