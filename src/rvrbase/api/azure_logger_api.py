# from https://medium.com/slalom-build/reading-and-writing-to-azure-log-analytics-c78461056862
import requests
import hashlib
import hmac
import base64
import logging
import datetime
from rvrbase.constants import ERR_POST_DATA, MSG_POST_DATA_SUCCESS


class Azure_logger_api():
    def _build_signature(self, customer_id, shared_key, date, content_length, method, content_type,
                         resource):
        # Returns authorization header which will be used when sending data into Azure Log
        # Analytics

        x_headers = 'x-ms-date:' + date
        string_to_hash = method + "\n" + \
            str(content_length) + "\n" + content_type + \
            "\n" + x_headers + "\n" + resource
        bytes_to_hash = bytes(string_to_hash, 'UTF-8')
        decoded_key = base64.b64decode(shared_key)
        encoded_hash = base64.b64encode(hmac.new(
            decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode('utf-8')
        authorization = "SharedKey {}:{}".format(customer_id, encoded_hash)
        return authorization

    def post_data(self, body, log_type, workspace_id, workspace_prim_key):
        """Sends payload to Azure Log Analytics Workspace

        Keyword arguments:
        customer_id -- Workspace ID obtained from Advanced Settings
        shared_key -- Authorization header, created using build_signature
        body -- payload to send to Azure Log Analytics
        log_type -- Azure Log Analytics table name
        """

        method = 'POST'
        content_type = 'application/json'
        resource = '/api/logs'
        rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        content_length = len(body)
        signature = self._build_signature(
            workspace_id, workspace_prim_key, rfc1123date, content_length, method, content_type,
            resource)

        uri = 'https://' + workspace_id + '.ods.opinsights.azure.com' + \
            resource + '?api-version=2016-04-01'

        headers = {
            'content-type': content_type,
            'Authorization': signature,
            'Log-Type': log_type,
            'x-ms-date': rfc1123date
        }

        response = requests.post(uri, data=body, headers=headers)
        if (response.status_code >= 200 and response.status_code <= 299):
            logging.info(MSG_POST_DATA_SUCCESS.format(body=body))
        else:
            raise RuntimeError(ERR_POST_DATA.format(
                status_code=response.status_code))
