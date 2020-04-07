import tkinter
import math
from tkinter import *

root = tkinter.Tk()
root.geometry("800x800")
root.title("Capillary Action")
root.configure(background="white")


frame1 = Frame(root)
frame1.grid(sticky=W)
frame1.configure(background="white")
L1 = Label(frame1, text="Surface Tension (N/m)",bg="white")
L1.grid(row=0, column=1)
S1 = Scale(frame1, from_=0, to=0.1, resolution=0.0001, orient=HORIZONTAL, activebackground="orange",bg="white")
S1.grid(row=0, column=2)
E1 = Entry(frame1, bd=5, highlightcolor="blue", width=10,bg="white")
E1.grid(row=0, column=3)

frame2 = Frame(root)
frame2.grid(sticky=W)
frame2.configure(background="white")
L2 = Label(frame2, text="Contact Angle (°)",bg="white")
L2.grid(row=1, column=1)
S2 = Scale(frame2, from_=10, to=90, resolution=0.1, orient=HORIZONTAL, activebackground="orange",bg="white")
S2.grid(row=1, column=2)
E2 = Entry(frame2, bd=5, highlightcolor="blue", width=10,bg="white")
E2.grid(row=1, column=3)

frame3 = Frame(root)
frame3.grid(sticky=W)
frame3.configure(background="white")
L3 = Label(frame3, text="Density",bg="white")
L3.grid(row=2, column=1)
S3 = Scale(frame3, from_=500, to=2000, resolution=0.1, orient=HORIZONTAL, activebackground="orange",bg="white")
S3.grid(row=2, column=2)
E3 = Entry(frame3, bd=5, highlightcolor="blue", width=10,bg="white")
E3.grid(row=2, column=3)

frame4 = Frame(root)
frame4.grid(sticky=W)
frame4.configure(background="white")
L4 = Label(frame4, text="Capillary radius (mm)",bg="white")
L4.grid(row=3, column=1)
S4 = Scale(frame4, from_=0.5, to=6.5, resolution=0.01, orient=HORIZONTAL, activebackground="orange",bg="white")
S4.grid(row=3, column=2)
E4 = Entry(frame4, bd=5, highlightcolor="blue", width=10,bg="white")
E4.grid(row=3, column=3, sticky=E)

frame5 = Frame(root)
frame5.grid(sticky=W)
frame5.configure(background="white")
label1 = Label(frame5, text="Height (mm)=",bg="white")
label1.grid(row=4, column=1)
E5 = Entry(frame5, bd=5, highlightcolor="blue",bg="white")
E5.grid(row=4, column=2)


def scale(event):
    S1.set(float(E1.get()))
    S2.set(float(E2.get()))
    S3.set(float(E3.get()))
    S4.set(float(E4.get()))
    combine_funcs(event)


def cal_height(event):
    E1.delete(0, END)
    E1.insert(0, S1.get())
    gamma = float(S1.get())
    angle = float(S2.get())
    theta = math.cos(math.radians(angle))
    rho = float(S3.get())/1000
    radius = float(S4.get())
    a = 2*gamma*theta
    b = rho*radius*9.81
    E5.delete(0, END)
    h = (a/b)*1000
    height = round(h, 2)
    E5.insert(0, height)
    E5.grid(row=4, column=2)


C = tkinter.Canvas(root, bg="white", height=465, width=400)


def diagram(event):
    E1.delete(0, END)
    E1.insert(0, S1.get())
    gamma = float(S1.get())
    E2.delete(0, END)
    E2.insert(0, S2.get())
    angle = float(S2.get())
    theta = math.cos(math.radians(angle))
    E3.delete(0, END)
    E3.insert(0, S3.get())
    rho = float(S3.get())/1000
    E4.delete(0, END)
    E4.insert(0, S4.get())
    rad = float(S4.get())
    a = 2 * gamma * theta
    b = rho * rad * 9.81
    h = float((a / b) * 1000)
    height = round(h, 2)
    C.delete("all")
    coord7 = 190.5 + rad * 10, 410, 190.5 + (rad * 10), 410 - height*5 + theta, 190, 410 - height*5 + (
            8 * theta), 189.5 - rad * 10, 410 - height*5 + theta, 189.5 - rad * 10, 410
    C.create_polygon(coord7, fill="blue")
    # water line left side
    coord6 = 189.5-rad*10, 410, 179.5-rad*10, 415, 20, 415, 10, 410, 10, 460, 390, 460, 390, 410, 380, 415, 200.5+rad*10, \
             415, 190.5+rad*10, 410
    C.create_polygon(coord6, fill="light blue")

    # vertical radius line
    rad = float(S4.get())
    coord4 = 189.5 - rad * 10, 5, 189.5 - rad * 10, 440
    line4 = C.create_line(coord4, fill="red")
    coord5 = 190.5 + rad * 10, 4, 190.5 + rad * 10, 440
    line5 = C.create_line(coord5, fill="red")
    coord1 = 10, 380, 10, 460
    line1 = C.create_line(coord1, fill="red")
    coord2 = 390, 380, 390, 460
    line2 = C.create_line(coord2, fill="red")
    coord3 = 10, 460, 390, 460
    line3 = C.create_line(coord3, fill="red")
    C.grid(row=6, column=0)


def combine_funcs(event):
    diagram(event)
    cal_height(event)


E1.bind('<Return>', scale)
E2.bind('<Return>', scale)
E3.bind('<Return>', scale)
E4.bind('<Return>', scale)

S1.bind('<ButtonRelease-1>', combine_funcs)
S2.bind('<ButtonRelease-1>', combine_funcs)
S3.bind('<ButtonRelease-1>', combine_funcs)
S4.bind('<ButtonRelease-1>', combine_funcs)

C1 = tkinter.Canvas(root, bg="white", height=655, width=400)
coordA = 10, 5, 10, 190, 390, 190, 390, 5, 10, 5
lineA = C1.create_line(coordA, fill="black")
coordB = 76, 5, 76, 190, 240, 190, 240, 5
lineB = C1.create_line(coordB, fill="black")
coordC = 10, 35, 390, 35
lineC = C1.create_line(coordC, fill="black")
# Fluids Name
fluids = C1.create_text(35, 20, text="Fluids")
Water = C1.create_text(35, 50, text="Water")
Alcohol = C1.create_text(38, 80, text="Alcohol")
Diesel = C1.create_text(35, 110, text="Diesel")
Milk = C1.create_text(35, 140, text="Milk")
Petrol = C1.create_text(35, 170, text="Petrol")
# Specific Gravity
fluids1 = C1.create_text(160, 20, text="Surface Tension (N/m)")
Water1 = C1.create_text(150, 50, text="0.0727")
Alcohol1 = C1.create_text(150, 80, text="0.0223")
Diesel1 = C1.create_text(150, 110, text="0.00003")
Milk1 = C1.create_text(150, 140, text="0.0475")
Petrol1 = C1.create_text(150, 170, text="0.00002")
# Density
fluids3 = C1.create_text(320, 20, text="Density (kg/m^3)")
Water3 = C1.create_text(310, 50, text="997")
Alcohol3 = C1.create_text(310, 80, text="789")
Diesel3 = C1.create_text(310, 110, text="832")
Milk3 = C1.create_text(310, 140, text="1035")
Petrol3 = C1.create_text(310, 170, text="719.7")

# Theory
C1.create_text(210, 409, text="Capillary action is important for moving water \n (and all of the things that are "
                              "dissolved in it) around. \nIt is defined as the movement of water within the spaces \n of"
                              " aporous material due to the forces of adhesion,\n cohesion, and surface tension. \n  "
                              "Capillary action occurs because water is sticky, \n thanks to the forces of cohesion "
                              "(water molecules like \n to stay close together) and adhesion (water molecules are \n "
                              "attracted and stick to other substances). Adhesion of \n water to the walls of a vessel "
                              "will cause \n an upward force on the liquid at the edges and result \n in a meniscus "
                              "which turns upward. The surface tension acts \n to hold the surface intact. Capillary"
                              " action occurs when the \n adhesion to the walls is stronger than the cohesive forces"
                              " \nbetween the liquid molecules. The height to which capillary \naction will take "
                              "water in a uniform circular tube (picture to right) is \n limited by surface tension and"
                              "of course, gravity. \n   Liquids (such as water) that wet glass climb upward on the "
                              "\nsurfaces of their containers to form a concave meniscus. \n This occurs when  "
                              "adhesive solid-liquid intermolecular forces are \nstronger than liquid forces. Such "
                              "liquids will rise in a \n narrow capillary tube until a balance is established \n between "
                              "the effects of surface tension \n and gravity. "
                              "The capillary rise increases sharply as the tube is \n made narrower. For example, "
                              "water in a glass capillary of radius \n 0.1 mm will rise by about 140 mm . \n "
                              "The Formula used is : (2γ cosθ/ρgr) where \n γ=Surface tension \n ρ=Specific gravity "
                              "and r=Radius of Capillary tube ")
C1.place(x=400, y=0)

# Image
C2 = tkinter.Canvas(root, height=345, width=400)
photo ="""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"""
photo = PhotoImage(data=photo)
image = C2.create_image(5, 8, image=photo, anchor=NW)
C2.place(x=400, y=627)

frame6 = Frame(root, width=400, height=100)
frame6.place(x=0, y=660)
label2 = Label(frame6, text="Capillary Action", font="Times", fg="maroon")
label2.place(x=100, y=10)
root.mainloop()
