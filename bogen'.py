from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = '#E6CE64'

wanted_text = Text(app, "Wanted!")
wanted_text.text_size = 50
wanted_text.text_font = "Times new roman"

micas = Picture(app, image = "swolegus.gif")

app.display()