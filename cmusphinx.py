import speech_recognition as sr

recognizer = sr.Recognizer()

def transcript (audio_file_path) :
    #result = ""
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    
    try:
        return recognizer.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

