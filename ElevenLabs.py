from elevenlabslib import *
import json

API_PATH_2 = #put your API json file here, or just leave this blank and directly add API in user API call.
user  = ElevenLabsUser(json.load(open(API_PATH_2))["eleven"])
voice = user.get_voices_by_name("Pippa")[0]

def get_speech(prompt):
    voice.generate_and_play_audio(prompt, playInBackground=False)
