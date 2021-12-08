Use the ManageEngine PAM360 to manage passwords, resources and accounts from Cortex XSOAR.

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
Fetch password from PAM360 vault.


#### Base Command

`pam360-fetch-password`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| resource_id | ID of the resource. | Required | 
| account_id | ID of the account | Required | 
| reason | Reason to fetch password | Optional | 
| ticket_id | To fetch ticket ID when the ticketing system integration is enabled. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| PAM360.Account.operation.Details.PASSWORD | String | Password of the account stored in PAM360 |
| PAM360.Account.operation.result.status | String | Status of the API call |
| PAM360.Account.operation.result.message | String | Message of the API call |


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
