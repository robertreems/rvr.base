# rvr.base
This is Roberts personal base module. Currently it provides the following functionality:
- Logging to Azure log analytics
- Sending notifications using https://notify.run/
- Querying configuration from a single configuration (.ini) file.

## Prerequistes
You'll need an Azure log analytics workspace. This is where the logs are send to.
This module is developed for Linux and tested on:
- Ubuntu 20.04 using Python 3.8.10.
- Raspberry Pi OS using Python 3.9.2

**The configurationfile**
The configuration file is used for some configuration settings like the Log analytics workspace and password... it's a bad practice I know... Perhaps I'll improve the security later on. The file is located in '/etc/rvr/config.ini'.

The file requires the following content:
```
[AZ_LOG_ANALYTICS_WORKSPACE]
workspace_id = ID OF YOUR WORKSPACE
primary_key = THE KEY OF  YOUR WORKSPACE
``` 

## Installing the module
Just install the module with `pip3 install rvr-base`.

## Using the module
An example says more than 1000 words in my opinion. Please see the example.py file in this project for examples.

## Building
**Prerequistes for building**
Make sure you'll have the following PIP packages installed:
- wheel
- setuptools
- twine

**Build the module**
Make sure the cursor is the root folder of the project and run:
`python3 -m build`

## Distributing the module
python3 -m twine upload dist/* --verbose -u <PyPi username>

## Testing the build module
Yeah I know, this isn't proper testing. But for now I've got to do with it.
Here is an example:

```Bash
# create a Python virtual environment:
python3 -m venv venv

# Make the environment active
source venv/bin/activate

# Install the build module
pip3 install ./dist/rvrbase-<VERSION AND THE REST OF THE FILE>.whl

#Run the example script
python3 example.py
```

## Sources used
https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Disclaimer
This module has been written for my personal use. Feel free to use it but at your own discression. There is no support or whatsoever on my part. 