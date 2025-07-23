from moviepy import *
from tkinter.filedialog import askopenfilename


vid = askopenfilename()
video = VideoFileClip(vid)

aud = video.audio

aud.write_audiofile("AUDIO.mp3")

print("END")