import tkinter
from tkinter import *
import array
import tkinter.messagebox as tmsg


# About main window properties
root = tkinter.Tk()
root.geometry("1500x725")
root.configure(background="white")

# Title name
l = Label(root, text="External Convection over an Isoflux flat plate", font="times 20 italic bold", bg="white", fg="blue")
l.place(x=300, y=5)
Label(root, text="How do we calculate temp of this plate at any x-location, T(x)?", font="times 14 italic bold", bg="white", fg="green").place(x=50,y=40)
C7 = tkinter.Canvas(root, height=60, width=220,bg="white")
photo = """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"""
photo = PhotoImage(data=photo)
image = C7.create_image(2, 2, image=photo, anchor=NW)
C7.place(x=950, y=5)
# Image Canvas
canvas1 = tkinter.Canvas(root, width=800, height=240, bg="white")
# Arrows
coord = 0, 10, 50, 10
coord1 = 45, 0, 50, 10, 45, 20
canvas1.create_line(coord, coord1, fill="blue", width=1.5)    # first arrow

coord = 0, 50, 50, 50
coord1 = 45, 40, 50, 50, 45, 60
canvas1.create_line(coord, coord1, fill="blue", width=1.5)    # second arrow

coord = 0, 90, 50, 90
coord1 = 45, 80, 50, 90, 45, 100
canvas1.create_line(coord, coord1, fill="blue", width=1.5)    # third arrow

coord = 0, 130, 50, 130
coord1 = 45, 120, 50, 130, 45, 140
canvas1.create_line(coord, coord1, fill="blue", width=1.5)    # fourth arrow

coord = 0, 170, 50, 170
coord1 = 45, 160, 50, 170, 45, 180
canvas1.create_line(coord, coord1, fill="blue", width=1.5)    # fifth arrow

coord = 65, 140, 70, 130, 75, 140
coord1 = 70, 130, 70, 180
coord2 = 80, 155
canvas1.create_text(coord2, text="       y", font="bold", fill="red")    # Y-axis
canvas1.create_line(coord, coord1, fill="black", width=1.5)

coord11 = 170, 210, 180, 200, 190, 210
coord10 = 180, 200, 180, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)    # first arrow
coord11 = 210, 210, 220, 200, 230, 210
coord10 = 220, 200, 220, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 250, 210, 260, 200, 270, 210
coord10 = 260, 200, 260, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 290, 210, 300, 200, 310, 210
coord10 = 300, 200, 300, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 330, 210, 340, 200, 350, 210
coord10 = 340, 200, 340, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 370, 210, 380, 200, 390, 210
coord10 = 380, 200, 380, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 410, 210, 420, 200, 430, 210
coord10 = 420, 200, 420, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 450, 210, 460, 200, 470, 210
coord10 = 460, 200, 460, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 490, 210, 500, 200, 510, 210
coord10 = 500, 200, 500, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 530, 210, 540, 200, 550, 210
coord10 = 540, 200, 540, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 570, 210, 580, 200, 590, 210
coord10 = 580, 200, 580, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 610, 210, 620, 200, 630, 210
coord10 = 620, 200, 620, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)
coord11 = 650, 210, 660, 200, 670, 210
coord10 = 660, 200, 660, 240
canvas1.create_line(coord11, width=1.5)
canvas1.create_line(coord10, width=1.5)

coord = 70, 180, 750, 180
coord2 = 65, 180, 75, 190
coord3 = 85, 180, 95, 190
coord4 = 105, 180, 115, 190
coord5 = 125, 180, 135, 190
coord6 = 145, 180, 155, 190
coord7 = 165, 180, 175, 190
coord8 = 185, 180, 195, 190
coord9 = 205, 180, 215, 190
coord10 = 225, 180, 235, 190
coord11 = 245, 180, 255, 190
coord12 = 265, 180, 275, 190
coord13 = 285, 180, 295, 190
coord14 = 305, 180, 315, 190
coord15 = 325, 180, 335, 190
coord16 = 345, 180, 355, 190
coord17 = 365, 180, 375, 190
coord18 = 385, 180, 395, 190
coord19 = 405, 180, 415, 190
coord20 = 425, 180, 435, 190
coord21 = 445, 180, 455, 190
coord22 = 465, 180, 475, 190
coord23 = 485, 180, 495, 190
coord24 = 505, 180, 515, 190
coord25 = 525, 180, 535, 190
coord26 = 545, 180, 555, 190
coord27 = 565, 180, 575, 190
coord28 = 585, 180, 595, 190
coord29 = 605, 180, 615, 190
coord30 = 625, 180, 635, 190
coord31 = 645, 180, 655, 190
coord32 = 665, 180, 675, 190
coord33 = 685, 180, 695, 190
coord34 = 705, 180, 715, 190
coord35 = 725, 180, 735, 190
canvas1.create_line(coord2, fill="yellow", width=2)     # plate
canvas1.create_line(coord3, fill="yellow", width=2)     # plate
canvas1.create_line(coord4, fill="yellow", width=2)     # plate
canvas1.create_line(coord5, fill="yellow", width=2)     # plate
canvas1.create_line(coord6, fill="yellow", width=2)     # plate
canvas1.create_line(coord7, fill="yellow", width=2)     # plate
canvas1.create_line(coord8, fill="yellow", width=2)     # plate
canvas1.create_line(coord9, fill="yellow", width=2)     # plate
canvas1.create_line(coord10, fill="yellow", width=2)     # plate
canvas1.create_line(coord11, fill="yellow", width=2)     # plate
canvas1.create_line(coord12, fill="yellow", width=2)     # plate
canvas1.create_line(coord13, fill="yellow", width=2)     # plate
canvas1.create_line(coord14, fill="yellow", width=2)     # plate
canvas1.create_line(coord15, fill="yellow", width=2)     # plate
canvas1.create_line(coord16, fill="yellow", width=2)     # plate
canvas1.create_line(coord17, fill="yellow", width=2)     # plate
canvas1.create_line(coord18, fill="yellow", width=2)     # plate
canvas1.create_line(coord19, fill="yellow", width=2)     # plate
canvas1.create_line(coord20, fill="yellow", width=2)     # plate
canvas1.create_line(coord21, fill="yellow", width=2)     # plate
canvas1.create_line(coord22, fill="yellow", width=2)     # plate
canvas1.create_line(coord23, fill="yellow", width=2)     # plate
canvas1.create_line(coord24, fill="yellow", width=2)     # plate
canvas1.create_line(coord25, fill="yellow", width=2)     # plate
canvas1.create_line(coord26, fill="yellow", width=2)     # plate
canvas1.create_line(coord27, fill="yellow", width=2)     # plate
canvas1.create_line(coord28, fill="yellow", width=2)     # plate
canvas1.create_line(coord29, fill="yellow", width=2)     # plate
canvas1.create_line(coord30, fill="yellow", width=2)     # plate
canvas1.create_line(coord31, fill="yellow", width=2)     # plate
canvas1.create_line(coord32, fill="yellow", width=2)     # plate
canvas1.create_line(coord33, fill="yellow", width=2)     # plate
canvas1.create_line(coord34, fill="yellow", width=2)     # plate
canvas1.create_line(coord35, fill="yellow", width=2)     # plate
canvas1.create_line(coord, fill="red", width=2)     # plate
canvas1.place(x=0, y=80)

coord = 70, 180, 120, 180
coord1 = 115, 170, 120, 180, 115, 190
coord2 = 55, 195
canvas1.create_text(coord2, text="               x", fill="red", font="bold")
canvas1.create_line(coord, coord1, fill="black", width=1)  # x-axis

# Enter the values
C2 = tkinter.Canvas(root, width=550, height=350, bg="white")
C2.place(x=801, y=75)
label1 = Label(root, text="Fluid:", font="times 14 bold italic", bg="white", fg="Maroon")
label1.place(x=70, y=95)  # Fluid label
tkvar1 = StringVar(root)
choice1 = {'Air', 'CO2', 'Diesel Fuel', 'Engine Oil 5w30', 'Ethylene Glycol', 'Ethylene Glycol 30%',
           'Ethylene Glycol 50%', 'Exxon 2389 (jet engine oil)', 'Freon 114', 'Gasoline', 'Kerosene', 'Marlotherm S',
           'Transmission Oil (Type-B)', 'Transmission Oil (Type-F)', 'Transmission Oil (Type-H)', 'Water'}
tkvar1.set('Air')
popupMenu1 = OptionMenu(root, tkvar1, *choice1)
popupMenu1.place(x=170, y=95)

label2 = Label(root, text="Incoming velocity, u(m/s):", font="times 14 bold italic", bg="white", fg="Maroon")
label2.place(x=70, y=135)
e1 = Entry(root, bd=5, highlightcolor="blue", width=8)  # Velocity label
e1.place(x=300, y=135)

label3 = Label(root, text="Incoming fluid temp, T∞ (°C):", font="times 14 bold italic", bg="white", fg="Maroon")
label3.place(x=70, y=175)
e2 = Entry(root, bd=5, highlightcolor="blue", width=8)  # Temperature
e2.place(x=320, y=175)

# plate dimensions
l3 = Label(root, text="Enter plate length, L(m):", font="times 14 bold italic", bg="white", fg="Maroon")
l3.place(x=390, y=95)
e3 = Entry(root, bd=5, width=7, highlightcolor="blue")
e3.place(x=650, y=95)
l4 = Label(root, text="Enter Heat Transfer rate, Q(W):", font="times 14 bold italic", bg="white", fg="Maroon")
l4.place(x=390, y=135)
e4 = Entry(root, bd=5, width=7, highlightcolor="blue")
e4.place(x=650, y=135)
l40 = Label(root, text="Plate width, w(m): ", font="times 14 bold italic", bg="white", fg="Maroon")
l40.place(x=390, y=175)
e5 = Entry(root, bd=5, width=7)
e5.place(x=650, y=175)

# Fluid properties
l1 = Label(root, text="Fluid Properties and Dimensionless Numbers", bg="white", fg="black", font="times 15 bold")
l1.place(x=810, y=80)
label4 = Label(root, text="Density, ρ(kg/m³):", bg="white", fg="maroon", font="times 15 bold")
label4.place(x=810, y=120)

label5 = Label(root, text="Dynamic viscosity, μ(kg/ms):", bg="white", fg="maroon", font="times 15 bold")
label5.place(x=810, y=160)

label6 = Label(root, text="Specific heat, Cp(J/kg.K):", bg="white", fg="maroon", font="times 15 bold")
label6.place(x=810, y=200)

label7 = Label(root, text="Thermal conductivity, k(W/mK):", bg="white", fg="maroon", font="times 15 bold")
label7.place(x=810, y=240)

label8 = Label(root, text="Kinematic viscosity, v(m²/s):", bg="white", fg="maroon", font="times 15 bold")
label8.place(x=810, y=280)

label9 = Label(root, text="Prandtl Number, Pr:", bg="white", fg="maroon", font="times 15 bold")
label9.place(x=810, y=320)
label10 = Label(root, text="Re_x:", bg="white", fg="maroon", font="times 15 bold")
label10.place(x=810, y=360)

arr= []
arr1= array.array('f')


def solve():
    incoming_velocity = float(e1.get())
    fluid_temp = float(e7.get())
    flat_plate_temp = float(e2.get())
    T_film = float(( fluid_temp+ flat_plate_temp)/2)
    x=float(e6.get())
    Label(root, height=1, width=20, bg="white").place(x=600, y=420)
    l5 = Label(root, text="For the given conditions, T_film(°C):", bg="white", fg="maroon", font="times 14")
    l5.place(x=250, y=420)
    l6 = Label(root, text=round(T_film,3), fg="red", font="times 14 bold", bg="white")
    l6.place(x=600, y=420)
    arr.append(fluid_temp)
    Label(root,bg="white",height=50,width=1000).place(x=470,y=440)
    ts = round(float(float(e4.get())/(float(e3.get())*float(e5.get()))), 3)
    Label(root, text=ts, fg="red", font="times 14 bold", bg="white").place(x=745, y=280)
    def retx():

        xc = float((5 * pow(10, 5) * dynamic_vis) / float(e1.get()))
        if xc > x:

            cord=185,160,185,200
            canvas1.create_line(cord,fill="green",width=3)

            cord2=780,160,780,200
            canvas1.create_line(cord2, fill="green", width=3)
            cord3 = 720, 160
            Label(canvas1,text="xcr(m)=",bg="white").place(x=680,y=150)
            Label(canvas1,height=1,width=10, bg="white").place(x=740, y=150)
            Label(canvas1,text=round(xc,3),bg="white").place(x=740,y=150)
            cord5 = 210, 160
            Label(canvas1,text="x(m)=",bg="white").place(x=194,y=150)
            Label(canvas1, height=1, width=5, bg="white").place(x=234, y=140)
            Label(canvas1, text=x, bg="white").place(x=234, y=150)




        else:
            cord = 355, 160, 355, 200
            canvas1.create_line(cord, fill="green", width=3)
            cord2 = 100, 160, 100, 200
            canvas1.create_line(cord2, fill="green", width=3)
            cord3=130,160
            Label(canvas1,text="xcr(m)=",bg="white").place(x=108,y=150)
            Label(canvas1, height=1, width=20, bg="white").place(x=154, y=150)
            Label(canvas1,text=round(xc,3),bg="white").place(x=154,y=150)
            cord5 = 380, 160
            Label(canvas1,text="x(m)=",bg="white").place(x=354,y=150)
            cord6 = 394, 160
            Label(canvas1, height=1, width=30, bg="white").place(x=394, y=150)
            Label(canvas1,text=round(x,3),bg="white").place(x=394,y=150)


        if rex<5*pow(10,5) :
            nu=(0.453*pow(rex,1/2)*pow(prno,1/3))
            h=((nu)*th_cond)/x
            heatflux=ts
            newt=(heatflux/h)+flat_plate_temp
            Label(root, height=1, width=150, bg="white").place(x=350, y=540)
            Label(root, height=1, width=150, bg="white").place(x=350, y=560)
            Label(root, height=1, width=150, bg="white").place(x=350, y=580)
            l46 = Label(root, text=round(nu,3), bg="white", fg="red",font="times 12 bold")
            l46.place(x=350, y=544)
            l47 = Label(root, text=round(h,3), bg="white", fg="red", font="times 12 bold")
            l47.place(x=350, y=568)
            l48 = Label(root, text=round(newt,3), bg="white", fg="red", font="times 12 bold")
            l48.place(x=350, y=592)
            l42 = Label(root, text="Since Re_x<5 X 10⁵, Laminar flow exists at chosen x location", bg="white", fg="black", font="times 12 bold")
            l42.place(x=10, y=520)
            l43 = Label(root, text="Nu_x=(0.453)(√Re_x)(3√pr)", bg="white", fg="black",font="times 12 bold")
            l43.place(x=10, y=544)
            l44 = Label(root, text="h_x=(Nu_x)(k)/x", bg="white", fg="black", font="times 12 bold")
            l44.place(x=10, y=568)
            l45 = Label(root, text="Ts_x, calculated (°C)= (q''/h_x)+T∞", bg="white", fg="black", font="times 12 bold")
            l45.place(x=10, y=592)


        else:
            nu = (0.0308 * pow(rex, 4 / 5) * pow(prno, 1 / 3))
            h = ((nu) * th_cond) / x
            heatflux = ts
            newt = (heatflux / h) + flat_plate_temp
            Label(root, height=1, width=150, bg="white").place(x=350, y=544)
            Label(root, height=1, width=150, bg="white").place(x=350, y=568)
            Label(root, height=1, width=150, bg="white").place(x=350, y=592)
            l46 = Label(root, text=round(nu,3), bg="white", fg="red", font="times 12 bold")
            l46.place(x=350, y=544)
            l47 = Label(root, text=round(h,3), bg="white", fg="red", font="times 12 bold")
            l47.place(x=350, y=568)
            l48 = Label(root, text=round(newt,3), bg="white", fg="red", font="times 12 bold")
            l48.place(x=350, y=592)
            l42 = Label(root, text="Since Re_x>5 X 10⁵,Turbulent flow exists at chosen x location ", bg="white", fg="black",font="times 12 bold")
            l42.place(x=10, y=520)
            l43 = Label(root, text="Nu_x=(0.0308)(Re_x⁴/⁵)(3√pr)", bg="white", fg="black", font="times 12 bold")
            l43.place(x=10, y=544)
            l44 = Label(root, text="h_x=(Nu_x)(k)/x", bg="white", fg="black", font="times 12 bold")
            l44.place(x=10, y=568)
            l45 = Label(root, text="Ts_x, calculated (°C)= (q''/h_x)+T∞", bg="white", fg="black", font="times 12 bold")
            l45.place(x=10, y=592)

        if (newt - fluid_temp)/(newt)<0.05:
            def solve1():
                y = float(e3.get())
                rel = float((density * y * float(e1.get())) / dynamic_vis)
                if rex < (5 * pow(10, 5)):
                    vt = (5 * x) / pow(rex, 1 / 2)
                    tt = (5 * x) / (pow(rex, 1 / 2) * pow(prno, 1 / 3))
                    sc = 0.664 / (pow(rex, 1 / 2))
                    st= (sc*density*float(e1.get())*float(e1.get()))/2
                    Label(root, text=" Local Parameters", bg="white", fg="green",
                          font="times 12 bold italic underline ").place(x=500, y=500)
                    l100 = Label(root, text="δ_x(m)  =", bg="white", fg="blue",
                                 font="times 12 bold")
                    l100.place(x=500, y=540)

                    Label(root, text="δt_x(m)  =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=564)
                    Label(root, text="Cdf_x    =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=588)
                    Label(root, text="h_x(W/m²K)      =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=636)
                    Label(root, text="Nu_x     =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=612)
                    Label(root, text="τ_sx(W/m²)     =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=660)
                    Label(root, text=round(vt, 3), bg="white", fg="red", font="times 12 bold").place(x=600, y=540)
                    Label(root, text=round(tt, 3), bg="white", fg="red", font="times 12 bold").place(x=600, y=564)
                    Label(root, text=round(sc, 3), bg="white", fg="red", font="times 12 bold").place(x=600, y=588)
                    Label(root, text=round(nu, 3), bg="white", fg="red", font="times 12 bold").place(x=600, y=612)
                    Label(root, text=round(h, 3), bg="white", fg="red", font="times 12 bold").place(x=630, y=636)
                    Label(root, text=round(st, 3), bg="white", fg="red", font="times 12 bold").place(x=630, y=660)








                else:

                    vt = (0.37 * x) / pow(rex, 1 / 5)
                    tt = (0.37 * x) / (pow(rex, 1 / 5) * pow(prno, 1 / 3))
                    sc = 0.0592 / (pow(rex, 1 / 5))
                    st = (sc * density * float(e1.get()) * float(e1.get())) / 2
                    Label(root, text=" Local Parameters", bg="white", fg="green",font="times 12 bold italic underline ").place(x=500, y=500)
                    Label(root, text="δ_x(m)   =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=540)
                    Label(root, text="δt_x(m)  =", bg="white",fg="blue", font="times 12 bold").place(x=500, y=564)
                    Label(root, text="Cdf_x    =", bg="white", fg="blue",font="times 12 bold").place(x=500, y=588)
                    Label(root, text="h_x(W/m²K)      =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=636)
                    Label(root, text="Nu_x     =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=612)
                    Label(root, text="τ_sx(W/m²)     =", bg="white", fg="blue", font="times 12 bold").place(x=500, y=660)
                    Label(root, text=round(vt,3), bg="white", fg="red", font="times 12 bold").place(x=600, y=540)
                    Label(root, text=round(tt,3), bg="white", fg="red", font="times 12 bold").place(x=600, y=564)
                    Label(root, text=round(sc,3), bg="white", fg="red", font="times 12 bold").place(x=600, y=588)
                    Label(root, text=round(nu, 3), bg="white", fg="red", font="times 12 bold").place(x=600, y=612)
                    Label(root, text=round(h, 3), bg="white", fg="red", font="times 12 bold").place(x=630, y=636)
                    Label(root, text=round(st, 3), bg="white", fg="red", font="times 12 bold").place(x=630, y=660)



                if rel<(5 * pow(10, 5)):
                    c=0.453
                    vt1 = (5 * y) / pow(rel, 1 / 2)
                    tt2 = (5 * y) / (pow(rel, 1 / 2) * pow(prno, 1 / 3))
                    sc2 = 0.664 / (pow(rel, 1 / 2))

                    h2 = (th_cond*c)/float(e3.get())*2*pow(prno, 1 / 3)*pow(rel, 1 / 2)
                    nul = (h2*float(e3.get())/th_cond)
                    tav=flat_plate_temp+(2/3)*(ts/h2)

                    st2 = (sc2 * density * float(e1.get()) * float(e1.get())) / 2
                    Label(root, text=" Average Parameters", bg="white", fg="green",font="times 12 bold italic underline ").place(x=700, y=500)
                    l101 = Label(root, text="δ_L(m)  =", bg="white", fg="blue",font="times 12 bold")
                    l101.place(x=700, y=540)

                    Label(root, text="δt_L(m)  =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=564)
                    Label(root, text="Cdf_average    =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=588)
                    Label(root, text="h_average(W/m²K)   =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=636)
                    Label(root, text="Nu_average    =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=612)
                    Label(root, text="τs_average(W/m²)   =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=660)
                    Label(root, text=round(vt1, 3), bg="white", fg="red", font="times 12 bold").place(x=800, y=540)
                    Label(root, text=round(tt2, 3), bg="white", fg="red", font="times 12 bold").place(x=800, y=564)
                    Label(root, text=round(sc2, 3), bg="white", fg="red", font="times 12 bold").place(x=840, y=588)
                    Label(root, text=round(nul, 3), bg="white", fg="red", font="times 12 bold").place(x=820, y=612)
                    Label(root, text=round(h2, 3), bg="white", fg="red", font="times 12 bold").place(x=850, y=636)
                    Label(root, text=round(st2, 3), bg="white", fg="red", font="times 12 bold").place(x=850, y=660)
                    Label(root, text="Ts_avg(°C) =", bg="white", fg="blue", font="times 12 bold").place(x=900, y=574)
                    Label(root, text=round(tav, 3), bg="white", fg="red", font="times 12 bold").place(x=1000, y=574)

                else:
                    c=0.030
                    vt1 = (0.37 * y) / pow(rel, 1 / 5)
                    tt2 = (0.37 * y) / (pow(rel, 1 / 5) * pow(prno, 1 / 3))
                    sc2 = (0.074 / (pow(rel, 1 / 5))) - (1742 / rel)
                    h2 = (th_cond * c) / float(e3.get()) * (5/4) * pow(prno, 3 / 5) * pow(rel, 4 / 5)
                    nul = (h2 * float(e3.get()) / th_cond)
                    tav = flat_plate_temp + (5/6 ) * (ts / h2)
                    st2 = (sc2 * density * float(e1.get()) * float(e1.get())) / 2

                    Label(root, text=" Average Parameters", bg="white", fg="green",font="times 12 bold italic underline ").place(x=700, y=500)
                    l101 = Label(root, text="δ_L(m)  =", bg="white", fg="blue",font="times 12 bold")
                    l101.place(x=700, y=540)

                    Label(root, text="δt_L(m)  =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=564)
                    Label(root, text="Cdf_average    =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=588)
                    Label(root, text="h_average(W/m²K)   =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=636)
                    Label(root, text="Nu_average   =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=612)
                    Label(root, text="τs_average(W/m²)   =", bg="white", fg="blue", font="times 12 bold").place(x=700, y=660)
                    Label(root, text=round(vt1, 3), bg="white", fg="red", font="times 12 bold").place(x=800, y=540)
                    Label(root, text=round(tt2, 3), bg="white", fg="red", font="times 12 bold").place(x=800, y=564)
                    Label(root, text=round(sc2, 3), bg="white", fg="red", font="times 12 bold").place(x=840, y=588)
                    Label(root, text=round(nul, 3), bg="white", fg="red", font="times 12 bold").place(x=820, y=612)
                    Label(root, text=round(h2, 3), bg="white", fg="red", font="times 12 bold").place(x=850, y=636)
                    Label(root, text=round(st2, 3), bg="white", fg="red", font="times 12 bold").place(x=850, y=660)
                    Label(root, text="Ts_avg(°C) =", bg="white", fg="blue", font="times 12 bold").place(x=900, y=574)
                    Label(root, text=round(tav, 3), bg="white", fg="red", font="times 12 bold").place(x=1000, y=574)




            def solve2():
                for i in range(0, 10):
                    Label(root, text=round(arr[i],3), bg="white", fg="Blue", font="times 12 bold italic").place(x=1220,
                                                                                                      y=490 + (i * 20))
                    Label(root,text="Ts_x assumed ",bg="white", fg="Black", font="times 12 bold italic").place(x=1100,y=490+(i*20))
                    Label(root, text=i+1, bg="white", fg="Blue", font="times 12 bold italic").place(x=1200,y=490 +(i * 20))

            ta=(newt+fluid_temp)/2


            Label(root,text="Since Ts_x assumed and Ts_x calculated are quite close,\nIt can be said that T(x)=",bg="white", fg="black", font="times 13 bold italic").place(x=10,y=630)
            Label(root,text=round(ta,3),bg="white", fg="red", font="times 12 bold italic").place(x=300,y=650)
            opm = Button(root, text="Calculate Local and Average Parameters",command=solve1)
            opm.place(x=520, y=470)
            pp = Button(root, text="See iterations of Ts_x", command=solve2)
            pp.place(x=1200, y=440)
        else:
            ta = (newt + fluid_temp) / 2

            Label(root, text="Your assumed value Ts_x,assumed is not accurate You need to \n  iterate once more for Ts_x assumed:" ,bg="white", fg="black", font="times 11 bold italic").place(x=10, y=630)
            Label(root, text=round(ta,3), bg="white", fg="red", font="times 11 bold italic").place(x=340, y=650)


    if tkvar1.get() == 'Air':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = (6.81368+(-0.51573)*(T_film+273)**0.5+(0.0109321)*(T_film+273))
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)

        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis= ((0.00625687+(0.00153069*(T_film+273)**0.5)+(-0.0000210769*(T_film+273)))**3)
        blablel = Label(root, height=2, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = (297.303+(126.386)*(T_film+273)**0.5+(-7.54029*(T_film+273)+0.150637*(T_film+273)**(3/2)))
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = (-0.00719331+(0.00118869)*(T_film+273)**0.5+(0.000042988)*(T_film+273))
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis/density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis*Sp_heat/th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'CO2':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 9.08765+(-0.638091*(T_film+273)**0.5)+(0.0124355)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)

        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (0.00818801+(0.00109054*(T_film+273)**0.5)+(-0.00000821403*(T_film+273)))**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 22.0999+(59.6828)*(T_film+273)**0.5+(-0.678364)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = -0.00202595+(-0.000485225)*(T_film+273)**0.5+(0.0000905949)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel= Label(root, height=1, width=50,bg="white")
        clablel.place(x=1100,y=360)
        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Diesel Fuel':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1038.73+(0.9223)*(T_film+273)**0.5+(-0.726)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (4.86287+(-0.640153*(T_film+273)**0.5)+0.0286278*(T_film+273)+(-0.000429409*(T_film+273)**(3/2)))**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 1072.18+(-27.4671)*(T_film + 273)**0.5+(4.44)*(T_film + 273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.1586+(0.00007133)*(T_film+273)**0.5+(-0.00007693)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Engine Oil 5w30':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1021.18+(4.2243)*(T_film+273)**0.5+(-0.703867)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = 10**(9274+(-2437.83*(T_film+273)**0.5)+256.145*(T_film+273)+(-13.4449*(T_film+273)**(3/2))+0.352491*(T_film+273)**2+(-0.00369285)*(T_film+273)**(5/2))
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 1286.63+(-71.4665)*(T_film+273)**0.5+(6.20997)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.183482+(-0.00123141)*(T_film+273)**0.5+(-0.0000613542)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)

        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)

        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Ethylene Glycol':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1457.87+(-15.91)*(T_film+273)**0.5+(-0.238222)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (716.119+(-154.425*(T_film+273)**0.5)+12.5104*(T_film+273)+(-0.451017)*(T_film+273)**(3/2)+0.00610317*(T_film+273)**2)**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 1159.23+(-8.2399)*(T_film+273)**0.5+(4.66769)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = -0.797513+(0.110425)*(T_film+273)**0.5+(-0.00287622)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Ethylene Glycol 30%':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 600.115+(68.6483)*(T_film+273)**0.5+(-2.51702)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (107.562+(-22.4664*(T_film+273)**0.5)+1.76552*(T_film+273)+(-0.0617784)*(T_film+273)**(3/2)+0.000811582*(T_film+273)**2)**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 1047.43+(202.095)*(T_film+273)**0.5+(-2.7069)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = -1.56126+(0.2163377)*(T_film+273)**0.5+(-0.0056602)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Ethylene Glycol 50%':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1416.3+(-22.2397)*(T_film+273)**0.5+(0.0703129)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (3.23858+(-0.310287*(T_film+273)**0.5)+(0.00761038*(T_film+273)))**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 4302.06+(-186.873)*(T_film+273)**0.5+(7.45367)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = -1.12878+(0.151667)*(T_film+273)**0.5+(-0.0035556)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = (float(dynamic_vis / density))
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Exxon 2389 (jet engine oil)':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1101+(7.673)*(T_film+273)**0.5+(-0.8996)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = 10**(37.154+(-3.89514*(T_film+273)**0.5)+(0.095177*(T_film+273)))
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = -336.62+(120.68)*(T_film+273)**0.5+(0.194)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.111+(0.00758)*(T_film+273)**0.5+(-0.000313)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = (float(dynamic_vis / density))
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)

        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Freon 114':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = -11367.9+(1577.84)*(T_film+273)**0.5+(-48.239)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (0.49+(-0.03867*(T_film+273)**0.5)+(0.0008361*(T_film+273)))**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 525.713+(-25.7344)*(T_film+273)**0.5+(3.11947)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.174+(-0.003758)*(T_film+273)**0.5+(-0.0001506)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = (float(dynamic_vis / density))
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Gasoline':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1466.47+(-46.3569)*(T_film + 273)**0.5+(0.282203)*(T_film + 273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (0.565766+(-0.0438361*(T_film + 273)**0.5)+(0.000929345*(T_film + 273)))**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 565.232+(16.4843)*(T_film + 273)**0.5+(4.07038)*(T_film + 273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.241233+(-0.00264178)*(T_film + 273)**0.5+(-0.0000350195)*(T_film + 273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Kerosene':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = float(1170.02+(-11.55011)*(T_film+273)**0.5+(-0.31374)*(T_film+273))
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = float((4.86287+(-0.640153*(T_film+273)**0.5)+0.0286278*(T_film+273)+(-0.000429409*(T_film+273)**(3/2)))**3)
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = float(-510.371+(134.076)*(T_film+273)**0.5+(0.649226)*(T_film+273))
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = float(0.197182+(0.0000801211)*(T_film+273)**0.5+(-0.0000955805)*(T_film+273))
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Marlotherm S':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1267.82+(-3.59809)*(T_film+273)**0.5+(-0.605724)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (250.537+(-46.9296*(T_film+273)**0.5)+3.28642*(T_film+273)+(-0.101907)*(T_film+273)**(3/2)+0.00118036*(T_film+273)**2)**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 86.6947+(44.7617)*(T_film+273)**0.5+(2.43846)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.186325+(-0.00252274)*(T_film+273)**0.5+(-0.0000407022)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Transmission Oil (Type-B)':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1159.7+(-11.0605)*(T_film+273)**0.5+(-0.359005)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = 10**(128.959+(-18.4209*(T_film+273)**0.5)+(0.868622*(T_film+273))+(-0.0137992*(T_film+273)**(3/2)))
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 237.467+(66.7114)*(T_film+273)**0.5+(1.73041)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.178947+(-0.00267278)*(T_film+273)**0.5+(-0.0000065788)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Transmission Oil (Type-F)':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1159.7+(-11.0605)*(T_film+273)**0.5+(-0.359005)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = 10**(2507.74+(-511.658*(T_film+273)**0.5)+39.1611*(T_film+273)+(-1.33299*(T_film+273)**(3/2))+0.0170163*(T_film+273)**2)
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 237.467+(66.7114)*(T_film+273)**0.5+(1.73041)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.178947+(-0.00267278)*(T_film+273)**0.5+(-0.0000065788)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Transmission Oil (Type-H)':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = 1159.7+(-11.0605)*(T_film+273)**0.5+(-0.359005)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = 10**(198.598+(-29.6011*(T_film+273)**0.5)+(1.46836*(T_film+273))+(-0.0245473*(T_film+273)**(3/2)))
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 237.467+(66.7114)*(T_film+273)**0.5+(1.73041)*(T_film+273)
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = 0.178947+(-0.00267278)*(T_film+273)**0.5+(-0.0000065788)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()
    if tkvar1.get() == 'Water':
        zlablel = Label(root, height=1, width=50, bg="white")
        zlablel.place(x=1100, y=200)
        xlablel = Label(root, height=1, width=50, bg="white")
        xlablel.place(x=1100, y=240)
        tlablel = Label(root, height=1, width=50, bg="white")
        tlablel.place(x=1100, y=280)
        rlablel = Label(root, height=1, width=50, bg="white")
        rlablel.place(x=1100, y=320)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        density = -342.584+(164.103)*(T_film+273)**0.5+(-5.01225)*(T_film+273)
        nlablel = Label(root, height=1, width=50, bg="white")
        nlablel.place(x=1100, y=120)
        dlabel = Label(root, text=round(density, 3), fg="red", bg="white", font="times 15 bold")
        dlabel.place(x=1100, y=120)

        dynamic_vis = (31.6371+(-6.37804*(T_film+273)**0.5)+0.485827*(T_film+273)+(-0.016519)*(T_film+273)**(3/2)+0.000211278*(T_film+273)**2)**3
        blablel = Label(root, height=1, width=50, bg="white")
        blablel.place(x=1100, y=160)
        dvlabel = Label(root, text=round(dynamic_vis, 5), fg="red", bg="white", font="times 15 bold")
        dvlabel.place(x=1100, y=160)

        Sp_heat = 3805070+(-1028080)*(T_film+273)**0.5+(111160)*(T_film+273)+(-6005.26*(T_film+273)**(3/2))+162.081*(T_film+273)**2+(-1.7482*(T_film+273)**(5/2))
        splabel = Label(root, text=round(Sp_heat, 3), fg="red", bg="white", font="times 15 bold")
        splabel.place(x=1100, y=200)

        th_cond = -2.76131+(0.340118)*(T_film+273)**0.5+(-0.00838245)*(T_film+273)
        thlabel = Label(root, text=round(th_cond, 3), fg="red", bg="white", font="times 15 bold")
        thlabel.place(x=1105, y=240)

        k_vis = float(dynamic_vis / density)
        kvilabel = Label(root, text=round(k_vis, 5), fg="red", bg="white", font="times 15 bold")
        kvilabel.place(x=1100, y=280)

        prno = float(dynamic_vis * Sp_heat / th_cond)
        prlabel = Label(root, text=round(prno, 3), fg="red", bg="white", font="times 15 bold")
        prlabel.place(x=1100, y=320)

        rex = float((density * x * float(e1.get())) / dynamic_vis)
        clablel = Label(root, height=1, width=50, bg="white")
        clablel.place(x=1100, y=360)

        rexlabel = Label(root, text=round(rex, 3), fg="red", bg="white", font="times 15 bold")
        rexlabel.place(x=1100, y=360)
        retx()


l6 = Label(root, text="Enter Value of x(m):", font="times 12 bold italic", bg="white", fg="red")
l6.place(x=10, y=340)
e6 = Entry(root, bd=5, highlightcolor="blue", width=8)
e6.place(x=250, y=340)

l8 = Label(root, text="First , We need to estimate film temperature to calculate fluid properties and proceed with the "
                      "calculations \nTo begin with let's put Ts = T∞", font="times 12 bold italic", bg="white", fg="green")
l8.place(x=10, y=370)
l7 = Label(root, text="Ts_x, assumed(°C):", font="times 12 bold italic", bg="white", fg="red")
l7.place(x=10, y=400)
e7 = Entry(root, bd=5, highlightcolor="blue", width=8)
e7.place(x=140, y=400)
l9 = Label(root, text="q''(W/m²):", font="times 12 bold italic", bg="white", fg="red")
l9.place(x=670, y=280)

def solve6():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    Label(root, bg="white", height=50, width=1000).place(x=470, y=440)
    del arr[:]

    cord = 355, 160, 355, 200
    canvas1.create_line(cord, fill="white", width=3)
    cord2 = 100, 160, 100, 200
    canvas1.create_line(cord2, fill="white", width=3)
    cord = 185, 160, 185, 200
    canvas1.create_line(cord, fill="white", width=3)

    cord2 = 780, 160, 780, 200
    canvas1.create_line(cord2, fill="white", width=3)

    Label(canvas1, height=1, width=100, bg="white").place(x=108, y=150)
    # Arrows
    coord = 0, 10, 50, 10
    coord1 = 45, 0, 50, 10, 45, 20
    canvas1.create_line(coord, coord1, fill="blue", width=1.5)  # first arrow

    coord = 0, 50, 50, 50
    coord1 = 45, 40, 50, 50, 45, 60
    canvas1.create_line(coord, coord1, fill="blue", width=1.5)  # second arrow

    coord = 0, 90, 50, 90
    coord1 = 45, 80, 50, 90, 45, 100
    canvas1.create_line(coord, coord1, fill="blue", width=1.5)  # third arrow

    coord = 0, 130, 50, 130
    coord1 = 45, 120, 50, 130, 45, 140
    canvas1.create_line(coord, coord1, fill="blue", width=1.5)  # fourth arrow

    coord = 0, 170, 50, 170
    coord1 = 45, 160, 50, 170, 45, 180
    canvas1.create_line(coord, coord1, fill="blue", width=1.5)  # fifth arrow

    coord = 65, 140, 70, 130, 75, 140
    coord1 = 70, 130, 70, 180
    coord2 = 80, 155
    canvas1.create_text(coord2, text="       y", font="bold", fill="red")  # Y-axis
    canvas1.create_line(coord, coord1, fill="black", width=1.5)

    coord = 70, 180, 750, 180
    coord2 = 65, 180, 75, 190
    coord3 = 85, 180, 95, 190
    coord4 = 105, 180, 115, 190
    coord5 = 125, 180, 135, 190
    coord6 = 145, 180, 155, 190
    coord7 = 165, 180, 175, 190
    coord8 = 185, 180, 195, 190
    coord9 = 205, 180, 215, 190
    coord10 = 225, 180, 235, 190
    coord11 = 245, 180, 255, 190
    coord12 = 265, 180, 275, 190
    coord13 = 285, 180, 295, 190
    coord14 = 305, 180, 315, 190
    coord15 = 325, 180, 335, 190
    coord16 = 345, 180, 355, 190
    coord17 = 365, 180, 375, 190
    coord18 = 385, 180, 395, 190
    coord19 = 405, 180, 415, 190
    coord20 = 425, 180, 435, 190
    coord21 = 445, 180, 455, 190
    coord22 = 465, 180, 475, 190
    coord23 = 485, 180, 495, 190
    coord24 = 505, 180, 515, 190
    coord25 = 525, 180, 535, 190
    coord26 = 545, 180, 555, 190
    coord27 = 565, 180, 575, 190
    coord28 = 585, 180, 595, 190
    coord29 = 605, 180, 615, 190
    coord30 = 625, 180, 635, 190
    coord31 = 645, 180, 655, 190
    coord32 = 665, 180, 675, 190
    coord33 = 685, 180, 695, 190
    coord34 = 705, 180, 715, 190
    coord35 = 725, 180, 735, 190
    canvas1.create_line(coord2, fill="yellow", width=2)  # plate
    canvas1.create_line(coord3, fill="yellow", width=2)  # plate
    canvas1.create_line(coord4, fill="yellow", width=2)  # plate
    canvas1.create_line(coord5, fill="yellow", width=2)  # plate
    canvas1.create_line(coord6, fill="yellow", width=2)  # plate
    canvas1.create_line(coord7, fill="yellow", width=2)  # plate
    canvas1.create_line(coord8, fill="yellow", width=2)  # plate
    canvas1.create_line(coord9, fill="yellow", width=2)  # plate
    canvas1.create_line(coord10, fill="yellow", width=2)  # plate
    canvas1.create_line(coord11, fill="yellow", width=2)  # plate
    canvas1.create_line(coord12, fill="yellow", width=2)  # plate
    canvas1.create_line(coord13, fill="yellow", width=2)  # plate
    canvas1.create_line(coord14, fill="yellow", width=2)  # plate
    canvas1.create_line(coord15, fill="yellow", width=2)  # plate
    canvas1.create_line(coord16, fill="yellow", width=2)  # plate
    canvas1.create_line(coord17, fill="yellow", width=2)  # plate
    canvas1.create_line(coord18, fill="yellow", width=2)  # plate
    canvas1.create_line(coord19, fill="yellow", width=2)  # plate
    canvas1.create_line(coord20, fill="yellow", width=2)  # plate
    canvas1.create_line(coord21, fill="yellow", width=2)  # plate
    canvas1.create_line(coord22, fill="yellow", width=2)  # plate
    canvas1.create_line(coord23, fill="yellow", width=2)  # plate
    canvas1.create_line(coord24, fill="yellow", width=2)  # plate
    canvas1.create_line(coord25, fill="yellow", width=2)  # plate
    canvas1.create_line(coord26, fill="yellow", width=2)  # plate
    canvas1.create_line(coord27, fill="yellow", width=2)  # plate
    canvas1.create_line(coord28, fill="yellow", width=2)  # plate
    canvas1.create_line(coord29, fill="yellow", width=2)  # plate
    canvas1.create_line(coord30, fill="yellow", width=2)  # plate
    canvas1.create_line(coord31, fill="yellow", width=2)  # plate
    canvas1.create_line(coord32, fill="yellow", width=2)  # plate
    canvas1.create_line(coord33, fill="yellow", width=2)  # plate
    canvas1.create_line(coord34, fill="yellow", width=2)  # plate
    canvas1.create_line(coord35, fill="yellow", width=2)  # plate
    canvas1.create_line(coord, fill="red", width=2)  # plate
    canvas1.place(x=0, y=80)

    coord = 70, 180, 120, 180
    coord1 = 115, 170, 120, 180, 115, 190
    coord2 = 55, 195
    canvas1.create_text(coord2, text="               x", fill="red", font="bold")
    canvas1.create_line(coord, coord1, fill="black", width=1)  # x-axis

    clablel = Label(root, height=1, width=50, bg="white")
    clablel.place(x=1100, y=360)
    zlablel = Label(root, height=1, width=50, bg="white")
    zlablel.place(x=1100, y=200)
    xlablel = Label(root, height=1, width=50, bg="white")
    xlablel.place(x=1100, y=240)
    tlablel = Label(root, height=1, width=50, bg="white")
    tlablel.place(x=1100, y=280)
    rlablel = Label(root, height=1, width=50, bg="white")
    rlablel.place(x=1100, y=320)
    nlablel = Label(root, height=1, width=50, bg="white")
    nlablel.place(x=1100, y=120)
    blablel = Label(root, height=1, width=50, bg="white")
    blablel.place(x=1100, y=160)
    l60 = Label(root, height=1, width=20, bg="white")
    l60.place(x=600, y=420)



# Button
b = Button(root, text="Calculate Fluid properties", command=solve)
b.place(x=90, y=470)
gg= Button(root, text="Reset", command=solve6)
gg.place(x=400, y=470)
root.mainloop()