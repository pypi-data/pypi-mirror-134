import os
from typing import Iterable
from typing import List

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


def parse_requirements(requirement_list: List[str]) -> Iterable[str]:
    for requirement in requirement_list:
        if not requirement.startswith('-r'):
            yield requirement
        else:
            file_to_read = requirement.lstrip('-r ')
            with open(os.path.join('requirements', file_to_read)) as req_file:
                for in_requirement in parse_requirements(req_file.readlines()):
                    yield in_requirement


def get_client_requirements():
    with open(os.path.join('requirements', 'client_requirements.txt'), 'r') as req_file:
        return list(parse_requirements(req_file.readlines()))


def run_setup():
    with open(rel('artifacts_proxy', '__init__.py'), 'r') as f:
        version_marker = '__version__ = '
        for line in f:
            if line.startswith(version_marker):
                _, version = line.split(version_marker)
                version = version.strip().strip('\'').strip('"')
                break
        else:
            raise RuntimeError("Version marker not found.")

    setup(name='artifacts-service',
          version=version,
          url='https://bitbucket.org/intezer/artifacts',
          author='Intezer Labs Ltd.',
          author_email='info@intezer.com',
          zip_safe=False,
          include_package_data=True,
          install_requires=get_client_requirements(),
          packages=['artifacts_proxy', 'artifact_normalization'])


run_setup()
