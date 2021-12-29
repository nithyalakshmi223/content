Use ManageEngine PAM360, a privileged access management solution to manage critical enterprise data such as privileged resources and accounts and secure credentials from Cortex XSOAR.

## Configure ManageEngine PAM360 on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for ManageEngine PAM360.
3. Click **Add instance** to create and configure a new integration instance.

| **Parameter** | **Description** | **Required** |
| --- | --- | --- |
| url | Server URL \(e.g., https://example.com\) | True |
| APP_TOKEN | Token to access PAM360 vault | True |
| insecure | Trust any certificate \(not secure\) | False |
| proxy | Use system proxy settings | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### pam360-fetch-password
***
Fetches account passwords.


#### Base Command

`pam360-fetch-password`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| account_id | ID of the account. | Required | 
| reason | Reason to fetch the password. | Optional | 
| ticket_id | Ticket ID when the ticketing system integration is enabled. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.Details.PASSWORD | String | Account password. |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-fetch-password resource_id=1 account_id=1 reason="Need the password to Login Windows Server" ticket_id=7```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Password fetched successfully",
         "status":"Success"
      },
      "Details":{
         "PASSWORD":"A1@8ZnQx)mh&="
      },
      "name":"GET PASSWORD"
   }
}
```
### pam360-create-resource
***
Creates a new resource.


#### Base Command

`pam360-create-resource`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_name | Name of the resource. | Required | 
| resource_type | Type of the resource. | Required | 
| resource_url | URL of the resource. | Optional | 
| domain_name | Domain name of the resource.| Optional |
| resourcegroup_name | Name of the resource group to which this resource belongs. | Optional |
| owner_name | Name of the resource owner. | Optional |
| location | Location of the resource. | Optional |
| dnsname | DNS Name or IP address. | Optional |
| department | The department to which the account belongs. | Optional | 
| resource_descritpion | Description of the resource. | Optional |
| notes | Additional notes about the resource.| Optional |
| account_name | Name of the account. | Required |
| password | Account password.| Required |
| resource_password_policy | Password policy for the resource. | Optional |
| account_password_policy | Password policy for the account. | Optional |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Resource.operation.result.status | String | Status of the operation. |
| PAM360.Resource.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-create-resource resource_name="pmp-win10" resource_type="Windows" resource_url="http://windowsserver/adminconsole" domain_name="pmp-win10" resourcegroup_name="Windows Servers" owner_name="admin" location="Level 10 - South Wing" dnsname="pmp-win10" department="NOC" resource_descritpion="Testing API" notes="Testing API" account_name="administrator" password="Test@123" resource_password_policy="Strong" account_password_policy="Strong"
```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Resource win-10 has been added successfully",
         "status":"Success"
      },
      "name":"CREATE RESOURCE"
   }
}
```
### pam360-create-account
***
Creates a new account under a specified resource.


#### Base Command

`pam360-create-account`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| account_name | Name of the account. | Required | 
| password | Account password. | Required | 
| notes | Account description. | Optional |
| account_password_policy | Password policy of the account.  | Optional |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-create-account resource_id=1 account_name="admin" password="Test@123" notes="Testing API" account_password_policy="Strong"```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Account(s) added successfully",
         "status":"Success"
      },
      "Details":[
         {
            "admin":{
               "STATUS":"Account added successfully"
            }
         }
      ],
      "name":"ADD ACCOUNTS"
   }
```
### pam360-update-resource
***
Updates the resource attributes.


#### Base Command

`pam360-update-resource`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| resource_name | Name of the resource. | Required | 
| resource_type | Type of the resource. | Optional | 
| resource_url | URL of the resource. | Optional |
| resource_description | Description of the resource. | Optional |
| resource_password_policy | Password policy of the resource. | Optional |
| location | Location of the resource. | Optional |
| dnsname | DNS name of the resource. | Optional |
| department | The department to which the account belongs. | Optional | 
| owner_name | Name of the resource owner. | Optional |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Resource.operation.result.status | String | Status of the operation. |
| PAM360.Resource.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-update-resource resource_id=1 resource_name="pmp-win10" resource_type="Windows" resource_url="http://windowsserver/adminconsole" resource_description="Testing API" resource_password_policy="Strong" location="Level 10 - South Wing" department="NOC" dnsname="pmp-win10" owner_name="admin"```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Resource  modified successfully.",
         "status":"Success"
      },
      "name":"EDIT RESOURCE"
   }
}
```
### pam360-update-account
***
Updates the account attributes.


#### Base Command

`pam360-update-account`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| account_id | ID of the account. | Required | 
| account_name | Name of the account. | Optional | 
| owner_name | Name of the owner. | Optional |
| notes | Additional notes about the account. | Optional |
| account_password_policy | Password policy of the account. | Optional |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-update-account resource_id=1 account_id=1 account_name="admin" owner_name="admin" notes="Testing API" account_password_policy="Strong"```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Account temp modified successfully",
         "status":"Success"
      },
      "name":"EDIT ACCOUNT"
   }
}
```
### pam360-fetch-account-details
***
Fetches the details of the account.


#### Base Command

`pam360-fetch-account-details`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| account_id | ID of the account. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status.|
| PAM360.Account.operation.Details.DESCRIPTION | String | Description of the account. |
| PAM360.Account.operation.Details.PASSWDID | String | ID that is used to perform password-related operations. |
| PAM360.Account.operation.Details.LAST MODIFIED TIME | String | The time at which the account was last modified. |
| PAM360.Account.operation.Details.EXPIRY STATUS | String | Expiry status of the account password. |
| PAM360.Account.operation.Details.COMPLIANT REASON | String | Reason for the password not being compliant with the password policy. |
| PAM360.Account.operation.Details.PASSWORD STATUS | String | The availability status of the password. |
| PAM360.Account.operation.Details.PASSWORD POLICY | String | The password policy of the account. |
| PAM360.Account.operation.Details.COMPLIANT STATUS | String | Status of whether the account password is compliant with the set password policy. |
| PAM360.Account.operation.Details.LAST ACCESSED TIME | String | The time at which the account was last accessed. |


#### Command Example
```!pam360-fetch-account-details resource_id=1 account_id=1```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Account details fetched successfully",
         "status":"Success"
      },
      "Details":{
         "DESCRIPTION":"N/A",
         "PASSWDID":"1",
         "LAST MODIFIED TIME":"N/A",
         "EXPIRY STATUS":"Valid",
         "COMPLIANT REASON":"-",
         "PASSWORD STATUS":"****",
         "PASSWORD POLICY":"Strong",
         "COMPLIANT STATUS":"Compliant",
         "LAST ACCESSED TIME":"Dec 1, 2021 09:00 PM"
      },
      "name":"GET RESOURCE ACCOUNT DETAILS"
   }
}
```
### pam360-list-all-resources
***
Lists all owned and shared resources.


#### Base Command

`pam360-list-all-resources`


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Resource.operation.result.status | String | Status of the operation. |
| PAM360.Resource.operation.result.message | String | Command execution status. |
| PAM360.Resource.operation.Details.RESOURCE DESCRIPTION | String | Description of the resource. |
| PAM360.Resource.operation.Details.RESOURCE TYPE | String | Type of the resource. |
| PAM360.Resource.operation.Details.RESOURCE ID | String | ID of the resource. |
| PAM360.Resource.operation.Details.RESOURCE NAME | String | Name of the resource. |
| PAM360.Resource.operation.Details.NOOFACCOUNTS | String | The number of accounts associated with the resource. |


#### Command Example
```!pam360-list-all-resources```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Resources fetched successfully",
         "status":"Success"
      },
      "Details":[
         {
            "RESOURCE DESCRIPTION":"",
            "RESOURCE TYPE":"Fortigate Firewall",
            "RESOURCE ID":"1",
            "RESOURCE NAME":"temp",
            "NOOFACCOUNTS":"1"
         }
      ],
      "name":"GET RESOURCES",
      "totalRows":1
   }
}
```
### pam360-list-all-accounts
***
Lists all accounts belonging to the resource.


#### Base Command

`pam360-list-all-accounts`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status. |
| PAM360.Account.operation.Details.LOCATION | String | Location of the account. |
| PAM360.Account.operation.Details.RESOURCE DESCRIPTION | String | Description of the resource. |
| PAM360.Account.operation.Details.RESOURCE TYPE | String | The resource type assigned to the account. |
| PAM360.Account.operation.Details.RESOURCE ID | String | ID of the resource. |
| PAM360.Account.operation.Details.DEPARTMENT | String | The department to which the account belongs. |
| PAM360.Account.operation.Details.RESOURCE OWNER | String | Name of the resource owner. |
| PAM360.Account.operation.Details.RESOURCE PASSWORD POLICY | String | The password policy of the resource to which the account belongs. |
| PAM360.Account.operation.Details.RESOURCE URL | String | URL of the resource. |
| PAM360.Account.operation.Details.DOMAIN NAME | String | The domain name of the resource. |
| PAM360.Account.operation.Details.RESOURCE NAME | String | The name of the resource to which the account belongs. |
| PAM360.Account.operation.Details.DNS NAME | String | DNS name of the resource. |
| PAM360.Account.operation.Details.ACCOUNT LIST.ACCOUNT ID | String | ID of the account. |
| PAM360.Account.operation.Details.ACCOUNT LIST.ACCOUNT NAME | String | The name of the account. |
| PAM360.Account.operation.Details.ACCOUNT LIST.PASSWORD STATUS | String | The availability status of the account password. |
| PAM360.Account.operation.Details.ACCOUNT LIST.ACCOUNT PASSWORD POLICY | String | The password policy assigned to the account. |
| PAM360.Account.operation.Details.ACCOUNT LIST.PASSWDID | String | ID needed for password-based operations. |
| PAM360.Account.operation.Details.ACCOUNT LIST.ISREASONREQUIRED | String | Reason to access the password. |


#### Command Example
```!pam360-list-all-accounts resource_id=1```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Resource details with account list fetched successfully",
         "status":"Success"
      },
      "Details":{
         "LOCATION":"",
         "RESOURCE DESCRIPTION":"",
         "RESOURCE TYPE":"Fortigate Firewall",
         "RESOURCE ID":"1",
         "ACCOUNT LIST":[
            {
               "ISFAVPASS":"false",
               "ACCOUNT ID":"1",
               "AUTOLOGONLIST":[
                  "SSH",
                  "Telnet"
               ],
               "ACCOUNT NAME":"temp",
               "PASSWORD STATUS":"****",
               "ISREMOTEAPPONLY":"false",
               "ACCOUNT PASSWORD POLICY":"Strong",
               "AUTOLOGONSTATUS":"One of the resources or landing servers is configured to be connected repeatedly. Check your landing server configuration or contact your administrator.",
               "IS_TICKETID_REQD_ACW":"false",
               "PASSWDID":"1",
               "IS_TICKETID_REQD_MANDATORY":"false",
               "IS_TICKETID_REQD":"false",
               "ISREASONREQUIRED":"false"
            }
         ],
         "DEPARTMENT":"",
         "RESOURCE OWNER":"admin",
         "RESOURCE PASSWORD POLICY":"Strong",
         "RESOURCE URL":"https://pam360:8282",
         "NEWSSHTERMINAL":"false",
         "DOMAIN NAME":"",
         "ALLOWOPENURLINBROWSER":"true",
         "RESOURCE NAME":"temp",
         "DNS NAME":""
      },
      "name":"GET RESOURCE ACCOUNTLIST"
   }
}
```
### pam360-update-account-password
***
Updates the account password.


#### Base Command

`pam360-update-account-password`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required |
| account_id | ID of the account. | Required |
| new_password | Password to be updated. | Required |
| reset_type | The type of password reset to be done - LOCAL or REMOTE. | Required |
| reason | Reason to update the password. | Optional |
| ticket_id | Ticket ID when the ticketing system integration is enabled.| Optional |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status. |


#### Command Example
```!pam360-update-account-password resource_id=1 account_id=1 new_password="win@10" reset_type="local" reason="Password Expired" ticket_id=7```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Password changed successfully",
         "status":"Success"
      },
      "name":"CHANGE PASSWORD"
   }
}
```
### pam360-fetch-resource-account-id
***
Fetches the IDs of the resources and accounts.


#### Base Command

`pam360-fetch-resource-account-id`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_name | Name of the resource. | Required |
| account_name | Name of the account. | Required |


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.result.status | String | Status of the operation. |
| PAM360.Account.operation.result.message | String | Command execution status.|
| PAM360.Account.operation.Details.RESOURCEID | String | ID of the resource. |
| PAM360.Account.operation.Details.ACCOUNTID | String | ID of the account. |


#### Command Example
```!pam360-fetch-resource-account-id resource_name=1 account_name=1```

#### Context Example
```
{
   "operation":{
      "result":{
         "message":"Resource ID and account ID fetched successfully for the given resource name and account name.",
         "status":"Success"
      },
      "Details":{
         "ACCOUNTID":"1",
         "RESOURCEID":"1"
      },
      "name":"GET_RESOURCEACCOUNTID"
   }
}
```