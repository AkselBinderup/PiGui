from guizero import App, Text, PushButton
from random import choice

def choose_name():
    #print("Button was pressed")

 first_names = ['Gus', 'Walter', 'Skylar', 'Hank', 'Saul']
 last_names = ['Obama', 'Tate', 'Biden', 'Rask', 'Bren']
 spy_name = choice(first_names) + " " + choice(last_names)
 #print(spy_name)
 name.value = spy_name

app = App("Meget hemmeligt spion navn (micas)")
app.bg = "white"

title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text="Tell me!")
button.text_color = "white"
button.bg = "red"
button.text_size = 30
name = Text(app, text="")
name.text_size = 50

app.display()