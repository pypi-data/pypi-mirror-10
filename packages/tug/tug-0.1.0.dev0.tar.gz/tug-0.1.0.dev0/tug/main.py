from __future__ import print_function
from __future__ import unicode_literals
from inspect import getdoc
from operator import attrgetter

import re
import signal
import sys
import os
from os import path

from docopt import docopt, DocoptExit

from compose import config
from compose.project import Project
from compose.cli.log_printer import LogPrinter

from .client import docker_client
from .__init__ import __version__

from docker.errors import APIError
from compose.project import NoSuchService, ConfigurationError
from compose.service import BuildError
from compose.legacy import LegacyContainersError

import docker
import dockerpty

def main():
  try:
    Usage()
  except KeyboardInterrupt:
    print("\nAborting.")
    sys.exit(1)
  except (NoSuchService, ConfigurationError, LegacyContainersError) as e:
    print(e.msg)
    sys.exit(1)
  except APIError as e:
    print(e.explanation)
    sys.exit(1)
  except BuildError as e:
    print("Service '{service}' failed to build: {reason}".format(
      service=e.service.name,
      reason=e.reason))
    sys.exit(1)
# tug2 exec PROJECT SERVICE [COMMANDS ...]
class Usage(object):
  """Describe your infrastructure with yaml files.

  Usage:
    tug2 ps
    tug2 COMMAND PROJECT [SERVICES ...]

  Common Commands:

    ps             List all running and available projects
    up             Update and run services
    diff           Describe the changes needed to update
    cull           Stop and delete services
    logs           Display container logs
    exec           Run a command inside a container (not implemented yet)

  Management Commands:

    kill           Gracefully terminate services
    down           Stop services
    rm             Delete services
    recreate       Stop, delete, then run services
    build          Build services
    rebuild        Build services from scratch

  Options:

    -h --help      Display this usage information
    -v --version   Display the version number

  """
  def __init__(self):
    docstring = getdoc(Usage)
    options = None
    try:
      options = docopt(docstring,
        argv=sys.argv[1:],
        version=__version__,
        options_first=True)
    except DocoptExit:
      raise SystemExit(docstring)

    if 'ps' in options and options['ps']:
      self._ps()
      return

    # if 'exec' in options and options['exec']:
    #   self._exec(options['PROJECT'], options['SERVICE'], options['COMMANDS'])
    #   return

    # command references a function on this class
    command = options['COMMAND']
    if not hasattr(self, command):
      print('{command} command not found'.format(command=command))
      sys.exit(1)

    projectname = options['PROJECT']
    servicenames = options['SERVICES']

    handle = getattr(self, command)
    handle(projectname, servicenames)

  def _clean_project_name(self, name):
    # remove .yml and .yaml to get back to project name
    # this is sugar
    if name.endswith('.yml'):
      name = name[:-4]
    if name.endswith('.yaml'):
      name = name[:-5]
    return name

  def _get_config(self, name):
    filename = path.abspath('{name}.yml'.format(
      name=name))
    return config.load(filename)

  def _get_projectnames_in_dir(self):
    return [self._clean_project_name(file) for file in os.listdir(os.getcwd()) if file.endswith('.yaml') or file.endswith('.yml')]

  def _ps(self):
    client = docker_client()
    projectnames = self._get_projectnames_in_dir()
    containers = client.containers(all=True)
    unknown = {}
    for container in containers:
      unknown[container['Id']] = client.inspect_container(container['Id'])
    if len(projectnames) != 0:
      print()
    for projectname in projectnames:
      config = self._get_config(projectname)
      project = Project.from_dicts(
        projectname,
        config,
        client)
      services = project.get_services()

      counts = {}

      for service in services:
        c = service.containers(stopped=True) + service.containers(one_off=True)
        if len(c) == 0:
          if not 'Uncreated' in counts:
            counts['Uncreated'] = 0
          counts['Uncreated'] += 1
        for container in c:
          del unknown[container.id]
          if not container.human_readable_state in counts:
            counts[container.human_readable_state] = 0
          counts[container.human_readable_state] += 1

      humancounts = []
      for state in counts:
        humancounts.append('{count} {state}'.format(
          count=counts[state],
          state=state))
      print('  {name: <24}{counts}'.format(
        name=projectname,
        counts=','.join(humancounts)))

    if len(unknown) != 0:
      print()
      print('  Containers not tracked by compose/tugboat:')
      print()
    for key in unknown:
      detail = unknown[key]
      name = detail['Name']
      if name.startswith('/'):
        name = name[1:]
      ip = detail['NetworkSettings']['IPAddress']
      if ip == '':
        ip = '(host)'
      print('  {name: <24}{state: <12}{ip: <17}'.format(
        name=name,
        state='',
        ip=ip))
    print()

  def ps(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    print()
    print('  {name} services:'.format(name=projectname))
    print()
    services = project.get_services(service_names=servicenames)
    for service in services:
      containers = service.containers(stopped=True) + service.containers(one_off=True)
      if len(containers) == 0:
        print('  {name: <24}{state: <12}{ip: <17}'.format(
          name=service.name,
          state='Uncreated',
          ip=''))
      for container in containers:
        name = container.name_without_project
        ip = container.get('NetworkSettings.IPAddress')
        if ip == '':
          ip = '(host)'
        state = container.human_readable_state
        print('  {name: <24}{state: <12}{ip: <17}'.format(
          name=name,
          state=state,
          ip=ip))
    print()

  def build(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.build(service_names=servicenames, no_cache=False)

  def rebuild(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.build(service_names=servicenames, no_cache=True)

  def kill(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.kill(service_names=servicenames, signal='SIGTERM')

    self.ps(projectname, servicenames)

  def logs(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    containers = project.containers(service_names=servicenames, stopped=True)
    print('Attaching to', ', '.join(c.name for c in containers))
    LogPrinter(containers, attach_params={'logs': True}).run()

  def pull(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.pull(service_names=servicenames)

  def rm(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.remove_stopped(service_names=servicenames)

    self.ps(projectname, servicenames)

  def down(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.kill(service_names=servicenames, signal='SIGTERM')
    project.stop(service_names=servicenames)

    self.ps(projectname, servicenames)

  def cull(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.kill(service_names=servicenames, signal='SIGTERM')
    project.stop(service_names=servicenames)
    project.remove_stopped(service_names=servicenames)

    self.ps(projectname, servicenames)

  def recreate(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.restart(service_names=servicenames)

    self.ps(projectname, servicenames)

  def up(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)
    project.up(
      service_names=servicenames,
      smart_recreate=True)

    self.ps(projectname, servicenames)

  def diff(self, projectname, servicenames):
    client = docker_client()
    config = self._get_config(projectname)
    project = Project.from_dicts(
      projectname,
      config,
      client)

    services = project.get_services(servicenames, include_deps=True)
    plans = project._get_convergence_plans(services, smart_recreate=True)

    print()
    print('  {name} convergence plan:'.format(name=projectname))
    print()
    for service in plans:
      plan = plans[service]
      containers = []
      for container in plan.containers:
        containers.append(container.name)
      print('  {name: <24}{action: <12}{containers}'.format(
        name=service,
        action=plan.action,
        containers=', '.join(containers)))
    print()

  # def _exec(self,projectname, servicename, commands):
  #   client = docker_client()
  #   config = self._get_config(projectname)
  #   project = Project.from_dicts(
  #     projectname,
  #     config,
  #     client)
  #   containers = project.containers(service_names=[servicename])
  #   container = containers[0]
  #   command = commands
  #   if command == None or not command:
  #     command = ['/bin/bash']
  #   execute = client.exec_create(container.id, command, tty=True)
  #   result = client.exec_start(execute.Id, tty=True, stream=True)
  #   print(execute)
  #   sys.exit(exit_code)