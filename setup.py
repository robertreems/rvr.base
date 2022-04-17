from setuptools import find_packages, setup
setup(
    name='rvr_base',
    packages=find_packages(include='rvr_base'),
    version='0.0.2',
    description='Roberts base module',
    author='Robert van Reems',
    license='MIT',
    install_requires=[
          'notify_run',
          'dbus-python'
      ],
)