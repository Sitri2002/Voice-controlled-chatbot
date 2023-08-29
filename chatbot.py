import os, openai, json, tiktoken, TortoiseTTS, voice_input, ElevenLabs, time, subprocess
from colorama import init as colorama_init, Fore, Style
from subprocess import  CREATE_NEW_CONSOLE 

colorama_init()
MODEL = "gpt-3.5-turbo"
USER = "Sitri"
AI = "Pippa"
TOKEN_LIMIT = 1000
API_PATH = "" #API JSON File path
PROMPTS_PATH = ""#JSON File to your system prompt

def generate_response(prompt):  
    OPENAI_API_KEY = json.load(open(API_PATH))["openai"]
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model= MODEL,
        messages=prompt,
        user=USER,
        max_tokens = 2048,
        temperature = 1,
        top_p = 0.7,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    text = response['choices'][0]['message']['content']
    return text

def num_tokens_from_messages(messages, model=MODEL):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == MODEL:  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.""")

def init():
    p = subprocess.Popen(os.path.abspath("mrq/ai-voice-cloning path"),stdin=subprocess.PIPE, cwd ="mrq/ai-voice-cloning path", creationflags=CREATE_NEW_CONSOLE)

def run(control = True, model : str = "Tortoise", voice : bool = True ):
    promptInp = json.load(open(PROMPTS_PATH))["Schizo_Pippa"]
    prompt = [{"role": "system", "content": promptInp}]
    if model == "Tortoise":
        init()
    while True:
        if (voice):
            user_inp = voice_input.record_audio(control)
        else: 
            user_inp = input("Sitri: ")

        if user_inp == "Restart.": prompt = [prompt[0]]

        if user_inp == None:
            pass
        else: 
            print(f"{Fore.GREEN}>{USER}:{user_inp}{Style.RESET_ALL}")
            prompt.append({"role": "user", "content": user_inp})

        if  prompt[-1]["role"] == "user":
            ai_output = generate_response(prompt)
            print(f"{Fore.CYAN}>{AI}: {ai_output}\n{Style.RESET_ALL}")
            prompt.append({"role": "assistant", "content" : ai_output})
            if model == "Tortoise":
                response = TortoiseTTS.get_speech(ai_output)
                TortoiseTTS.play_audio_from_api_response(response)
            if model == "Eleven":    
                ElevenLabs.get_speech(ai_output)
            time.sleep(5)

        if num_tokens_from_messages(prompt, MODEL) > TOKEN_LIMIT:
            prompt = [prompt[0]]
        

    
