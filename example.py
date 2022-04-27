# Please make sure PYTHONPATH is set to the src directory before running this script.

import rvrbase as rvrbase

# Log something.
thelogger = rvrbase.Rvrlogger()
thelogger.log_application_event(
    type='warning', message='No worries, just testing here.')

# print something from the configuration file.
rvrconfig = rvrbase.Rvrconfig(rvrbase.CONFIG_FILE)
print(rvrconfig.q1('hwip'))
