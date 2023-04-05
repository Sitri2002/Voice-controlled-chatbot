import requests, winsound
def get_speech(text):
    response = requests.post("http://127.0.0.1:7860/run/generate", json={
	"data": [
		text, # prompt
		"\n", # line seperator delimeter
		"Angry", # emotion
		"", # custom emotion (use Custom on emotion)
		"Pippa",
		{"name":"audio.wav","data":"data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA="}, # microphone src
		0, # number of voice chunks (0 for autofit)
		1, # number of candidates
		1679386360, # voice seed
		16, # samples
		30, # iterations
		0.2, # temperature
		"DDIM", # diffusion sampler
		8, # pause size 
		0, # CVVP Weight
		0.8, # Top P
		1, # Diffusion Temp
		1, # Length Penalty
		2, # Repetition Penalty
		2, # Condition Free K value
		["Conditioning-Free"], # Half Precision and Cond Free
	]
    }).json()
    return response["data"]

def play_audio_from_api_response(api_response):
    item = api_response[0]
    audio_url = f'http://127.0.0.1:7860/file={item["name"]}'
    audio_content = requests.get(audio_url).content
    winsound.PlaySound(audio_content, winsound.SND_MEMORY)