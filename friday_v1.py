import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
speech = sr.Recognizer


#greeting dict = {'hello':'hello', 'hi':'hi','sup':'sup'}
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('I am listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('network error')
    except sr.WaitTimeoutError:
        pass
    return voice_text

if __name__ == '__main__':
    #playsound('')

    while True:
        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('Hello sir. How can i help you?')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\{}  '.format(voice_note.replace('Open'), ''))
        elif 'bye' in voice_note:
            exit()