from guizero import App, Text, Picture, Window, PushButton

def open_window():
    window.show()

def close_window():
    window.hide()
    
def open():
    micas.show()

def close():
    micas.hide()

app = App(title = "Første vindue")

app.bg = "black"
our_text = Text (app, text = "Jon er cute")
our_text.text_size = 30
our_text.font = "Times new roman"
our_text.text_color = "white"
minecraft = Picture(app, image="Netflix.gif")
    
window = Window(app, title = "andet vindue")
window.hide()

window.bg = "pink"
our_text = Text (window, text = "Mathias har børn")
our_text.text_size = 12
our_text.font = "Arial"
neg = Picture(window, image="swolegus.gif")

open_button = PushButton(app, text="åben", command=open_window)
open_button.text_color ="White"

close_button = PushButton(window, text = "close", command=close_window)

micas = Window (app, title = "sorte børn")
micas.hide()

micas.bg = "blue"
our_text = Text (micas, text = "Gustavo fring micas cute")
our_text.text_size = 30
our_text.font = "Calibri"
fuck = Picture (micas, image = "download.jpeg")

open_button = PushButton(window, text="åben eller dø", command=open)
open_button.text_color ="yellow"

close_button = PushButton(micas, text = "close", command=close)

app.display()
