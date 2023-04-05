import speech_recognition as sp
from colorama import init as colorama_init, Fore, Style

colorama_init()
r = sp.Recognizer()
hotword = ["Hey", "hey", "Restart"]
r.pause_threshold = 2
def record_audio(control):
    with sp.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(f"{Fore.RED}Listening...")
        audio = r.listen(source)
        print(f"Finished listening.{Style.RESET_ALL}")
        transcribe =  r.recognize_whisper(audio, language= "english", model= "small")
        if any(word in transcribe for word in hotword):
            return transcribe 
        else:
            if control: return None
            else: return transcribe
        
