from elevenlabslib import *
import json

API_PATH_2 = "C:/Users/nguye/Desktop/Repository/Pippa/doc/API_key.json"
user  = ElevenLabsUser(json.load(open(API_PATH_2))["eleven"])
voice = user.get_voices_by_name("Pippa")[0]

def get_speech(prompt):
    voice.generate_and_play_audio(prompt, playInBackground=False)
