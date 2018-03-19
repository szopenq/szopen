from tkinter import *
import datetime
from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()
root = Tk()
root.title("Samia.pl odliczacz")

class Channel:
    def __init__(self,number):
        self.number= number
        self.seconds = 0
        self.counting = False
        self.color = ""
        self.fontColor = ""
        
    def draw(self):
        button = Button(root, width=15,height = 3, text = "CH " + str(self.number+1), command = self.startCounting).grid(row=self.number,column=0)
        minutes = str(datetime.timedelta(seconds=self.seconds))[2:]
        self.defineColor()
        text = Label(root, width=20, height = 3,font=("TkDefaultFont", 12), text= minutes,justify = LEFT, anchor=W, bg=self.color, fg=self.fontColor).grid(row=self.number,column=1)
    def startCounting(self):
        self.counting = True
        self.seconds = 1590
    def tick(self):
        if self.counting == True:
            if self.seconds == 1:
                self.counting = False
            self.seconds = self.seconds - 1
    def defineColor(self):
        if self.seconds == 0:
            self.color = "blue"
            self.fontColor = "white"
        elif self.seconds >= 1590/2:
            self.color = "green"
            self.fontColor = "white"
        elif self.seconds < 1590/2 and self.seconds > 180:
            self.color = "yellow"
            self.fontColor = "black"
        elif self.seconds == 180:
            toaster.show_toast("Veryhtus CH" + str(self.number+1),
                   "czas: " + str(datetime.timedelta(seconds=self.seconds))[2:],
                   icon_path="custom.ico",
                   duration=5,
                   threaded=True)
        else:
            self.color = "red"
            self.fontColor = "white"
    def notification(self):
        toaster.show_toast("VERYHTUS CH" + self.number+1,
                    "czas: " + str(datetime.timedelta(seconds=self.seconds))[2:],
                   icon_path="custom.ico",
                   duration=10)
    

channels = []


for i in range(0,8):
    aktualnyChannel = Channel(i)
    channels.append(aktualnyChannel)



root.minsize(width = 250, height = 470)
root.maxsize(width = 250, height = 470)
root.call('wm', 'attributes', '.', '-topmost', '1')

def cleanUp():
    for ele in root.winfo_children():
      ele.destroy()
    root.after(1000 * 60 * 2,cleanUp) 
      
def refresh():
    for i in range(len(channels)):
        channels[i].draw()
        channels[i].tick()
    root.after(1000,refresh)
    
if __name__ == '__main__':
    refresh()
    cleanUp()
    root.mainloop()
