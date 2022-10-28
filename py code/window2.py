from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("700x600")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 600,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background2.png")
background = canvas.create_image(
    350.0, 297.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox00.png")
entry0_bg = canvas.create_image(
    368.5, 239.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#bbe7da",
    highlightthickness = 0)

entry0.place(
    x = 272.0, y = 217,
    width = 193.0,
    height = 43)
date=entry0
entry1_img = PhotoImage(file = f"img_textBox01.png")
entry1_bg = canvas.create_image(
    368.5, 358.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#bbe7da",
    highlightthickness = 0)

entry1.place(
    x = 272.0, y = 336,
    width = 193.0,
    height = 43)
prodName=entry1
entry2_img = PhotoImage(file = f"img_textBox02.png")
entry2_bg = canvas.create_image(
    368.5, 299.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#bbe7da",
    highlightthickness = 0)

entry2.place(
    x = 272.0, y = 277,
    width = 193.0,
    height = 43)
prodPrice=entry2
img0 = PhotoImage(file = f"img000.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 73, y = 425,
    width = 169,
    height = 62)

img1 = PhotoImage(file = f"img001.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 395, y = 421,
    width = 160,
    height = 71)

window.resizable(False, False)
window.mainloop()
