from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from time import ctime
import time
import pyttsx3
import webbrowser
import datetime
def talkToMe(audio):
    #"speaks audio passed as argument"
 engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
	#print(audio)
    #for line in audio.splitlines():
    #engine.say(audio)
    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')
def myCommand():
    "listens for commands"
 r = sr.Recognizer()  #r object
with sr.Microphone() as source:
        print('I am ready for your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  #beshi noisy room e thakle noise jate na catch kore
 audio = r.listen(source)
try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
#loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();
 return command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talkToMe("Good Morning!")
elif hour>=12 and hour<18:
        talkToMe("Good Afternoon!")   
 else:
        talkToMe("Good Evening!")  
talkToMe("I am Jarvis mam. Please tell me how may I help you")
def assistant(command):
    "if statements for executing commands"
    if 'open website' in command:
        reg_ex = re.search('open website (.*)', command)
        url = 'https://www.iiuc.ac.bd/'
        #if reg_ex:
            #subreddit = reg_ex.group(1)
            #url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
	if 'how are you' in command:
        talkToMe('I am fine thank you')
 if 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')
	elif 'nancy' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()
if 'nab' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)  
 #identify to server
            mail.ehlo()
 #encrypt session
            mail.starttls()
 #login
            mail.login('Nabeela56 Quader', 'nabu01')
 #send message
            mail.sendmail('Kangna56nab', 'Kangna56nab@gmail.com', content)
 #end mail connection
            mail.close()
talkToMe('Email sent.')
 else:
            talkToMe('I don\'t know what you mean!')
            if 'play music' in command:
            music_dir = 'H:\\My Documents\\fv music'
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[0]))
			if 'what time is it' in command:
	    print(time.ctime())
	    talkToMe(ctime())	
    if 'open google' in command:
        webbrowser.open("google.com")
        print('Done!')	
   #talkToMe('I am ready for your command')
wishMe()
#loop to continue executing multiple commands
while True:
    assistant(myCommand())
