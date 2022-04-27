import logging
from platform import node
import json
import sys
from dbus import ValidationException

from rvrbase import rvrconfig_delegate
from .__about__ import __version__ as version
from .notification_api import New_notification_api
from .azure_logger_api import Azure_logger_api
from rvrbase.constants import LOG_TYPE_APPLICATION_EVENT, NOTIFY_APPLICATION_EVENT,\
    VALID_MESSAGE_TYPES

# todo put it all in try / except


class Rvrbase(rvrconfig_delegate.Rvrconfig):

    def __init__(self, path):
        super().__init__(path)

        self.notifcation_api = New_notification_api()
        self.azure_logger_api = Azure_logger_api()
        self.workspace_id = self.q1('workspace_id')
        self.workspace_prim_key = self.q1('primary_key')

        # todo to constant.
        message = f'Starting, notify URL: {self.notifcation_api.notify.endpoint}'
        self.send_az_app_event(type='info', message=message)

    def send_browser_notification(self, message, type):
        if type not in VALID_MESSAGE_TYPES:
            raise ValidationException(
                f'{type} is not in {VALID_MESSAGE_TYPES}.')

        self.notifcation_api.send_browser_notification(
            NOTIFY_APPLICATION_EVENT.format(type=type, node=node(), message=message))

    def log_app_event(self, type, message, notify_message=False):
        if type not in VALID_MESSAGE_TYPES:
            raise ValidationException(
                f'{type} is not in {VALID_MESSAGE_TYPES}.')  # todo use constants.

        if type == 'debug':
            logging.debug(message)
        elif type == 'info':
            logging.info(message)
        elif type == 'warning':
            logging.warning(message)
        elif type == 'error':
            logging.error(message)

        self.send_az_app_event(type, message)

        if notify_message:
            self.notifcation_api.send_browser_notification(message=message)

    def send_az_app_event(self, type, message):
        if type not in VALID_MESSAGE_TYPES:
            raise ValidationException(
                f'{type} is not in {VALID_MESSAGE_TYPES}.')  # todo use constants.

        body = {
            "hostname": node(),
            "script_path": sys.argv[0],
            "arguments": sys.argv[1:],
            "type": type,
            "message": message,
            "rvrbase_version": version
        }

        body_json = json.dumps(body)

        self.azure_logger_api.post_data(
            body_json, LOG_TYPE_APPLICATION_EVENT, self.workspace_id, self.workspace_prim_key)

    def send_az_metric(self, log_type, metric_name, value):
        body = {
            "hostname": node(),
            "script_path": sys.argv[0],
            "metric_name": metric_name,
            "value": value,
            "rvrbase_version": version
        }

        body_json = json.dumps(body)
        self.azure_logger_api.post_data(
            body_json, log_type, self.workspace_id, self.workspace_prim_key)
