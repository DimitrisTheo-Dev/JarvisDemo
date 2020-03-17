import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()
try:
    engine = pyttsx3.init()
except ImportError:
    print('Not Found')
except RuntimeError:
    print('fail')


voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
engine.setProperty('voice','com.apple.speech.synthesis.voice.Alex')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('I am listening...')
    with sr.Microphone() as source:
       audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('network error')
    return voice_text

if __name__ == '__main__':

    speak_text_cmd('Hello mister Jim this is Jarvis. I am you artificial assistant')

    while True:
        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('Hello sir. How can i help you?')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\{}  ' .format(voice_note.replace('Open'), ''))
        elif 'bye' in voice_note:
            speak_text_cmd('Bye')
            exit()



