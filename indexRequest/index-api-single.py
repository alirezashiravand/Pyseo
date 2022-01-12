from oauth2client.service_account import ServiceAccountCredentials
import httplib2

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.

JSON_KEY_FILE = "./secret.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())

content = """{
  "url": "url",
  "type": "URL_UPDATED"
}"""


response, content = http.request(ENDPOINT, method="POST", body=content)
print(response)
print(content)

returned_response=response


# print(response.status)
# request_date=response.date
if returned_response.status==200:
  print(f"indexing requested successfull")
else:
  print(f"there is a problem with request")
