import json

from fabric.api import env, task, execute, parallel, run


INSTALL = True
UNINSTALL = False
env.always_use_pty = False
env.warn_only = True

@task
def execute_steps(**kwargs):
    """Executes installation/uninstallation steps.

    This function assumes that fabric environment variables are set before
    execution.
    """
    steps = kwargs['steps']
    for step in steps:
        run(step)

@task
def manage_package(package, machine):
    """Sets fabric env variables
    and initiates installation steps execution
    """
    env.user = machine.user
    env.key_filename = machine.key
    hosts = [machine.endpoint]
    execute(execute_steps, steps=package['steps'], hosts=hosts)

def print_packages(machines):
    """Prints Packages while dryrun of the script"""
    for machine, packages in machines.iteritems():
        print 'Operating on {machine}'.format(machine=machine.endpoint)
        for package in packages:
            print 'Package-Name: {pkg_name}'.format(pkg_name=package["package_name"])
            print 'Steps:'
            print json.dumps(package['steps'], indent=4)

def manage_dependencies_on_machine(machine, packages):
    """Handles the dependencies on a given machine
    """
    for package in packages:
        manage_package(package, machine)
