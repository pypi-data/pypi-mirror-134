from setuptools import setup, find_packages

setup(
    name='grading-utils',
    versions='0.1',
    description='A basic collection of tools to aid in the process of grading Python assignments while also '
                'attempting to reduce cheating through various methods.',
    author='David Kanter Eivin',
    license='MIT',
    package=find_packages(),
    test_suite='tests'
)