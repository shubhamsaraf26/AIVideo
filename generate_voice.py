
from gtts import gTTS

text = open("scripts/script.txt", "r", encoding="utf-8").read()
tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")
print("Voice generated")
