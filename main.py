import os
import random
from tkinter import *
import tkintermapview
from PIL import Image, ImageTk
from tkinter import messagebox

win = Tk()
win.title("first")
win.geometry("1060x800")
win["bg"] = "#7FFFD4"
win.resizable(False, False)
my_points = []
score = 50



class Answer:
    def __init__(self, country, city, attraction):
        self.country = country
        self.city = city
        self.attraction = attraction

answers = []
answers.append(Answer("Turkey", "Stambul", "Ortakoy Mosque"))
with open ("place.txt", "r") as file:
    for i in file:
        place = i.split(" | ")
        answers.append(Answer(place[0], place[1], place[2]))

geo = random.choice(answers)
# geo = answers[7]
print(geo.city)


def check_score():
    global score
    if score <= 0:
        fgh = messagebox.askretrycancel("You Lose", "you lost! your score has dropped below zero! Press 'retry' if you want to start over, or press 'cancel' if you want to end the game")
        if fgh == True:
            score = 50
            wallet.config(text="your" + "\n" + "score: " + str(score))
            f = Canvas(win, width=500, height=400, bg="#7FFFD4", highlightthickness=0)
            f.place(x=810, y=10)
            geo = random.choice(answers)
            print(geo.attraction)
            buttons(geo)
            widget_map.set_address(geo.attraction + " " + geo.city + " " + geo.country)
        else:
            win.destroy()


def buttons(true_answer):

    ans = []
    i = 0
    while i < 5:
        k = random.choice(answers)
        if k not in ans and k != true_answer:
            ans.append(k)
            i += 1
    ans.insert(random.randint(0, 5), true_answer)

    ans_1 = Button(win, text = ans_ans_ans(ans[0]))
    ans_1["command"] =lambda b=ans_1: check(ans[0], true_answer, b)
    ans_1.place(x=820, y=20)
    print(ans_1)

    ans_2 = Button(win, text=ans_ans_ans(ans[1]))
    ans_2["command"] = lambda b=ans_2: check(ans[1], true_answer, b)
    ans_2.place(x=820, y=80)

    ans_3 = Button(win, text=ans_ans_ans(ans[2]))
    ans_3["command"] = lambda b=ans_3: check(ans[2], true_answer, b)
    ans_3.place(x=820, y=140)

    ans_4 = Button(win, text=ans_ans_ans(ans[3]))
    ans_4["command"] = lambda b=ans_4: check(ans[3], true_answer, b)
    ans_4.place(x=820, y=200)

    ans_5 = Button(win, text=ans_ans_ans(ans[4]))
    ans_5["command"] = lambda b=ans_5: check(ans[4], true_answer, b)
    ans_5.place(x=820, y=260)

    ans_6 = Button(win, text=ans_ans_ans(ans[5]))
    ans_6["command"] = lambda b=ans_6: check(ans[5], true_answer, b)
    ans_6.place(x=820, y=320)
def check(answer, true_answer, button):
    global score
    print(button["text"])
    if answer == true_answer:
        score += 15
        wallet.config(text="your" + "\n" + "score: " + str(score))
        button.config(highlightbackground="green", fg="green")
        win.update()
        print("True")
        f = Canvas(win, width=500, height=400, bg="#7FFFD4", highlightthickness=0)
        f.place(x=810, y=10)
        geo = random.choice(answers)
        print(geo.attraction)
        buttons(geo)
        widget_map.set_address(geo.attraction + " " + geo.city + " " + geo.country)

    else:
        score -= 10
        wallet.config(text="your" + "\n" + "score: " + str(score))
        button.config(highlightbackground="red", fg="red")
        win.update()
        print(False)
        h = Canvas(win, width=500, height=400, bg="#7FFFD4", highlightthickness=0)
        h.place(x=810, y=10)
        geo = random.choice(answers)
        print(geo.attraction)
        buttons(geo)
        widget_map.set_address(geo.attraction + " " + geo.city + " " + geo.country)
        check_score()

def ans_ans_ans(ans):
    return ans.country + ", " + ans.city + "\n" + ans.attraction

buttons(geo)
def pajk(coordinates):
    m = widget_map.set_address("Troitsk, Moscow, Russia", marker=True, text="test")
    widget_map.set_zoom(11)
    img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images",
                                                     "../images/random_cat.jpg")).resize((300, 200)))
    b = widget_map.set_position(coordinates[0], coordinates[1], text="first", marker=True, image = img, image_zoom_visibility=(14, float("inf")))
    d = widget_map.set_path([m.position, b.position])

def olfg(coordinates):
    ad = tkintermapview.convert_coordinates_to_address(coordinates[0], coordinates[1])
try:
    fraim = LabelFrame(win)
    fraim.place(x=0, y=0)
    widget_map = tkintermapview.TkinterMapView(fraim, width=800, height=800, corner_radius=100)
    widget_map.pack()
except:
    messagebox.showwarning("error", "error")


f = Canvas(win, width=130, height=100, bg="#BEBEBE")
f.place(x=0, y=0)
widget_map.set_zoom(16)

wallet = Label(win, text="your" + "\n" + "score: " + str(score), font=('Terminal', 20, "italic"), bg="#BEBEBE")
wallet.place(x=5,  y=5)
widget_map.set_address(geo.attraction + " " + geo.city + " " + geo.country)

# widget_map.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")  # OpenStreetMap (default)
#widget_map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
try:
    widget_map.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google
except:
    messagebox.showwarning("error", "error")

    # satellite
#widget_map.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")  # painting stylepyinstaller --onefile -w

#widget_map.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")  # black and white
# widget_map.set_tile_server("https://tiles.wmflabs.org/osm-no-labels/{z}/{x}/{y}.png")  # no labels
#widget_map.set_tile_server("https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg")  # swisstopo map
#
# # example overlay tile server
##widget_map.set_overlay_tile_server("http://tiles.openseamap.org/seamark//{z}/{x}/{y}.png")  # sea-map overlay
#widget_map.set_overlay_tile_server("http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png")  # railway infrastructure

win.mainloop()