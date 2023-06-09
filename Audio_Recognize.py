import pyttsx3
import speech_recognition as sr
import nltk

spEng = pyttsx3.init()
spEng.setProperty('rate',150)

spEng.say('Hi')
#print(spEng.getProperty('rate'))

recognizer = sr.Recognizer()

with sr.Microphone() as mic:
    #recognizer.adjust_for_ambient_noise(mic)
    print('Say:', end=' ')
    audio = recognizer.listen(mic, timeout = 1, phrase_time_limit = 2)
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        spEng.say(text)
        spEng.runAndWait()
    except Exception as err:
        print('\nCould not recognise')