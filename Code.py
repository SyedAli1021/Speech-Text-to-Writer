import speech_recognition as sr

R = sr . Recognizer()

with sr.Microphone() as source:
     print("Say something")
     audio = R.listen(source)

try:
   text = R.recognize_google(audio)
   print("You said that: {}" .format(text))
except:
      print ("Sorry could not identify your voice")