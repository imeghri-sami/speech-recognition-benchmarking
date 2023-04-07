import os
import speech_recognition as sr


WIT_AI_TOKEN = os.environ.get("WIT_AI_TOKEN") 

recognizer = sr.Recognizer()

def transcript (audio_file_path) :
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    
    try:
        return recognizer.recognize_wit(audio, key=WIT_AI_TOKEN)
    except sr.UnknownValueError:
        print("witai could not understand audio")
    except sr.RequestError as e:
        print("witai error; {0}".format(e))
