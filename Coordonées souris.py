def pointeur(event):
    """ recupere les coordonnées du clic de souris sur le canvas """
    global posX, posY
    affCoord.configure(text = "X=" + str(event.x) +", Y =" + str(event.y))
    posX = event.x
    posY = event.y
    can.bind("<Button-1>", pointeur)