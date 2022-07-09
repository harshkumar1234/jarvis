# (module) speech_recognition and alias sr
from http import server
from imghdr import what
from unicodedata import category
import speech_recognition as sr
# module text to speech
import pyttsx3
# module webbrowser
import webbrowser
# module data and time
import datetime
import pyjokes
import smtplib
from twilio.rest import Client
from urllib.request import urlopen



# first function create 
def sptext():  
#Recognizer() is class attribute of sr
 recognizer=sr.Recognizer() 
 #Microphone() is class attribute of sr and source is variable
 with sr.Microphone() as source:
     print("listening .....")
     #Adjusts the energy threshold dynamically using audio from source (an AudioSource instance)
     recognizer.adjust_for_ambient_noise(source)
     audio=recognizer.listen(source)
     try:
        print("recognizing....")
        data = recognizer.recognize_google(audio)
        print(data)
        return data
     except sr.UnknownValueError:
        print("not understand")

# sptext()  # function calling

def speechtx(x):
 engine=pyttsx3.init()
 voice=engine.getProperty('voice')
 engine.setProperty('voice',voice[1])
 rate = engine.getProperty('rate')
 engine.setProperty('rate',150)
 engine.say(x)
 engine.runAndWait()

def sendemail(to , content):
       server=smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo()
       server.starttls()
       #Enable low security in gmail
       server.login("your email id ",'your email password')
       server.sendmail('your email id',to,content)
       server.close()
# speechtx("my name is harsh kumar upadhyay")
if __name__=='__main__':
#  if sptext().lower() == "pranjal" :
       #  print("harsh kumar")
# #    if 'pranjal' in sptext().lower():
       while True:
              data1 = sptext().lower()
              if "your name" in data1:
                     name="my name is pranjal"
                     speechtx(name)
                     
              elif"old are you" in data1:
                     age="i am 19years old"
                     speechtx(age)

              elif 'time' in data1:
                     time = datetime.datetime.now().strftime("%I %M %p")
                     speechtx(time)

              elif 'youtube' in data1:
                     webbrowser.open("https://www.youtube.com/")

              elif 'google' in data1:
                     webbrowser.open("https://www.google.com/")

              elif "joke" in data1:
                     joke_1 = pyjokes.get_joke(language="en",category="neutral")
                     print(joke_1)
                     speechtx(joke_1)

              elif 'play song' in data1:
                     webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
              
              elif "how are you" in data1:
                     speechtx("i am fine and you sir")

              elif 'email to ' in data1:
                     try:
                            speechtx("what should i say")
                            content= sptext()
                            speechtx("whome should I send")
                            to = input()
                            sendemail(to,content)
                            speechtx("email has been sent ")
                     except Exception as e:
                            print(e)
                            speechtx("i am not able to send this email")
		
              elif 'send a mail' in data1:
                     try:
                            speechtx("what should I say")
                            content= sptext()
                            speechtx("whome should I send")
                            to = input()
                            sendemail(to,content)
                            speechtx("email has been sent ")
                     except Exception as e:
                            print(e)
                            speechtx("i am not able to send this email")
              
              elif 'who i am 'in data1:
                     speechtx("if you talk then definitely you are human")
              
              elif "why you came to world "in data1:
                     speechtx("thanks to harsk upadhyay ji . further it is a secret")

              elif 'who are you' in data1:
                     speechtx("i am your best friend")
              
              		# elif "send message " in query:
    				# # You need to create an account on Twilio to use this service
				# account_sid = 'Account Sid key'
				# auth_token = 'Auth token'
				# client = Client(account_sid, auth_token)

				# message = client.messages \
				# 				.create(
				# 					body = takeCommand(),
				# 					from_='Sender No',
				# 					to ='Receiver No'
				# 				)
				# print(message.sid)
                     # elif 'send message' in data1:
                            



              elif 'exit' in data1:
                     speechtx("thank you")
                     break
              
              
              else:
                print("thanks you sir ")
