
#### Learning methodology
    # understanding concepts
    # prototyping
    # integration in melissa

# Speech to text engines
    # pocketsphinx
    # ATT STT
    # Wit.ai STT
    # IBM STT
import os, sys

import speech_recognition as sr
import yaml
from brain import brain
from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables

name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print "Say Something!"
        audio = r.listen(source)

    try:
        key = '6MXA3KORTY67ZHD45TUFFXPWFLAETARY'
        speech_text = r.recognize_wit(audio, key=key).lower().replace("'", "")
        print "Melissa thinks you said '" + speech_text + "'"
    except sr.UnknownValueError:
        print "Melissa could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Wit Speech Recognition service; {0}".format(e)

    brain(name, speech_text)

main()