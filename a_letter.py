from guizero import App, PushButton

app = App(title="pointless pop-up")

app.info("Application started", "Well done you started the application") #info popup du kan slukke

def are_you_sure():
    if app.yesno("Confirmation", "Are you sure?"):
        app.info("Thanks", "Button Pressed")
    else:
        app.error("ok", "cancelling")
        
button = PushButton(app, command=are_you_sure)

app.display()