from guizero import App, Text, Combo
from string import ascii_letters

#det skal være en dårlig GUI så man lærer af sine fejl

app = App("Verdens værste GUI") #App er navnet på popuppen.
title = Text(app, text="ulideligt-stykke.text", size="14", #overskrift, med skriftstørelse 14
font = "Comic Sans", color = "Green") # font comic sans og farve på tekst grøn

def flash_text (): #Laver et loop der siger hvis title er synlig skal den gemme den ellers viser den det og det gør den med 1000ms mellemrum.
    if title.visible:
        title.hide()
    else:
        title.show()

app.repeat(1000, flash_text) #laver tidsmellemrum



app.display
