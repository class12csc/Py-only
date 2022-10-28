from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("700x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background1.png")
background = canvas.create_image(
    336.0, 287.0,
    image=background_img)

img0 = PhotoImage(file = f"img00.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command=addProd,
    relief = "flat")

b0.place(
    x = 43, y = 285,
    width = 226,
    height = 66)

img1 = PhotoImage(file = f"img01.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = delProd,
    relief = "flat")


b1.place(
    x = 388, y = 295,
    width = 221,
    height = 51)

img2 = PhotoImage(file = f"img02.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = newCust,
    relief = "flat")

b2.place(
    x = 388, y = 384,
    width = 221,
    height = 51)

img3 = PhotoImage(file = f"img03.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = viewProds,
    relief = "flat")

b3.place(
    x = 52, y = 384,
    width = 217,
    height = 51)

window.resizable(False, False)
window.mainloop()
