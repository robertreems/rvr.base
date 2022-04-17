# rvr.base
This is Roberts personal base module. Currently it provides the following functionality:
- Logging to Azure log analytics
- Sending notifications using https://notify.run/
- Querying configuration from a single configuration (.ini) file.


# Prerequistes
You'll need an Azure log analytics workspace. This is where the logs are send to.
This module is developed for Linux and tested only on Ubuntu 20.04 using Python 3.8.10.

**The configurationfile**
The configuration file is used for some configuration settings like the Log analytics workspace and password... it's a bad practice I know... Perhaps I'll improve the security later on. The file is located in '/etc/rvr/config.ini'.

The file requires the following content:
```
[AZ_LOG_ANALYTICS_WORKSPACE]
workspace_id = ID OF YOUR WORKSPACE
primary_key = THE KEY OF  YOUR WORKSPACE
``` 

# Building
**Prerequistes for building**
Make sure you'll have the following PIP packages installed:
- wheel
- setuptools
- twine

**Build the module**
Make sure the cursor is the root folder of the project and run:
`python3 setup.py bdist_wheel`

Be sure to test newly build module by installing it on a new venv:
`pip3 install dist/rvrbase-<VERSION AND THE REST OF THE FILE>`
You're advised to create a new virtual environment and test the package there.


# Using the module
An example says more than 1000 words in my opinion. Please see the example.py file in this project for examples.

# Distributing the module
python3 -m twine upload dist/* --verbose -u <PyPi username>

# Credits
Kia Eisinga for writning a good explaination on how to create a Python package
https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
Joel barmettler for explaining how to upload a Python package.
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

# Other sources used
https://packaging.python.org/en/latest/tutorials/packaging-projects/