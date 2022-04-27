from platform import node

from dbus import ValidationException
from rvrbase import rvrconfig_delegate
from .new_notification_api import My_new_notification_api
from rvrbase.constants import NOTIFY_APPLICATION_EVENT, VALID_MESSAGE_TYPES


class Mydelegate(rvrconfig_delegate.Rvrconfig):
    
    def __init__(self, path):
        super().__init__(path)

        self.notifcation_api = My_new_notification_api()

    def send_browser_notification(self, message, type):
        if type not in VALID_MESSAGE_TYPES:
            raise ValidationException(
                f'{type} is not in {VALID_MESSAGE_TYPES}.')

        self.notifcation_api.send_browser_notification(NOTIFY_APPLICATION_EVENT.format(type=type, node=node(), message=message))
        
