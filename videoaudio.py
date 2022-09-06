import moviepy.editor as mp # installed
from tkinter.filedialog import *

vid = askopenfilename()
video = mp.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile('demo.mp3')

print('done')