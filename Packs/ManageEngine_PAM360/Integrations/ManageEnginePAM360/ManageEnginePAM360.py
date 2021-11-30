import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *
import urllib3
urllib3.disable_warnings()


class Client(BaseClient):
    def __init__(self, server_url: str, use_ssl: bool, proxy: bool, app_token=str):
        super().__init__(base_url=server_url, verify=use_ssl, proxy=proxy)
        self._app_token = app_token

    def fetch_password(self, method, resid, accid):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resid}/accounts/{accid}/password'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers)

    def create_resource(self, method, resource_name, account_name, resource_type, resource_url, password, notes, resource_password_policy, account_password_policy):
        URL_SUFFIX = '/restapi/json/v1/resources'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        query = {
            "operation": {
                "Details": {
                    "RESOURCENAME": resource_name,
                    "ACCOUNTNAME": account_name,
                    "RESOURCETYPE": resource_type,
                    "PASSWORD": password,
                    "NOTES": notes,
                    "RESOURCEURL": resource_url,
                    "RESOURCEPASSWORDPOLICY": resource_password_policy,
                    "ACCOUNTPASSWORDPOLICY": account_password_policy
                }
            }
        }
        params = {
            'INPUT_DATA': f'{query}'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers, data=params)

    def create_account(self, method, resource_id, account_name, password, notes, account_password_policy):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}/accounts'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        query = {
            "operation": {
                "Details": {
                    "ACCOUNTNAME": account_name,
                    "PASSWORD": password,
                    "NOTES": notes,
                    "ACCOUNTPASSWORDPOLICY": account_password_policy
                }
            }
        }
        params = {
            'INPUT_DATA': f'{query}'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers, data=params)

    def update_resource(self, method, resource_id, resource_name, resource_type, resource_url, password, resource_description, resource_password_policy, location, department):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        query = {
            "operation": {
                "Details": {
                    "RESOURCENAME": resource_name,
                    "RESOURCETYPE": resource_type,
                    "PASSWORD": password,
                    "RESOURCEDESCRIPTION": resource_description,
                    "RESOURCEURL": resource_url,
                    "RESOURCEPASSWORDPOLICY": resource_password_policy,
                    "LOCATION": location,
                    "DEPARTMENT": department
                }
            }
        }
        params = {
            'INPUT_DATA': f'{query}'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers, data=params)

    def update_account(self, method, resource_id, account_id, account_name, notes, account_password_policy):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}/accounts/{account_id}'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        query = {
            "operation": {
                "Details": {
                    "ACCOUNTNAME": account_name,
                    "NOTES": notes,
                    "ACCOUNTPASSWORDPOLICY": account_password_policy
                }
            }
        }
        params = {
            'INPUT_DATA': f'{query}'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers, data=params)

    def fetch_account_details(self, method, resource_id, account_id):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}/accounts/{account_id}'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers)

    def fetch_resources(self, method):
        URL_SUFFIX = '/restapi/json/v1/resources'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers)

    def fetch_accounts(self, method, resource_id):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}/accounts'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers)

    def update_account_password(self, method, resource_id, account_id, new_password, reset_type, reason, ticket_id):
        URL_SUFFIX = f'/restapi/json/v1/resources/{resource_id}/accounts/{account_id}'
        headers = {
            'APP_AUTHTOKEN': self._app_token,
            'APP_TYPE': '17'
        }
        query = {
            "operation": {
                "Details": {
                    "NEWPASSWORD": new_password,
                    "RESETTYPE": reset_type,
                    "REASON": reason,
                    "TICKETID": ticket_id
                }
            }
        }
        params = {
            'INPUT_DATA': f'{query}'
        }
        return self._http_request(method, URL_SUFFIX, headers=headers, data=params)


def pam360_fetch_password(client, **args):
    resid = args.get("resource_id")
    accid = args.get("account_id")
    creds_list = client.fetch_password("GET", resid, accid)
    password = creds_list.get('operation').get('Details').get('PASSWORD')
    readable_output = f'{password}'
    results = CommandResults(
        outputs=creds_list,
        raw_response=creds_list,
        outputs_prefix='PAM360.Account',
        outputs_key_field='PASSWORD',
        readable_output=readable_output,
    )
    return results


def pam360_create_resource(client, **args):
    resource_name = args.get("resource_name")
    account_name = args.get("account_name")
    resource_type = args.get("resource_type")
    resource_url = args.get("resource_url")
    password = args.get("password")
    notes = args.get("notes")
    resource_password_policy = args.get("resource_password_policy")
    account_password_policy = args.get("account_password_policy")
    create_resource = client.create_resource("POST", resource_name, account_name, resource_type, resource_url, password, notes, resource_password_policy, account_password_policy)
    readable_output = f'{create_resource}'
    results = CommandResults(
        outputs=create_resource,
        raw_response=create_resource,
        outputs_prefix='PAM360.Resource',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_create_account(client, **args):
    resource_id = args.get("resource_id")
    account_name = args.get("account_name")
    password = args.get("password")
    notes = args.get("notes")
    account_password_policy = args.get("account_password_policy")
    create_account = client.create_account("POST", resource_id, account_name, password, notes, account_password_policy)
    readable_output = f'{create_account}'
    results = CommandResults(
        outputs=create_account,
        raw_response=create_account,
        outputs_prefix='PAM360.Account',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_update_resource(client, **args):
    resource_id = args.get("resource_id")
    resource_name = args.get("resource_name")
    resource_type = args.get("resource_type")
    resource_url = args.get("resource_url")
    password = args.get("password")
    resource_description = args.get("resource_description")
    resource_password_policy = args.get("resource_password_policy")
    location = args.get("location")
    department = args.get("department")
    update_resource = client.update_resource("PUT", resource_id, resource_name, resource_type, resource_url, password, resource_description, resource_password_policy, location, department)
    readable_output = f'{update_resource}'
    results = CommandResults(
        outputs=update_resource,
        raw_response=update_resource,
        outputs_prefix='PAM360.Resource',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_update_account(client, **args):
    resource_id = args.get("resource_id")
    account_id = args.get("account_id")
    account_name = args.get("account_name")
    notes = args.get("notes")
    account_password_policy = args.get("account_password_policy")
    update_account = client.update_account("PUT", resource_id, account_id, account_name, notes, account_password_policy)
    readable_output = f'{update_account}'
    results = CommandResults(
        outputs=update_account,
        raw_response=update_account,
        outputs_prefix='PAM360.Account',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_fetch_account_details(client, **args):
    resource_id = args.get("resource_id")
    account_id = args.get("account_id")
    account_details = client.fetch_account_details("GET", resource_id, account_id)
    readable_output = f'{account_details}'
    results = CommandResults(
        outputs=account_details,
        raw_response=account_details,
        outputs_prefix='PAM360.Account',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_list_resources(client, **args):
    resource_list = client.fetch_resources("GET")
    readable_output = f'{resource_list}'
    results = CommandResults(
        outputs=resource_list,
        raw_response=resource_list,
        outputs_prefix='PAM360.Resource',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_list_accounts(client, **args):
    resource_id = args.get("resource_id")
    account_list = client.fetch_accounts("GET", resource_id)
    readable_output = f'{account_list}'
    results = CommandResults(
        outputs=account_list,
        raw_response=account_list,
        outputs_prefix='PAM360.Account',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def pam360_update_account_password(client, **args):
    resource_id = args.get("resource_id")
    account_id = args.get("account_id")
    new_password = args.get("new_password")
    reset_type = args.get("reset_type")
    reason = args.get("reason")
    ticket_id = args.get("ticket_id")
    update_password = client.update_account_password("PUT", resource_id, account_id, new_password, reset_type, reason, ticket_id)
    readable_output = f'{update_password}'
    results = CommandResults(
        outputs=update_password,
        raw_response=update_password,
        outputs_prefix='PAM360.Account',
        outputs_key_field='message',
        readable_output=readable_output,
    )
    return results


def main():

    params = demisto.params()
    url = params.get('URL')
    app_token = params.get('APP_TOKEN')
    use_ssl = not params.get('insecure', False)
    proxy = params.get('proxy', False)
    try:
        client = Client(server_url=url, use_ssl=use_ssl, proxy=proxy, app_token=app_token)
        command = demisto.command()
        demisto.debug(f'Command being called in ManageEngine PAM360 is: {command}')
        commands = {
            'pam360-fetch-password': pam360_fetch_password,
            'pam360-create-resource': pam360_create_resource,
            'pam360-create-account': pam360_create_account,
            'pam360-update-resource': pam360_update_resource,
            'pam360-update-account': pam360_update_account,
            'pam360-fetch-account-details': pam360_fetch_account_details,
            'pam360-list-all-resources': pam360_list_resources,
            'pam360-list-all-accounts': pam360_list_accounts,
            'pam360-update-account-password': pam360_update_account_password,
        }
        if command in commands:
            return_results(commands[command](client, **demisto.args()))

        else:
            raise NotImplementedError(f'{command} is not an existing PAM360 command')
    except Exception as err:
        return_error(f'Unexpected error: {str(err)}', error=traceback.format_exc())


if __name__ in ['__main__', 'builtin', 'builtins']:
    main()
