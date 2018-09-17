import pygame.mixer
from tkinter import *

def wait_finish(channel):
    if channel.get_busy():
        pass

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")


def correct_sound():
    wait_finish(correct_s.play())
    number_correct.set(number_correct.get() + 1)


def wrong_sound():
    wait_finish(wrong_s.play())
    number_wrong.set(number_wrong.get() + 1)

def quit():
    lb_correct = Label(app, textvariable=number_correct)
    number_correct.set(number_correct)
    lb_wrong = Label(app, textvariable=number_wrong)
    number_wrong.set(number_wrong)

app = Tk()
app.title("gooey game: judging")
app.geometry('400x300+200+200')
#add button before mainloop()
number_correct = IntVar()
number_correct.set(0)
number_wrong = IntVar()
number_wrong.set(0)
lb_prompt = Label(app,text = 'when you\'re ready, click the buttons',height = 3)
lb_prompt.pack()
lb_correct = Label(app, textvariable = number_correct)
lb_correct.pack(side = 'left')
lb_wrong = Label(app, textvariable = number_wrong)
lb_wrong.pack(side = 'right')
btn_correct = Button(app,text="correct",width = 10,command = correct_sound)
btn_correct.pack()#(side = 'left')

btn_wrong = Button(app,text = "wrong",width =10,command = wrong_sound)
btn_wrong.pack()#(padx = 20,pady = 20)

btn_quit = Button(app,text = "Quit",width =10,command = quit)
btn_quit.pack()#(side = 'right')
app.mainloop()










