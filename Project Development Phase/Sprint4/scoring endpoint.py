

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "wLpq84jiqdQmAoNvQ9t0JafQQsECjik-mL4VIh51s4g8"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["IPAddress","LongURL","ShortURL","@Symbol","//Redirecting","PrefixSuffix","SubDomain","SSLfinal_state","DomainLength","Favicon","Port","HTTPStoken","RequestURL","AnchorURL","LinksInScriptTags","ServerFormHandler","InfoEmail","AbnormalURL","Redirect","Onmouseover","RightClick","PopupWindow","Iframe","AgeofDomain","DNSRecord","WebTraffic","PageRank","GoogleIndex","LinksPointingToPage","StatisticalReport"
]], "values": [[-1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,0,0,-1,1,-1,0,1,1,1,1,1,-1,1,-1,1,-1,-1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b82d7090-8831-4285-bede-9ac562e6d2e7/predictions?version=2022-11-21', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print(predictions)
pred=predictions['predictions'][0]['values'][0][0]
print(pred)
if(pred != -1):
   print("The Website is the Legitimate Website ... Continue!!")
else:
   print("The Website is not Legitimate... BEWARE!!")

