from setuptools import setup, find_packages

setup(
    name='grading-utils',
    version='0.2',
    description='A basic collection of tools to aid in the process of grading Python assignments while also '
                'attempting to reduce cheating through various methods.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='David Kanter Eivin',
    license='MIT',
    packages=find_packages(),
    test_suite='tests'
)