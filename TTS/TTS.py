from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '48RwzFT4WKK5TVa67HCDHqq-TLkMcqTmqVaIkD1vYGlu'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/94322130-6fe2-45b2-bae7-d8456059379d'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('smartmethod.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)
with open('./smartmethodOUTPUT.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)  