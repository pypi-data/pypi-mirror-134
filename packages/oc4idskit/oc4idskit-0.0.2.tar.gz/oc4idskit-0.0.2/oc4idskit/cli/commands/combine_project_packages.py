from ocdskit.cli.commands.base import OCDSCommand

from oc4idskit.combine import combine_project_packages


class Command(OCDSCommand):
    name = 'combine-project-packages'
    help = 'reads project packages from standard input, collects projects, and prints one project package'

    def add_arguments(self):
        self.add_package_arguments('project')

    def handle(self):
        kwargs = self.parse_package_arguments()

        output = combine_project_packages(self.items(), **kwargs)

        self.print(output)
