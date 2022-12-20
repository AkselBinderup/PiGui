from guizero import App, Text, PushButton, Window, Picture, Box
import webbrowser

#Nyheder
def openchrome():
    webbrowser.get(Chrome).open_new("google.com")

def bt():
    webbrowser.get(Chrome).open_new("bt.dk")
    
def jp():
    webbrowser.get(Chrome).open_new("jyllands-posten.dk")
    
def dr():
    webbrowser.get(Chrome).open_new("dr.dk")

def eb():
    webbrowser.get(Chrome).open_new("eb.dk")

def wa():
    webbrowser.get(Chrome).open_new("weekendavisen.dk")

def inf():
    webbrowser.get(Chrome).open_new("information.dk")

def roko():
    webbrowser.get(Chrome).open_new("rokokoposten.dk")

def berl():
    webbrowser.get(Chrome).open_new("berlingske.dk")

def nord():
    webbrowser.get(Chrome).open_new("nordjyske.dk")
    
#-------Film og serier-------
def netflix():
    webbrowser.get(Chrome).open_new("netflix.com")

def viaplay():
    webbrowser.get(Chrome).open_new("viaplay.dk")

def disney():
    webbrowser.get(Chrome).open_new("disneyplus.com")

def hbo():
    webbrowser.get(Chrome).open_new("hbomax.com")
    
#-------filer define--------
def spild():
    webbrowser.get(Chrome).open_new("https://tc201512-my.sharepoint.com/:x:/g/personal/akse0708_elev_techcollege_dk/EeISE4B_MGRBl3821HpGpzEBC1JyK7e_sF-gFLS5ptf73A?e=wYVCxu")
def noter():
    webbrowser.get(Chrome).open_new("https://tc201512-my.sharepoint.com/:x:/g/personal/akse0708_elev_techcollege_dk/EQNvN8WbXkZBnnL4b2w4SvEBPS5o5xU-5Fi4c5VGLTdKJg?e=FU1pep")
def fotos():
    webbrowser.get(Chrome).open_new("https://tc201512-my.sharepoint.com/:w:/g/personal/akse0708_elev_techcollege_dk/EW2bfUMYww5Kv_yOq_MksmQBgqwEcCbbw2yTyXJpodJruA?e=Lb5NRh")
def lektier():
    webbrowser.get(Chrome).open_new("https://all.studieplus.dk/opgave/?id=id_menu_opgaver#oversigt:")
    
#-------kommandoer til at åbne forskellige docs og excel ark---------
def film_excel():
    webbrowser.get(Chrome).open_new("https://tc201512-my.sharepoint.com/:x:/g/personal/akse0708_elev_techcollege_dk/EfoGfQZtLzVClTppGv0Hw-UBEMw3s0irxRa02-P1cbMI8Q?e=YkCmZb")    

def serier_excel():
    webbrowser.get(Chrome).open_new("https://tc201512-my.sharepoint.com/:x:/g/personal/akse0708_elev_techcollege_dk/Ed9700S5l_RGiOa8ClSgGakBJ_4aLxCBrM3uhJRpPSBp4g?e=SFRcbK")    

#-------kommando for at åbne og lukke et vindue #1  -------
def open_window():
    window.show()
    
def close_window():
    window.hide()

#-------vindue2 define-------
def open_window2():
    window2.show()
def close_window2():
    window2.hide()
    
def open_window3():
    window3.show()
def close_window3():
    window3.hide()
    
def open_window4():
    window4.show()
def close_window4():
    window4.hide()
    
def open_window5():
    window5.show()
def close_window5():
    window5.hide()
    
#-------define interwindow-------
def open_window6():
    nyefilm.show()
def close_window6():
    nyefilm.hide()
def open_window7():
    nyeserier.show()
def close_window7():
    nyeserier.hide()
    
def luk():
    exit()
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
#-------box2-------

 
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
window2 = Window(app,title = "Film og serier")
window2.hide()

window2.width = 1920
window2.height = 1080

window2.bg = "#348D91"
window2_text = Text(window2, text = "Film og serier")
window2_text.text_size = 128
window2_text.text_color = "#CBD0CF"

box2 = Box(window2, align="left", width="fill", border=2)

#------Ny knap-------
nyefilm = Window(window2, title = "Film-liste")
nyefilm.hide()

nyefilm.width = 1920
nyefilm.height = 1080

nyefilm.bg = "#348D91"
nyefilm_text = Text (nyefilm, text = "Film-Liste")
nyefilm_text.text_size = 128
nyefilm_text.text_color = "#CBD0CF"

#--------ny knap (serier)-------
nyeserier = Window(window2, title = "Serie-liste")
nyeserier.hide()

nyeserier.width = 1920
nyeserier.height = 1080

nyeserier.bg = "#348D91"
nyeserier_text = Text (nyeserier, text = "Serie-liste")
nyeserier_text.text_size = 128
nyeserier_text.text_color = "#CBD0CD"

#-------knap3 vindue------
window3 = Window(app,title = "Filer")
window3.hide()

window3.width = 1920
window3.height = 1080

window3.bg = "#348D91"
window3_text = Text(window3, text = "Filer")
window3_text.text_size = 128
window3_text.text_color = "#CBD0CF"

box4 = Box(window3, align="left", width="fill", border=2)


#-------knap4 vindue-------
window4 = Window(app,title = "Nyheder")
window4.hide()

window4.width = 1920
window4.height = 1080

window4.bg = "#348D91"
window4_text = Text(window4, text = "Nyheder")
window4_text.text_size = 128
window4_text.text_color = "#CBD0CF"

box3 = Box(window4, align="left", width="fill", border=2)

#-------knap5 vindue-------
window5 = Window(app,title = "Skolearbejde")
window5.hide()

window5.width = 1920
window5.height = 1080

window5.bg = "#348D91"
window5_text = Text(window5, text = "Skolearbejde")
window5_text.text_size = 128
window5_text.text_color = "#CBD0CF"

#-------knap 1 og 2, de er sat ind i en box og er lavet som pushbutton så der er en knap, så er de alignet til
#-------venstre og har en command der åbner vindue-----------
button = PushButton (box, image="controller.jpg", align="left", command=open_window) 

spiltext = Picture(box, image="textwindows.jpg", align="left")
spiltext.height = 175
spiltext.width = 200

button2 = PushButton (box, image = "film.png", align="left", command=open_window2)

spiltext1 = Picture(box, image="text1.jpg", align="left")
spiltext1.height = 175
spiltext1.width = 200

button3 = PushButton (box, image = "mikkelsus.png", align="left", command=open_window3)

spiltext2 = Picture(box, image="lll.jpg", align="left")
spiltext2.height = 175
spiltext2.width = 200

button4 = PushButton (box, image="airpods.png", align="left", command=open_window4)

spiltext3 = Picture(box, image="micas1.jpg", align="left")
spiltext3.height = 175
spiltext3.width =200

#-------Nyhedsknapperne------
bt1 = PushButton (box3, image = "bt.png", align="left", command=bt)

jp1 = PushButton(box3, image="jp.png", align="left", command=jp)

dr1 = PushButton (box3, image="dr.png", align="left", command=dr)

eb1 = PushButton (box3, image="eb.png", align="left", command=eb)

wa1 = PushButton (box3, image="wa.png", align="left", command=wa)

inf1 = PushButton (box3, image="inf.png", align="left", command=inf)

roko1 = PushButton (box3, image="roko.jpg", align="left", command=roko)

berl1 = PushButton (box3, image="berl.png", align="left", command=berl)

nord1 = PushButton (box3, image="nord.png", align="left", command=nord)

button5 = PushButton (box, image="take.png", align="left", command=open_window5)

#----------------Streaming tjenester-------------------
netflix1 = PushButton (box2, image="netflix.png", align="left", command=netflix)
viaplay1 = PushButton (box2, image="viaplay.png", align="left", command=viaplay)
disney1 = PushButton (box2, image="disney.png", align="left", command=disney)
hbo1 = PushButton (box2, image="hbo.png", align="left", command=hbo)

#-------Filer-------
spild1 = PushButton (box4, image="folder1.png", align="left", command=spild)
error1 = Picture (box4, image="error.jpg", align = "left")
noter1 = PushButton (box4, image="folder1.png", align="left", command=noter)
fotos1 = PushButton (box4, image="folder1.png", align="right", command=lektier)
error2 = Picture (box4, image="error2.jpg", align = "right")
lektier1 = PushButton (box4, image="folder1.png", align="right", command=fotos)

#-------vindue4-----------
spiltext4 = Picture(box, image="skole.jpg", align="left")
spiltext4.height = 175
spiltext4.width =200

nyefilm1 = PushButton(box2, image = "folder1.png", align = "left", command = film_excel)

Chrome = "/bin/chromium-browser"
nyeserier1 = PushButton(box2, image = "folder1.png", align = "right", command = serier_excel)


#-------ændrer knappens størrelse-------
button.height = 175
button.width = 175

button2.height = 175
button2.width = 175

button3.height = 175
button3.width = 175

button4.height = 175
button4.width = 175

button5.height = 175
button5.width = 175

nyefilm1.height = 175
nyefilm1.width = 175

nyeserier1.height=175
nyeserier1.width=175

bt1.height=175
bt1.width=175

jp1.height=175
jp1.width=175

dr1.height=175
dr1.width=175

eb1.height=175
eb1.width=175

wa1.height=175
wa1.width=175

inf1.height=175
inf1.width=175

roko1.height=175
roko1.width=175

berl1.height=175
berl1.width=175

nord1.height=175
nord1.width=250

error1.height=175
error1.width=550

error2.height=175
error2.width=550

#------film og serier størrelse------
netflix1.height=175
netflix1.width=175

viaplay1.height=175
viaplay1.width=175

disney1.height=175
disney1.width=175

hbo1.height=175
hbo1.width=175

#-------Filer justering-------
spild1.height=175
spild1.width=175

noter1.height=175
noter1.width=175

fotos1.height=175
fotos1.width=175

lektier1.height=175
lektier1.width=175
#------knap lukke funktion de er opkaldt efter vinduerne, og har den tidligere definerede close window på.-------
button_close = PushButton (window, text = "tilbage til start", command=close_window)

button2_close = PushButton (window2, text = "tilbage til start", command=close_window2)

button3_close = PushButton (window3, text = "tilbage til start", command=close_window3)

button4_close = PushButton (window4, text = "tilbage til start", command=close_window4)

button5_close = PushButton (window5, text = "tilbage til start", command=close_window5)

nyefilm1_close = PushButton (nyefilm, text = "tilbage til start", command=close_window6)

nyeserier1_close = PushButton (nyeserier, text = "tilbage til start", command=close_window7)
#-------EXIT-------
lukknap = PushButton (app, text="Luk siden", command=luk)

app.display()
