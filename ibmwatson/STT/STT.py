from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'iFPJKpf_2B3b0W01zbq4Iwh6j4LA5fbr49h6lfTGM3tn'
url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/a93525f1-8b12-484f-9752-d661f88d188b'

# Setup Service
authenticator = IAMAuthenticator(apikey) 
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)


# Perform conversion
with open('wel.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

res 

text = res['results'][0]['alternatives'][0]['transcript']
text

confidence = res['results'][0]['alternatives'][0]['confidence']
confidence

with open('output.txt', 'w') as out:
    out.writelines(text) 
