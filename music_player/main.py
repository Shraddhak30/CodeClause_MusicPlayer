import os
from tkinter import *
import tkinter as tk
from tkinter import ttk ,filedialog
from pygame import mixer

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


logo=PhotoImage(file="itunes.png")
root.iconphoto(False,logo)

Top=PhotoImage(file="top.png")
Label(root,image=Top,bg="#0f1a2b").pack()

Logo=PhotoImage(file="itunes.png")
Label(root,image=Logo,bg="#345bc9").place(x=25,y=25)

play=PhotoImage(file="play.png")
Button(root,image=play,bg="#0f1a2b",bd=0,command=play_song).place(x=100,y=400)

stop=PhotoImage(file="stop.png")
Button(root,image=stop,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=30,y=500)

resume=PhotoImage(file="resume.png")
Button(root,image=resume,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=115,y=500)

pause=PhotoImage(file="pause-button.png")
Button(root,image=pause,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=200,y=500)

music=Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=150,y=340,anchor="center")

menu=PhotoImage(file="list.png")
Label(root,image=menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=300)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330,y=300)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()