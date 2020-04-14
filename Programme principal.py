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

terrain.grid(row=1 , column=1, columnspan=19)

tir_raté = Button(fenetre,text ='tir raté').grid(row=4,column=1)
tir_réussi = Button(fenetre,text ='tir réussi').grid(row=4,column=4)
ballon_perdu = Button(fenetre,text ='ballon perdu').grid(row=4,column=9)
ballon_récupéré = Button(fenetre,text ='ballon récupéré').grid(row=4,column=15)
rebond_offensif = Button(fenetre,text ='rebond offensif').grid(row=4,column=19)
rebond_defensif = Button(fenetre,text ='rebond défensif').grid(row=5,column=7)
faute_subie = Button(fenetre,text ='faute subie').grid(row=5,column=12)
faute = Button(fenetre,text ='faute').grid(row=6,column=1)
lancer_réussi = Button(fenetre,text ='lancer réussi').grid(row=6,column=4)
lancer_raté = Button(fenetre,text ='lancer raté').grid(row=6,column=9)
passe_décisive = Button(fenetre,text ='passe décisive').grid(row=6,column=15)

joueur_1 = Button(fenetre,text ='joueur 1').grid(row=3,column=1)
joueur_2 = Button(fenetre,text ='joueur 2').grid(row=3,column=2)
joueur_3 = Button(fenetre,text ='joueur 3').grid(row=3,column=3)
joueur_4 = Button(fenetre,text ='joueur 4').grid(row=3,column=4)
joueur_5 = Button(fenetre,text ='joueur 5').grid(row=3,column=5)
joueur_6 = Button(fenetre,text ='joueur 6').grid(row=3,column=6)
joueur_7 = Button(fenetre,text ='joueur 7').grid(row=3,column=7)
joueur_8 = Button(fenetre,text ='joueur 8').grid(row=3,column=8)
joueur_9 = Button(fenetre,text ='joueur 9').grid(row=3,column=9)
joueur_10 = Button(fenetre,text ='joueur 10').grid(row=3,column=10)

joueur_visiteur_1 = Button(fenetre).grid(row=3,column=11)
joueur_visiteur_2 = Button(fenetre).grid(row=3,column=12)
joueur_visiteur_3 = Button(fenetre).grid(row=3,column=13)
joueur_visiteur_4 = Button(fenetre).grid(row=3,column=14)
joueur_visiteur_5 = Button(fenetre).grid(row=3,column=15)
joueur_visiteur_6 = Button(fenetre).grid(row=3,column=16)
joueur_visiteur_7 = Button(fenetre).grid(row=3,column=17)
joueur_visiteur_8 = Button(fenetre).grid(row=3,column=18)
joueur_visiteur_9 = Button(fenetre).grid(row=3,column=19)
joueur_visiteur_10 = Button(fenetre).grid(row=3,column=20)

label1=input('Nom équipe1')
label2=input('Nom équipe2')

Label(text=label1).grid(row=2,column=5)
Label(text=label2).grid(row=2,column=15)

fenetre.mainloop()