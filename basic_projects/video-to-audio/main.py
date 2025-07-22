from moviepy import *
from tkinter.filedialog import askopenfilename



video = moviepy.VideoFileClip(r"C:\Users\HP\Downloads\Recording 2025-07-16 184431.mp4")

aud = video.audio

aud.write_audiofile("AUDIO.mp3")

print("END")