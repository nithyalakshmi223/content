FETCH_PASSWORD_CONTEXT = {
  "PAM360.Account(val.PASSWORD && val.PASSWORD == obj.PASSWORD)": {
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
}

CREATE_RESOURCE_CONTEXT = {
  "PAM360.Resource(val.message && val.message == obj.message)": {
   "operation":{
      "result":{
         "message":"Resource win-10 has been added successfully",
         "status":"Success"
      },
      "name":"CREATE RESOURCE"
   }
 }
}

CREATE_ACCOUNT_CONTEXT = {
  "PAM360.Account(val.message && val.message == obj.message)": {
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
 }
}

UPDATE_RESOURCE_CONTEXT = {
  "PAM360.Resource(val.message && val.message == obj.message)": {
   "operation":{
      "result":{
         "message":"Resource  modified successfully.",
         "status":"Success"
      },
      "name":"EDIT RESOURCE"
   }
 }
}

UPDATE_ACCOUNT_CONTEXT = {
  "PAM360.Account(val.message && val.message == obj.message)": {
   "operation":{
      "result":{
         "message":"Account temp modified successfully",
         "status":"Success"
      },
      "name":"EDIT ACCOUNT"
   }
 }
}

FETCH_ACCOUNT_DETAILS_CONTEXT = {
  "PAM360.Account(val.message && val.message == obj.message)": {
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
}

LIST_ALL_RESOURCE_CONTEXT = {
  "PAM360.Resource(val.message && val.message == obj.message)": {
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
}

LIST_ALL_ACCOUNTS_CONTEXT = {
  "PAM360.Account(val.message && val.message == obj.message)": {
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
}

UPDATE_ACCOUNT_PASSWORD_CONTEXT = {
  "PAM360.Account(val.message && val.message == obj.message)": {
   "operation":{
      "result":{
         "message":"Password changed successfully",
         "status":"Success"
      },
      "name":"CHANGE PASSWORD"
   }
 }
}

FETCH_RESOURCE_ACCOUNT_ID_CONTEXT = {
  "PAM360.Resource(val.message && val.message == obj.message)": {
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
}