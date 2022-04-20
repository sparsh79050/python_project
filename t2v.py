from gtts import gTTS
import os

f=open('codewithus.txt')
x=f.read()

language="en"

audio=gTTS(text=x, lang=language, slow=False)

audio.save("1.wav")
os.system("1.wav")