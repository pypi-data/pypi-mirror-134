from setuptools import setup, find_packages

setup(
    name='grading-utils',
    version='0.1.1',
    description='A basic collection of tools to aid in the process of grading Python assignments while also '
                'attempting to reduce cheating through various methods.',
    author='David Kanter Eivin',
    license='MIT',
    packages=find_packages(),
    test_suite='tests'
)