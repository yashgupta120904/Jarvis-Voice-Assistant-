import datetime
import pyttsx3
import speech_recognition as sr 
import os
import webbrowser as web
import wikipedia
import keyboard
import pywhatkit
import pyautogui
Assistant = pyttsx3.init('sapi5')
voices= Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)



while True:
	def speak(audio):
		print("  ")
		Assistant.say(audio)
		print("  ")
		Assistant.runAndWait()


	def takecommand():
		command= sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening....")
			command.pause_threshold= 1
			audio= command.listen(source)
			
			try:
				print("Recognizing")
				query= command.recognize_google(audio,language='en-in')
				print(f"You Said : {query}")
			
			except Exception as Error:
				return 'none'
			return query.lower()
		

	query= takecommand()
                
    
	
	
	if 'hello' in query:
		speak("hello sir , I am Jarvis")
		speak("you personal AI Assistant , how may i help you")
	elif 'open chrome' in query:
		speak("opening sir")
		os.startfile("C:\\Users\\YashGupta\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
		speak("opened sir")

	
	elif 'jarvis how are you' in query:
		speak("I am Fine sir!")
		speak("what About YOU")
	elif 'I am fine' in query:
		speak("Feeling good after Hearing This")
		

	elif 'you need a break' in query:

		speak("ok sir , you can call me Anytime")
		break
    
	elif 'youtube search' in query:
		speak("OK sir, This Is what I found for Your Search!")
		query = query.replace("jarvis","")
		query = query.replace("youtube search" , "")
		w ='https://www.youtube.com/results?search_query='+ query
		web.open(w)
		speak("Done Sir!")
		break

	elif 'google search' in query:
		speak("This is what I found For Your Search Sir!")
		query = query.replace("jarvis" , "")
		query = query.replace("google search" , "")
		pywhatkit.search(query)
		speak("done sir")
		break

	elif 'open website' in query:
		speak("opening sir")
		query=query.replace ("jarvis","")
		query=query.replace("website","")
		w1 =query.replace("open","")
		w2  = "https://www." +w1+ ".com"
		web.open(w2)
		speak("Done Sir!")
		break
		

	elif 'open facebook' in query:
		speak("Ok Sir!")
		web.open("https://www.facebook.com")
		speak("Done Sir....!")
		break
        
	elif 'wikipedia search' in query:
		speak("Sreaching Wikipedia....")
		query = query.replace("jarvis","")
		query = query.replace("wikipedia" ,"")
		wiki = wikipedia.summary(query,10)
		speak(f"According To Wikipedia")
		print(wiki)
		speak(wiki)
		break
		
	elif 'play music' in query:
		speak("playing sir")
		query = query.replace("play music","")
		pywhatkit.playonyt(query)
		break
	     
		

	elif 'what is the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
             speak(f"Sir, the time is {strTime}")
             break
        
			



