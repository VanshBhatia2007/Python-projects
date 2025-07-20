from moviepy.editor import *
from tkinter.filedialog import askopenfilename


vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)

aud = video.audio

aud.write_audiofile("AUDIO.mp3")

print("END")