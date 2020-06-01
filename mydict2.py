from tkinter import *
from tkinter import messagebox
import backend
import json
import sys
import os
import difflib
from difflib import get_close_matches


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


data = json.load(open(resource_path('data.json')))

window = Tk()



def translate():
    list_box.delete('1.0', END)
    w=word_text.get()
    w = w.lower()
    if w in data:
        list_box.insert(END, data[w])
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        msgbox1 = messagebox.askquestion('Not Found',
            'Did you mean %s instead?' % get_close_matches(w, data.keys())[0])
        #0 is to check suggestions starting with the first word of the input
        if msgbox1 == 'yes':
            x = get_close_matches(w, data.keys())[0]
            word_text.insert(x)
            list_box.insert(END, data[x])
    else:
        msgbox2 = msgbox.askquestion('Alert','The word does not exist, do you want to continue?')
        if msgbox2=='yes':
            msgbox.showinfo('You will be directed back')
        else:
            msgbox.destroy()
        

#def translate_command():
#    list_box.delete('1.0', END)
#    for word in translate(word_text.get()):
#        list_box.insert(END, word)

def close_command():
    Msgbox = messagebox.askquestion("exit","Do you want to quit the dictionary?")
    if Msgbox=='yes':
        window.destroy()
    else:
        messagebox.showinfo("Return","You will now be directed back to the application")


def clear():
    list_box.delete('1.0', END)

window.wm_title('Dictionary')

l1=Label(window,text="Enter Word")
l1.grid(row=0,column=0)

l2=Label(window,text="Definition")
l2.grid(row=1,column=0)

b1=Button(window,text="Search",width=12,command=translate)
b1.grid(row=2,column=2)

b2=Button(window,text="Close",width=12,command=close_command)
b2.grid(row=4,column=2)

b3 = Button(window, text="Clear", width=12, command=clear)
b3.grid(row=3, column=2)

word_text = StringVar()
e1=Entry(window,textvariable=word_text)
e1.grid(row=0, column=1)

list_box = Text(window,wrap=WORD, height=20, width =35 )
list_box.grid(row=2,column=0, rowspan=15, columnspan=2)
 

window.mainloop()
