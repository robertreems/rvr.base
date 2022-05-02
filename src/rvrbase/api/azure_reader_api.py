# This class is heavily inspired by
# https://medium.com/slalom-build/reading-and-writing-to-azure-log-analytics-c78461056862

import requests
import urllib3
import json

from rvrbase.constants import ERR_GETTING_AZURE_DATA, ERR_GETTING_TOKEN


class Azure_reader_api:
    def __init__(self, tenant, sp_id, sp_secret, az_workspace_id):
        # tenant = #'83ebf573-f6a0-4a5a-a14e-323ba97ec356'
        # self.sp_id = '274cef59-fa12-4b39-92f7-4081ae279424' # Application (client) ID
        # self.sp_secret = '3p78Q~pLBhy.qHQxKfvJEb-xoq_ATnqQwBIdobA.' # The service principal secret
        # self.az_workspace_id = '7756814b-7720-4b6d-9fb6-0aa03fe97658'
        # self.query = "app_event_CL  | where type_s  contains 'error' or type_s contains 'warning'"
        self.sp_token = self.__get_token(
            tenant=tenant, sp_id=sp_id, sp_secret=sp_secret)
        # self.data = get_data(query=query,token=sp_token, az_workspace_id=
        # az_workspace_id) # todo move

        self.az_workspace_id = az_workspace_id

    def __get_token(self, tenant, sp_id, sp_secret):
        """Obtain authentication token using a Service Principal"""
        login_url = "https://login.microsoftonline.com/" + tenant + "/oauth2/token"
        resource = "https://api.loganalytics.io"

        payload = {
            'grant_type': 'client_credentials',
            'client_id': sp_id,
            'client_secret': sp_secret,
            'Content-Type': 'x-www-form-urlencoded',
            'resource': resource
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.post(login_url, data=payload, verify=False)

        if (response.status_code >= 200 and response.status_code <= 299):
            token = json.loads(response.content)["access_token"]
            return {"Authorization": str("Bearer " + token), 'Content-Type': 'application/json'}
        else:
            raise RuntimeError(ERR_GETTING_TOKEN.format(
                status_code=response.status_code))

    def get_data(self, query):
        """Executes a KQL on a Azure Log Analytics Workspace

        Keyword arguments:
        query -- Kusto query to execute on Azure Log Analytics
        token -- Authentication token generated using get_token
        az_workspace_id -- Workspace ID obtained from Advanced Settings
        """

        az_url = "https://api.loganalytics.io/v1/workspaces/" + \
            self.az_workspace_id + "/query"
        query = {"query": query}

        response = requests.get(az_url, params=query, headers=self.sp_token)

        if (response.status_code >= 200 and response.status_code <= 299):
            return json.loads(response.content)
        else:
            raise RuntimeError(ERR_GETTING_AZURE_DATA.format(
                status_code=response.status_code))
