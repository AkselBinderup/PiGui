from guizero import App, Text, PushButton, Window, Picture, Box

#-------kommando for at åbne og lukke et vindue #1-------
def open_window():
    window.show()
    
def close_window():
    window.hide()

#-------vindue2 define-------
def open_window2():
    window2.show()
def close_window2():
    window2.hide()
#-------forsiden-------
app = App(title = "PiGui")
app.width = 1920
app.height = 1080
our_text = Text (app, text = "PiGui")
our_text.text_size = 128
our_text.text_color = "#CBD0CF"
app.bg = "#348D91"
#-------box-------
box = Box(app, align="left", width="fill", border=2)
#-------det nye vindue-------
window = Window(app, title = "Spil")
window.hide()
window.width = 1920
window.height = 1080

window.bg = "#348D91"
window_text = Text(window, text = "Spil")
window_text.text_size = 128
window_text.text_color = "#CBD0CF"


#-------Knap2 vindue-------
window2 = Window(app,title = "Film")
window2.hide()

window2.width = 1920
window2.height = 1080

window2.bg = "#348D91"
window2_text = Text(window2, text = "Film")
window2_text.text_size = 128
window2_text.text_color = "#CBD0CF"


#-------knap2-------
#-------knap1-----------
button = PushButton (box, image="controller.jpg", command=open_window)
button2 = PushButton (box, image="film.png", command=open_window2)
button.height = 150
button.width = 150

button2.height = 150
button2.width = 150

button_close = PushButton (window2, title = "tilbage til start", command=close_window)

button2_close = PushButton (window2, title = "tilbage til start", command=close_window2)



app.display()
