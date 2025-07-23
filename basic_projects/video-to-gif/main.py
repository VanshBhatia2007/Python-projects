from moviepy import *

video = VideoFileClip(r"C:\Users\HP\Downloads\Recording 2025-07-16 184431.mp4").subclipped(00,3)

video.write_gif("test.gif")