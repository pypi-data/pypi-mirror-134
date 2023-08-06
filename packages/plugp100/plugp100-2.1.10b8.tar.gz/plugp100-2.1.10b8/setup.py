import os
import platform
import sys
from typing import Optional

from setuptools import setup, find_packages


def requirements_filename_by_arch() -> Optional[str]:
    requirements_arch_file = f'requirements-{platform.machine().lower()}.txt'
    if os.path.exists(requirements_arch_file):
        return requirements_arch_file
    else:
        return 'requirements.txt'


with open('README.md') as readme_file:
    README = readme_file.read()

with open(requirements_filename_by_arch()) as requirements_file:
    COMPLIANT_PYPI_REQUIREMENTS = filter(lambda requirement: "http" not in requirement, requirements_file.read().split("\n"))

setup_args = dict(
    name='plugp100',
    version='2.1.10b8',
    install_requires=COMPLIANT_PYPI_REQUIREMENTS,
    description='Controller for TP-Link Tapo P100 and other devices',
    long_description_content_type="text/markdown",
    long_description=README,
    license='GPL3',
    packages=find_packages(),
    author='@petretiandrea',
    author_email='petretiandrea@gmail.com',
    keywords=['Tapo', 'P100'],
    url='https://github.com/petretiandrea/plugp100',
    download_url='https://github.com/petretiandrea/plugp100',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable'
    ],
    include_package_data=True,
    package_data={'': ['requirements*.txt']},
)


def execute_custom_install(executable: str, requirements_file: str) -> int:
    if 'python' in executable and requirements_file:
        command = f'"{executable}" -m pip install -r {requirements_file}'
    elif 'pip' in executable and requirements_file:
        command = f'"{executable}" install -r {requirements_file}'
    else:
        command = ''
    if command:
        return os.system(command)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != 'sdist' and sys.argv[1] != 'bdist_wheel':
        if execute_custom_install(sys.executable, requirements_filename_by_arch()) != 0:
            exit(-1)
    setup(**setup_args)

# def get_dependency_links() -> [str]:
#     requirements_arch = requirements_filename_by_arch()
#     if requirements_arch:
#         with open(requirements_arch) as dependency_links_file:
#             return dependency_links_file.read().split('\n')
#     else:
#         return []
