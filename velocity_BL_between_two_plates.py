import tkinter as tk
from tkinter import *
import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt

mainWindow = tk.Tk()
mainWindow.geometry('1590x1450')
mainWindow.title("Boundary Layer Growth between two Parallel Plates")
mainWindow.configure(background="white")
tkVar1 = StringVar(mainWindow)
y=[]
x=[]
h=[]
Reₓ1=[]

label1 = tk.Label(mainWindow, text="Boundary Layer Growth between two Parallel Plates", fg="red", bg="white", font="times 20 bold")
label1.pack()

label2 = tk.Label(mainWindow, text="Distance between Plates, H(cm):", bg="white", font="times 12 bold")
label2.place(x=10,y=50)

scroll1 = Scale(mainWindow, from_=0, to=50, resolution=1, orient=HORIZONTAL, activebackground="black", length="250")
scroll1.place(x=30,y=75)

label3 = tk.Label(mainWindow, text="Inlet Fluid Velocity, u(m/s):", bg="white", font="times 12 bold")
label3.place(x=10,y=115)

scroll2 = Scale(mainWindow, from_=0, to=100, resolution=1, orient=HORIZONTAL, activebackground="black", length="250")
scroll2.place(x=30,y=140)

label4 = tk.Label(mainWindow, text="Choose a Fluid:", bg="white", font="times 12 bold")
label4.place(x=280,y=50)

choice1 = {'Air', 'CO₂', 'Diesel Fuel', 'Engine Oil 5w30', 'Ethylene Glycol', 'Ethylene Glycol 30%',
            'Ethylene Glycol 50%', 'Exxon 2389(Jet Engine Fuel)','Freon 114', 'Gasoline', 'Kerosene', 
            'Marlotherm S', 'Transmission Oil (Type B)', 'Transmission Oil (Type F)',
            'Transmission Oil (Type H)', 'Water' }
tkVar1.set('Air')
popupMenu1 = OptionMenu(mainWindow, tkVar1, *choice1)
popupMenu1.place(x=300, y=80)

C4 = Canvas(mainWindow, width=240, height=70, background="white")
C4.place(x=10,y=550)
path="""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"""
gif1 = PhotoImage(data=path)
image = C4.create_image(1, 0, image=gif1, anchor=NW)

def solve():
    

    if tkVar1.get() == 'Air':
        Nu = float(0.00001575)
    elif tkVar1.get() == 'CO₂':
        Nu = float(0.000008337)
    elif tkVar1.get() == 'Diesel Fuel':
        Nu = float(0.000002883)
    elif tkVar1.get() == 'Engine Oil 5w30':
        Nu = float(0.00009684)
    elif tkVar1.get() == 'Ethylene Glycol':
        Nu = float(0.00001556)
    elif tkVar1.get() == 'Ethylene Glycol 30%':
        Nu = float(0.000001809)
    elif tkVar1.get() == 'Ethylene Glycol 50%':
        Nu = float(0.000003210)
    elif tkVar1.get() == 'Exxon 2389(Jet Engine Fuel)':
        Nu = float(0.00001957)
    elif tkVar1.get() == 'Freon 114':
        Nu = float(0.00000002457)
    elif tkVar1.get() == 'Gasoline':
        Nu = float(0.00000008472)
    elif tkVar1.get() == 'Kerosene':
        Nu = float(0.000002755)
    elif tkVar1.get() == 'Marlotherm S':
        Nu = float(0.00003917)
    elif tkVar1.get() == 'Transmission Oil (Type B)':
        Nu = float(0.00007789)
    elif tkVar1.get() == 'Transmission Oil (Type F)':
        Nu = float(0.0001177)
    elif tkVar1.get() == 'Transmission Oil (Type H)':
        Nu = float(0.00009153)
    elif tkVar1.get() == 'Water':
        Nu = float(0.0000008743)

    H = scroll1.get()
    H=H*0.01
    u = scroll2.get()
    u=u*0.01

    for i in np.arange(0.0,70.0,0.001):
        Reₓ=(u*i)/Nu
        if (Reₓ<200000):
            dx1 = (5*i)/math.sqrt(Reₓ)
            dx2 = H - dx1
            if(dx1>=H/2):
                dx1 = H/2
            if(dx2<=H/2):
                dx2 = H/2
            y.append(dx1)
            x.append(i)
            h.append(dx2)
            
        elif (Reₓ>3000000):
            dx1 = (0.37*i)/math.pow(Reₓ,0.2)
            dx2 = H - dx1
            if(dx1>=H/2):
                dx1 = H/2
            if(dx2<=H/2):
                dx2 = H/2
            y.append(dx1)
            x.append(i)
            h.append(dx2)
            
        elif (Reₓ>200000 and Reₓ<3000000):
            xl = (200000*Nu)/u
            xt = (3000000*Nu)/u
            f = (i - xl)/(xt - xl)
            dx1 = (1 - f)*(5*i)/math.sqrt(Reₓ) + f * (0.37*i)/math.pow(Reₓ,0.2)
            dx2 = H - dx1
            if(dx1>=H/2):
                dx1 = H/2
            if(dx2<=H/2):
                dx2 = H/2
            y.append(dx1)
            x.append(i)
            h.append(dx2)


    fig = Figure(figsize=(10,5))
    a = fig.add_subplot(111)
    a.set_xlim([0,5])
    txt1=a.text(0.1,H/2+0.02,'Laminar',fontsize=15)   
    txt1.set_rotation(90)

    xtran=(200000*Nu)/u   
    a.axvline(x=xtran, dashes=[6,2])
    txt2=a.text(xtran,H/2,'Transition',fontsize=15)
    txt2.set_rotation(90)
    xturb=(3000000*Nu)/u
    a.axvline(x=xturb, dashes=[6,2])
    txt3=a.text(xturb,H/2,'Turbulent',fontsize=15)
    txt3.set_rotation(90)

    count=0
    for i in y:
        count+=1
        if(i>=H/2):
            txt4=a.text(x[count],H/2+0.03,'Fully Developed Flow',fontsize=15)
            txt4.set_rotation(90)
            break

    a.plot(x,y,color='red')
    a.plot(x,h,color='red')
        
    #a.set_xlabel('length down plate (m)',fontsize=16,color='green')
    a.set_ylabel('Distance between plates(m)',fontsize=16,color='green')
   
    C2 = Canvas(mainWindow, width=100, height=40)
    C2 = FigureCanvasTkAgg(fig, master=mainWindow)
    C2.get_tk_widget().place(x=525,y=150)
    C2.draw()

    label5 = tk.Label(mainWindow, text="Entry Length = ", font="times 15 bold", bg="white")
    label5.place(x=960,y=145)
    
    count=0
    for i in y:
        count+=1
        if(i>=H/2):
            label6 = tk.Label(mainWindow, text=round(x[count],3), font="times 15 bold", bg="white")
            label6.place(x=1095,y=145)
            break
    label7 = tk.Label(mainWindow, text="m", font="times 15 bold", bg="white")
    label7.place(x=1150,y=145)

    C3 = Canvas(mainWindow, width=770, height=30, bg="DarkGoldenrod1")
    C3.place(x=645,y=175)
    C4 = Canvas(mainWindow, width=770, height=30, bg="DarkGoldenrod1")
    C4.place(x=645,y=620)
    C3.create_text(100,20, text="Top Plate", font="times 15 bold")
    C4.create_text(100,20, text="Bottom Plate", font="times 15 bold")
    C4.create_text(350,20, text="length down plate (m)", font="times 15", fill="green")
    x.clear()
    y.clear()
    h.clear()

label7 = tk.Label(mainWindow, text="This Demonstration calculates the thickness of a boundary\n layer for flow between stationary parallel plates as a function\n of distance down the plates. You can vary the distance \nbetween the plates, fluid velocity and mateirial with sliders.\n The boundary layer represents the region where viscous\n forces must be taken into account due to the no-slip condition.\n Outside of the boundary layer, viscous forces are negligible.\n Once the two boundary layers meet midway between the plates,\n the fluid flow is fully developed.", font="times 15", bg="white")
label7.place(x=10,y=205)  

button1 = tk.Button(mainWindow, text="SOLVE", command=lambda:solve())
button1.place(x=350,y=130)
mainWindow.mainloop()