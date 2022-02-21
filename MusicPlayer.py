import os
import time
import tkinter as tk
import UI
import MusicTool as tool
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import threading

class MusicPlayer():
    def __init__(self):
        self.window = UI.UI()
        self.music = tool.MusicTool()
        self.state = "Start"
        self.DirPath = ""
        self.NowMusic = ""
        self.playState = "replay"
        self.musicTime = 0
        self.index = -1
        self.musicStateTime = 0
        self.starting = False
        self.MuTimeChange = False
        self.setBtt()
        self.startTrack()

    def setBtt(self):
        self.window.playlist.bind('<<ListboxSelect>>', self.choiceMusic)
        self.window.MuScale.bind('<ButtonRelease>', self.musicProgress)
        self.window.volScale.bind('<ButtonRelease>', self.volume)
        self.window.Openbutton.configure(command=self.openDir)
        self.window.Backbutton.configure(command=self.Back)
        self.window.Playbutton.configure(command=self.Play_Stop)
        self.window.Nextbutton.configure(command=self.Next)
        self.window.Changebutton.configure(command=self.changeMode)

    def startTrack(self):
        t = threading.Thread(target=self.progressTracking)
        t.daemon = True
        t.start()

    def progressTracking(self):
        while True:
            if self.starting and self.music.Mulen != 0 and not self.MuTimeChange:
                self.musicTime = self.music.getMusicPos()
                Num = self.musicTime//(10*self.music.Mulen)
                print(self.musicTime)
                print(Num)
                self.musicTime = Num*10*self.music.Mulen+self.musicTime
                self.window.MuVar.set(Num+self.musicStateTime)
                time.sleep(0.2)
                if Num == -1:
                    if self.playState == "next":
                        self.Next()
                    elif self.playState == "replay":
                        self.Back()
                        self.Next()

            else:
                time.sleep(1)



    def openDir(self):
        self.window.playlist.delete(0, tk.END)
        filename = fd.askdirectory()
        self.DirPath = filename
        print(self.DirPath)
        Dir = os.listdir(self.DirPath)
        for f in Dir:
            self.window.playlist.insert(tk.END, f)
        showinfo(
            title='Selected Directory',
            message=filename
        )

    def choiceMusic(self, event):
        object = event.widget
        self.starting = False
        self.index = int(object.curselection()[0])
        print(self.index)
        musicFile = self.window.playlist.get(self.index)
        self.window.musicNameVar.set(musicFile)
        self.NowMusic = os.path.join(self.DirPath, musicFile)

    def musicProgress(self, value):
        self.MuTimeChange = True
        if self.music.Mulen != 0:
            self.music.rewind()
            self.musicStateTime = int(self.window.MuScale.get())
            pos = round(int(int(self.window.MuScale.get())*(10*self.music.Mulen))/1000, 3)
            self.music.just_play(pos)
        self.MuTimeChange = False


    def volume(self, value):
        value = round(self.window.VolVar.get()/100, 2)
        print(value)
        self.music.changeVolume(value)

    def Back(self):
        if self.index != 0 and self.NowMusic != "":
            self.starting = False
            print(self.index)
            self.window.playlist.select_clear(self.index)
            self.index -= 1
            self.window.playlist.select_set(self.index)
            musicFile = self.window.playlist.get(self.index)
            self.window.musicNameVar.set(musicFile)
            self.NowMusic = os.path.join(self.DirPath, musicFile)
            self.state = "Start"
            self.Play_Stop()



    def Play_Stop(self):
        if self.NowMusic != "":
            if not self.starting:
                self.musicStateTime = 0
                self.window.MuScale.set(0)
                self.starting = True
                self.music.playMusic(self.NowMusic)
            if self.state == "Stop":
                self.music.pauseMusic()
                self.state = "Start"
                self.window.bttTextVar1.set(self.state)
            elif self.state == "Start":
                self.music.continueMusic()
                self.state = "Stop"
                self.window.bttTextVar1.set(self.state)


    def Next(self):
        if self.NowMusic != "":
            if self.index+1 != len(os.listdir(self.DirPath)):
                self.starting = False
                print(self.index)
                self.window.playlist.select_clear(self.index)
                self.index += 1
                self.window.playlist.select_set(self.index)
                musicFile = self.window.playlist.get(self.index)
                self.window.musicNameVar.set(musicFile)
                self.NowMusic = os.path.join(self.DirPath, musicFile)
                self.state = "Start"
                self.Play_Stop()

    def changeMode(self):
        if self.playState == "next":
            self.playState = "replay"
            self.window.bttTextVar2.set("Replay")
        elif self.playState == "replay":
            self.playState = "next"
            self.window.bttTextVar2.set("normal")

if __name__=="__main__":
    MyMusicPlayer = MusicPlayer()
    MyMusicPlayer.window.start()
