from tkinter import *
import datetime
from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()
root = Tk()
root.title("Samia.pl odliczacz")

class StartPage:
    def __init__(self):
        self.options = ["Olimpus", "Veryhtus", "Temani"]
        self.times = [17 * 60 + 30, 26 * 60 + 30, 46 * 60 + 30]
        self.choosed = False
    def draw(self):
        olimpus = Button(root, width=15, height = 3, text = self.options[0], command = self.Olimpus)
        veryhtus = Button(root, width=15, height = 3, text = self.options[1], command = self.Veryhtus)
        temani = Button(root, width=15, height = 3, text = self.options[2], command = self.Temani)
        olimpus.pack()
        veryhtus.pack()
        temani.pack()

    def Olimpus(self):
        self.choosed = True
        for i in range(0,8):
            aktualnyChannel = Channel(i, self.times[0])
            channels.append(aktualnyChannel)
            
    def Veryhtus(self):
        self.choosed = True
        for i in range(0,8):
            aktualnyChannel = Channel(i, self.times[1])
            channels.append(aktualnyChannel)
            
    def Temani(self):
        self.choosed = True
        for i in range(0,8):
            aktualnyChannel = Channel(i, self.times[2])
            channels.append(aktualnyChannel)

class Channel:
    def __init__(self,number,time):
        self.number= number
        self.time = time
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
        self.seconds = self.time
        
    def tick(self):
        if self.counting == True:
            self.seconds = self.seconds - 1
            if self.seconds == 1:
                self.counting = False
            
    def defineColor(self):
        if self.seconds == 0:
            self.color = "blue"
            self.fontColor = "white"
        elif self.seconds >= self.time/2:
            self.color = "green"
            self.fontColor = "white"
        elif self.seconds < self.time/2 and self.seconds > 180:
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


#for i in range(0,8):
#    aktualnyChannel = Channel(i,1590)
#    channels.append(aktualnyChannel)



root.minsize(width = 250, height = 470)
root.maxsize(width = 250, height = 470)
root.call('wm', 'attributes', '.', '-topmost', '1')

def cleanUp():
    if sp.choosed == True:
        for ele in root.winfo_children():
          ele.destroy()
    #root.after(1000 * 60 * 2,cleanUp) 
      
def refresh():
    cleanUp()
    if sp.choosed == True:
        for i in range(len(channels)):
            channels[i].draw()
            channels[i].tick()
    root.after(1000,refresh)


sp = StartPage()

if __name__ == '__main__':
    sp.draw()
    #cleanUp()
    refresh()
    root.mainloop()
