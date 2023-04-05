from setuptools import find_packages, setup
setup(
    name='perfecto_token_provider',
    packages=find_packages(include=['perfecto_token_provider']),
    version='0.1.0',
    description='Simple utility to provide Perfecto tokens from simple file storage',
    author='Hristo Genev',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)