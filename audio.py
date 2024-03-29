import requests
import json


def read_audio(WAVE_FILENAME):
    # function to read audio(wav) file
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio


API_ENDPOINT = 'https://api.wit.ai/speech'
ACCESS_TOKEN = 'BXISKARHN2PWZ3FUXSDU3BJ7JG6ZOZVV'

# get a sample of the audio that we recorded before.
audio = read_audio("001.wav")

# defining headers for HTTP request
headers = {'authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-Type': 'audio/mpeg3'}

# Send the request as post request and the audio as data
resp = requests.post(API_ENDPOINT, headers=headers,
                     data=audio)

# Get the text
data = json.loads(resp.content)
print(data)