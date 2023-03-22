import requests  #pip install requests to solve
import json

# Set up variables for authentication
username = 'your_salesforce_username'
password = 'your_salesforce_password'
security_token = 'your_salesforce_security_token'
consumer_key = 'your_salesforce_consumer_key'
consumer_secret = 'your_salesforce_consumer_secret'

# Set up authentication endpoint
auth_url = 'https://login.salesforce.com/services/oauth2/token'

# Set up payload for authentication request
payload = {
    'grant_type': 'password',
    'client_id': consumer_key,
    'client_secret': consumer_secret,
    'username': username,
    'password': password + security_token
}

# Send authentication request
auth_response = requests.post(auth_url, data=payload)
auth_data = json.loads(auth_response.text)

# Get access token from authentication response
access_token = auth_data['access_token']

# Set up SOQL query
query = 'SELECT Id, Name, AccountNumber FROM Account LIMIT 10'

# Set up endpoint for SOQL query
query_url = 'https://your_salesforce_instance.salesforce.com/services/data/v49.0/query'

# Set up headers for SOQL query
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Send SOQL query request
query_response = requests.get(query_url, headers=headers, params={'q': query})
query_data = json.loads(query_response.text)

# Print query results
for record in query_data['records']:
    print('Id:', record['Id'])
    print('Name:', record['Name'])
    print('Account Number:', record['AccountNumber'])
    print('------------------------------')


'''
In this example, you will need to replace the placeholders for 
the authentication variables (username, password, security_token, 
consumer_key, and consumer_secret) with your own Salesforce authentication 
information. You will also need to replace the placeholder for your_salesforce_instance
 with your own Salesforce instance URL.

Once you've made these replacements, you can run the script to extract data from 
Salesforce. This script uses the Salesforce REST API to authenticate the user and 
execute a SOQL query to extract data from the Account object. The results are then 
printed to the console. You can modify the SOQL query to extract data from other 
objects in Salesforce as needed.
'''