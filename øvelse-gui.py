from guizero import App, Text, PushButton, Combo, Box, ButtonGroup, CheckBox, Drawing, ListBox, Picture, Slider, TextBox, TitleBox, Waffle, Window

app=App()

box = Box(app)
box = Box(app, border=True)

choice = ButtonGroup(app, options=["cheese", "ham", "salad", "Shrimp"])

check = CheckBox(app, text="salad ?")

combo = Combo(app, options=["cheese", "bacon", "meat"])

drawing = Drawing(app)

listbox = ListBox(app, items=["jon", "Micas", "oliver"])

#start knap
def do_nothing():
    print("knap berørt")
    
button = PushButton(app, command=do_nothing)
#slut knap

slider = Slider(app)

text = Text(app, text="JON er qute")

textbox = TextBox(app)

titlebox = TitleBox(app, "title")
titlebox = TitleBox(app, "title", border = False)

waffle = Waffle(app)

window = Window(app)



app.display()