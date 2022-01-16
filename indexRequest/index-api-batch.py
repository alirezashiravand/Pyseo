from oauth2client.service_account import ServiceAccountCredentials
import httplib2

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.

JSON_KEY_FILE = "./secret.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())  

with open('urllist.txt') as file:
   url_list=[line.rstrip() for line in file]

for index in url_list : 
  content="""{
  "url": "%s",
  "type": "URL_UPDATED"
  } 
  """%(index)
  response, content = http.request(ENDPOINT, method="POST", body=content)
  returned_response=response
  
  if returned_response.status==200:
    print(f"indexing requested successfull" + str(returned_response.date))
  else:
    print(f"there is a problem with request"+"    "+str(returned_response))
