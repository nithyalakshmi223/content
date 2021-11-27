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