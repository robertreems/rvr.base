# Please make sure PYTHONPATH is set to the src directory before running this script.

import rvrbase as rvrbase

# Log something.
newdelegate = rvrbase.Rvrbase(rvrbase.CONFIG_FILE)
# logs to both the system (using logger) and Azure.
newdelegate.log_app_event(
    type='warning', message='Dit is een test met nieuw design pattern.')
# Sends the message to Azure only.
newdelegate.send_az_app_event(type='info', message='Just relax.')
# sends a metric to Azure only.
newdelegate.send_az_metric(log_type='info', metric_name='somemetric', value=5)

# Send a notification to the browser(s)
newdelegate.send_browser_notification(
    type='info', message='No worries, just testing here.')

# print something from the configuration file.
print(newdelegate.q1('hwip'))

# Test read a metric from azure loganalytics
print(newdelegate.azlog_analyticsq(
    query='power_usage_CL | where TimeGenerated > startofday(now())'))
