from setuptools import setup, find_packages

setup(
    name = "pymultinode",
    version = "0.0",
    packages = find_packages(),

    install_requires = ['docutils>=0.3', 'eventlet>=0.9.13', 'mako>=0.3.5'],

    scripts = ['multinode.py'],

    package_data = {
        '' : ['*.rst']
    },

    author = "Winston Ewert",
    author_email = "coder@winstonewert.com",
    description = "Nearly effortless python clustering"
)
