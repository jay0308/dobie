from tts import text_to_speech
from wikiSrc import who_is
import sys
import threading

text_to_speech("")

# Python program to translate
# speech to text and text to speech
  
  
import speech_recognition as sr
  
# Initialize the recognizer 
r = sr.Recognizer() 

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
  
          
# Loop infinitely for user to
# speak

  
while(1):    
    # Exception handling to handle
    # exceptions at the runtime
    print("In Loop")
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source2:
              
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if ("shutdown" in MyText) or ("stop" in MyText) or ("exit" in MyText) or ("quit" in MyText):
                text_to_speech("I am going off, bye bye have a great day")
                sys.exit()

           
  
            print("Did you say "+MyText)
            wikiRes = who_is("",MyText) 
            tts_thread = threading.Thread(target=text_to_speech, name="tts", args=[wikiRes])
            tts_thread.start()
            # text_to_speech(wikiRes)
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")