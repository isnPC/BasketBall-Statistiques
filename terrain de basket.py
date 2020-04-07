# Créé par Max, le 07/04/2020 en Python 3.4

from tkinter import *

fenetre = Tk()

terrain = Canvas(fenetre,width=600,height=500,background="grey",bd=8)

terrain.create_rectangle(50,300,550,50,fill="goldenrod", outline="white")

terrain.create_line(300,300,300,50,fill="white",width=1)

terrain.create_oval(240,115,360,235,width=1,fill="darkorange2",outline="white")
terrain.create_oval(250,125,350,225,width=1,fill="darkorange3",outline="white")

terrain.create_arc(25,75 ,225 ,275, extent=180, start=270,outline="white")
terrain.create_arc(375,75 ,575 ,275, extent=180, start=90,outline="white")

terrain.create_line(125,300,125,50,fill="goldenrod",width=1)
terrain.create_line(475,300,475,50,fill="goldenrod",width=1)

terrain.create_rectangle(50,140,175,210,fill="darkorange3", outline="white")
terrain.create_rectangle(425,140,550,210,fill="darkorange3", outline="white")

terrain.create_line(50,75,125,75,fill="white",width=1)
terrain.create_line(50,275,125,275,fill="white",width=1)
terrain.create_line(475,75,550,75,fill="white",width=1)
terrain.create_line(475,275,550,275,fill="white",width=1)

terrain.create_oval(390,140,460,210,width=1,outline="white")
terrain.create_oval(140,140,210,210,width=1,outline="white")

terrain.pack()

fenetre.mainloop()