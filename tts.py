
import pyttsx3
engine = pyttsx3.init()
def text_to_speech(text):
	print("Text",text,engine.isBusy())
	if(engine.isBusy()):
		engine.stop()
	# voices = engine.getProperty('voices')
	# engine.setProperty('voice', voices[1].id) 
	# rate = engine.getProperty('rate')
	# engine.setProperty('rate', 125)
	# print (rate)
	if text == "":
		engine.say("Hello I am dobie, hope you are fine")
	else:
		engine.say(text)
	engine.runAndWait()