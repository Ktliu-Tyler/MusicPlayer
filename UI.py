from tkinter import *
import tkinter.ttk as ttk

class UI:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 250
        self.window = Tk()
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.window.title("Music Player")
        self.window.configure(bg="#220088")
        self.optionColor = "silver"
        self.allSetting()

    def allSetting(self):
        self.varSetting()
        self.PlayListSetting()
        self.OptionSetting()

    def varSetting(self):
        self.musicList = []
        self.musicName = "Please choice the song first"
        self.musicNameVar = StringVar(self.window, self.musicName)
        self.SbttText = "Start"
        self.bttTextVar1 = StringVar(self.window, self.SbttText)
        self.CbttText = "Replay"
        self.bttTextVar2 = StringVar(self.window, self.CbttText)
        self.MuVar = DoubleVar()
        self.VolVar = IntVar()

    def PlayListSetting(self):
        self.songsframe = LabelFrame(self.window, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        self.songsframe.place(x=self.WIDTH//3*2, y=0, width=self.WIDTH//3, height=self.HEIGHT)
        self.scrol_y = Scrollbar(self.songsframe, orient=VERTICAL)
        self.playlist = Listbox(self.songsframe, yscrollcommand=self.scrol_y.set, selectbackground="gold", selectmode=BROWSE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        self.scrol_y.pack(side=RIGHT, fill=Y)
        self.scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

    def OptionSetting(self):
        self.Optionframe = LabelFrame(self.window, text="Option", font=("times new roman", 15, "bold"), bg="grey",
                                     fg="white", bd=5, relief=GROOVE)
        self.Optionframe.place(x=0, y=0, width=self.WIDTH//3*2, height=self.HEIGHT)
        self.Openbutton = Button(self.Optionframe, text="Choice Directory", bg=self.optionColor)
        self.Openbutton.grid(row=0, column=0, ipady=5, padx=10, pady=10)
        self.MuLabel = Label(self.Optionframe, width=32, height=1, bg=self.optionColor, textvariable=self.musicNameVar)
        self.MuLabel.grid(row=0, column=1, columnspan=4, ipady=5, padx=10, pady=10)
        self.MuScale = ttk.Scale(self.Optionframe, length=350, variable=self.MuVar, from_=0, to=100)
        self.MuScale.grid(row=2, column=0, columnspan=5, ipady=5, padx=10, pady=10)
        self.volScale = Scale(self.Optionframe, orient="horizontal", bg="gray", variable=self.VolVar, relief=GROOVE)
        self.volScale.grid(row=3, column=0, ipady=5, padx=10, pady=10)
        self.Backbutton = Button(self.Optionframe, text="Back", width=7, bg=self.optionColor)
        self.Backbutton.grid(row=3, column=1)
        self.Playbutton = Button(self.Optionframe, textvariable=self.bttTextVar1, width=7, bg=self.optionColor)
        self.Playbutton.grid(row=3, column=2)
        self.Nextbutton = Button(self.Optionframe, text="Next",width=7, bg=self.optionColor)
        self.Nextbutton.grid(row=3, column=3)
        self.Changebutton = Button(self.Optionframe, textvariable=self.bttTextVar2,width=7, bg=self.optionColor)
        self.Changebutton.grid(row=3, column=4)

    def start(self):
        self.window.update()
        self.window.mainloop()



if __name__=="__main__":
    window = UI()
    window.start()