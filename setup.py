from setuptools import setup, find_packages

setup_requires = []

install_requires = ['pyyaml']

dependency_links = []

setup(
    name = 'mobideep_helper',
    version = '0.0.1',
    description = 'MobiDeep Helper',
    author = 'leesak',
    author_email = 'is77@mobigen.com',
    packages = find_packages(),
    install_requires = install_requires,
    setup_requires = setup_requires,
    dependency_links = dependency_links,
    scripts=['bin/mobideep_run'],
    zip_safe = False,
    include_package_data = True)