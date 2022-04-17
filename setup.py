from setuptools import find_packages, setup
setup(
    name='rvrbase',
    packages=find_packages(include='rvrbase'),
    version='0.0.1',
    description='Roberts base module',
    author='Robert van Reems',
    license='MIT',
    install_requires=[
          'notify_run',
          'dbus-python'
      ],
)