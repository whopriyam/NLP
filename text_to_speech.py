# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 

fh = open("ww2.txt", "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("audio.mp3")
fh.close()
