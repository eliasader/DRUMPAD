from tkinter import *
import ttkbootstrap as tb
from pygame import mixer
mixer.init()
#Drums variables/ variaveis da bateria
kick = mixer.Sound("./Sounds/kick.mp3")
snare = mixer.Sound("./Sounds/snare.mp3")
hihat = mixer.Sound("./Sounds/hihat.mp3")
openhat = mixer.Sound("./Sounds/openhat.mp3")
shaker = mixer.Sound("./Sounds/shaker.mp3")
percussion = mixer.Sound("./Sounds/percussion.mp3")

#Sound playing funtions/ funções do som 
def playKick(*args):
    kick.play(loops=0)

def playSnare(*args):
    snare.play(loops=0)

def playHihat(*args):
    hihat.play(loops=0)

def playOpenhat(*args):
    openhat.play(loops=0)

def playPerc(*args):
    percussion.play(loops=0)

def playShaker(*args):
    shaker.play(loops=0)
            
#Creating window/ Criando janela
window = tb.Window(themename="cyborg")
#key events/ eventos do teclado
window.bind("<a>",playKick)
window.bind("<s>",playSnare)
window.bind("<d>",playHihat)
window.bind("<z>",playShaker)
window.bind("<c>",playOpenhat)
window.bind("<x>",playPerc)
#Window title and size/ Titulo e tamanho da janela
window.title("DRUMPAD!")
window.geometry('700x500')
window.resizable(False,False)
#Labels/Titulos
title = tb.Label(text="Drum Pad - Lo fi ", font=("Bahnschrift",28))
title.place(x=10,y=0)

#Labels/Titulos
subTitle = tb.Label(text="You can use keyboard keys!! (A,s,d,z,x,c)", font=("Bahnschrift",14))
subTitle.place(x=10,y=50)

#Create custom style/ criar estilo customizado

customStyle = tb.Style()
customStyle.configure('dark.TButton', font=("Bahnschrift",28))
#Buttons/Botões
kickBtn = tb.Button(window,text="KICK",bootstyle="dark",command=playKick,style="dark.TButton")
kickBtn.place(x=90,y=100)
snareBtn = tb.Button(window,text="SNARE",bootstyle="dark",command=playSnare,style="dark.TButton")
snareBtn.place(x=300,y=100)
#window´s main loop/ loop principal da janela
window.mainloop()