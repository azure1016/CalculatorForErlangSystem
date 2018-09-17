from tkinter import *
def save_data():
    save_file = open("transcriptsOfZhe.txt","a")
    save_file.write("Subject:\n")
    save_file.write("%s\n" % service.get())
    save_file.write("Score:\n")
    save_file.write("%s" % description.get("1.0",END))
    save_file.write("Pingyu:\n")
    save_file.write("%s\n" % address.get("1.0",END))
    save_file.close()
    service.set(None)
    description.delete("1.0",END)
    address.delete("1.0",END)

def read_line(file):
    rf = open(file)
    options = []
    for items in rf:
        options.append(items.rstrip())
    return options



app = Tk()
app.title("gooey application for Head-ex")
app.geometry('600x300+200+200')
Label(app, text = "Subject:").pack()
service = StringVar()
service.set(None)
#Radiobutton(app,text="cambridge, MA",value = "cambridge, MA",variable = service).pack()
#Radiobutton(app,text="cambridge, England",value = "cambridge, England",variable = service).pack()
#Radiobutton(app,text="canada, ON",value = "canada, ON",variable = service).pack()
OptionMenu(app,service,*read_line("subjects.txt")).pack()
Label(app, text = "Score:").pack()
description = Text(app,height = 3)
description.pack()
Label(app, text = "Pingyu:").pack()
address = Text(app,height =3)
address.pack()

Button(app, text = "save", command = save_data).pack()

app.mainloop()

