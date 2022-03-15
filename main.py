import tkinter
from tkinter import *
from tkinter import  ttk,messagebox
import googletrans
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
from multiprocessing import process
import sys

root=Tk()

root.title("Python Language Translator")
root.geometry("1075x400")
root.resizable(False,False)
root.configure(bg="lightsteelblue")

def clear():
    left_textbox.delete(1.0, END)
    right_textbox.delete(1.0, END)

def information():
    messagebox.showinfo("Python Language Translator","Please read the following instructions:\n"
                                                     "1. Select a language from each box \n"
                                                     "2. Enter the text you would like to translate \n"
                                                     "3. Click the Translate button")

def speech_recognition():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
        try:
            audio_text = r.recognize_google(audio)
            left_textbox.insert(tkinter.INSERT,str(audio_text).capitalize())
            print("Finished")
        except:
            messagebox.showerror("Audio Recording","Please Try Again")

def label_change():
    left_lang=left_combo.get()
    right_lang=right_combo.get()
    left_label.configure(text=left_lang)
    right_label.configure(text=right_lang)
    root.after(100, label_change)

def translate_now():
    try:
        temp_text=left_textbox.get(1.0,END)
        translator=Translator()
        translated_text=translator.translate(temp_text,src=left_combo.get(),dest=right_combo.get())
        translated_text=translated_text.text
        right_textbox.delete(1.0,END)
        right_textbox.insert(END,translated_text)
    except Exception as e:
        messagebox.showerror("Python Language Translator","Please try again")

def left_speech_engine():
    left_speech_engine = pyttsx3.init()
    left_speech_engine.say(left_textbox.get(1.0,END))
    left_speech_engine.runAndWait()

def langauge_detect():
    translator = Translator()
    textbox_text = (left_textbox.get(1.0,END))
    detected_lang = translator.detect(str(textbox_text))
    try:
        messagebox.showinfo("Python Language Translator",str(detected_lang))
    except Exception as e:
        messagebox.showinfo("Python Language Translator","Language could not be detected")

def swap_cbox():
    temp_left_combo = left_combo.get()
    temp_right_combo = right_combo.get()
    left_combo.set(temp_right_combo)
    right_combo.set(temp_left_combo)

#Icon
image_icon=PhotoImage(file="icons8-python-64.png")
root.iconphoto(False,image_icon)

#Arrow
arrow_image = PhotoImage(file="data-in-both-directions.png")
swap_button = Button(root,image=arrow_image,relief="raised",borderwidth=4,command=swap_cbox,bg="white")
swap_button.place(x=485,y=50)

#List of Languages
language=googletrans.LANGUAGES
language_values=list(i.capitalize() for i in language.values())
#lang1=language.keys()

#Left ComboBox
left_combo=ttk.Combobox(root,values=language_values,font="Courier 14",state="r")
left_combo.place(x=110,y=20)
left_combo.set("English")

left_label=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
left_label.place(x=10,y=50)

#Left Frame
left_frame=Frame(root,bg="Black",bd=5)
left_frame.place(x=10,y=118,width=440,height=210)

#Left Textbox
left_textbox=Text(left_frame,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
left_textbox.place(x=0,y=0,width=430,height=200)

#Left Scrollbar
left_scrollbar=Scrollbar(left_frame)
left_scrollbar.pack(side="right",fill="y")
left_scrollbar.configure(command=left_textbox.yview)
left_textbox.configure(yscrollcommand=left_scrollbar.set)

#Right ComboBox
right_combo=ttk.Combobox(root,values=language_values,font="Courier 14",state="r")
right_combo.place(x=730,y=20)
right_combo.set("Select Language")

right_label=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
right_label.place(x=620,y=50)

#Right Frame
right_frame=Frame(root,bg="Black",bd=5)
right_frame.place(x=620,y=118,width=440,height=210)

#Right Textbox
right_textbox=Text(right_frame,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
right_textbox.place(x=0,y=0,width=430,height=200)

#Right ScrollBar
right_scrollbar=Scrollbar(right_frame)
right_scrollbar.pack(side="right",fill="y")
right_scrollbar.configure(command=right_textbox.yview)
right_textbox.configure(yscrollcommand=right_scrollbar.set)

#Translate Button
translate=Button(root,text="Translate",font="Courier 15 bold",
                   activebackground="lightsteelblue",relief="solid",cursor="hand2",bd=1,bg="white",
                   fg="black",command=translate_now)
translate.place(x=475,y=250)
label_change()

#Detect Button
detect=Button(root,text="Detect Language",font="Courier 15 bold",
                   activebackground="lightsteelblue",relief="solid",cursor="hand2",bd=1,bg="white",
                   fg="black",command=langauge_detect)
detect.place(x=865,y=345)

#Clear Button
clear=Button(root,text="Clear",font="Courier 15 bold",
                   activebackground="lightsteelblue",relief="solid",cursor="hand2",bd=1,bg="white",
                   fg="black",command=clear)
clear.place(x=500,y=310)

#Speech Button
audio_image = PhotoImage(file="high-volume.png")
speech=Button(root,image=audio_image,command=left_speech_engine, bg="white")
speech.place(x=10,y=335)

#Record Button
Record_image = PhotoImage(file="play-record.png")
speech=Button(root,image=Record_image,command=speech_recognition, bg="white")
speech.place(x=80,y=335)

#Information Button
info_image = PhotoImage(file="information--v1.png")
speech=Button(root,image=info_image,command=information, bg="white")
speech.place(x=150,y=335)

root.mainloop()
