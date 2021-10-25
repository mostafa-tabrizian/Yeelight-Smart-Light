#from yeelight import discover_bulbs
#print (discover_bulbs())

import time
from yeelight import Bulb as Lamp
import speech_recognition as sr

lamp = Lamp("192.168.1.2", effect="smooth", duration=100)

def on():
    lamp.turn_on()

def off():
    lamp.turn_off()

def brightness(amount):
    lamp.set_brightness(amount)

def power():
    lamp.toggle()

def powerWithVoice():
    #Fix def errors(type):
    #    errorTypes = {'claps': print('hello'), }
    #    errorTypes[type]
    def commands():
        command = mic.recognize_google(speech)
        print(command)
        if command == 'ali' or 'taylor':
            power()
        else:
            return '...this is not a command...'
    r = sr.Recognizer()
    mic = sr.Microphone()
    print('Lestining...')
    with mic as source:
        speech = r.listen(source)
        if not isinstance(speech, dict):
            power()
        

def ListenerLamp():
        powerWithVoice()

def countdown():
    second = int(input("Enter the time in seconds: "))
    while second: 
        mins, secs = divmod(second, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        second -= 1
    power()
    return ''


#print(power())
#print(brightness(10))
#print(powerWithVoice())
print(ListenerLamp())