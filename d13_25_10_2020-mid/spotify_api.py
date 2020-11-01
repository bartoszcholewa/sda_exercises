import requests
import base64
import json
from secrets import *

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}
clientId = 'c28c1e00158a48d595d5e0fb8c3d729f'
clientSecret = '67e3b6aec9f84d0e8f5470c263ea63f8'

# Encode as Base64
message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint

playlistId = "37i9dQZF1Ejj8aykI3TXsR"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(res.json(), indent=2))