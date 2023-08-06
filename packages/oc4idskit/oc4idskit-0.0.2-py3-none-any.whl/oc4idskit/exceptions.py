class OC4IDSKitWarning(UserWarning):
    """Base class for warnings from within this package"""


class MissingProjectsWarning(OC4IDSKitWarning):
    """Used when the "projects" field is missing from a project package when combining packages"""

    def __str__(self):
        return 'item {0} has no "projects" field (check that it is a project package)'.format(*self.args)
