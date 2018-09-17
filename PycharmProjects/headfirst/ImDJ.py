from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel

def track_start():
    track.play(loops = -1)

def track_stop():
    track.stop()

def shut_down():
    track_stop()
    if askokcancel(title='Are you sure to close the window?', message = 'Do you really want to quit?'):
        app.destroy()

mixer = pygame.mixer
mixer.init()
sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)

app = Tk()
app.title("I am a DJ playing music~")
app.geometry('400x600+100+200')

start_btn = Button(app,text="start",command = track_start)
start_btn.pack(side=LEFT)
stop_btn = Button(app, command = track_stop,text="stop")
stop_btn.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW",shut_down)
app.mainloop()