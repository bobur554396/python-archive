import sys, os

import yaml
import speech_recognition as sr

def tts(message):
    '''
    this function takes a message as an argument and converts it to speech depending on the OS.
    :param message: message getting read
    :return: audio message
    '''
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + '"' + message + '"')
