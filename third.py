import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry("1090x750")
root.title("Composite Wall Design in a Snowy Ambient")
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)

# Heading
label1 = Label(root, text="Composite Wall Design in a Snowy Ambient", fg="dark red", font="algerian 18 bold "
                                                                                                   "italic")
label1.place(x=150, y=30)

# Inputs

label2 = Label(root, text="Inputs", fg="Black", font="algerian 15 bold")
label2.place(x=620, y=130)

label3 = Label(root, text="Select material 1:", fg="blue", font="times 15")
label3.place(x=620, y=180)
choice1 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar1.set('Softwoods (0.12 W/m.K)')
popupMenu1 = OptionMenu(root, tkvar1, *choice1)
popupMenu1.place(x=820, y=180)

label4 = Label(root, text="Select material 2:", fg="blue", font="times 15")
label4.place(x=620, y=230)
choice2 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar2.set('Gypsum or plaster board (0.17 W/m.K)')
popupMenu2 = OptionMenu(root, tkvar2, *choice2)
popupMenu2.place(x=820, y=230)

label5 = Label(root, text="Select material 3:", fg="blue", font="times 15")
label5.place(x=620, y=280)
choice3 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar3.set('Foam (0.23 W/m.K)')
popupMenu3 = OptionMenu(root, tkvar3, *choice3)
popupMenu3.place(x=820, y=280)

label6 = Label(root, text="Contact Resistance (k/W):", fg="blue", font="times 15")
label6.place(x=620, y=330)
label7 = Label(root, text="(Rtc1'', Rtc2'' (m²K/W))")
label7.place(x=620, y=355)
scroll1 = Scale(root, from_=0, to=0.1, resolution=0.001, orient=HORIZONTAL, activebackground="orange")
scroll1.place(x=910, y=315)

# Outputs
C2 = tkinter.Canvas(root, width=900, height=200)
coord1e = 50, 10
C2.create_text(coord1e, text="Outputs", font="times 15 bold")
coord2e = 250, 70
C2.create_text(coord2e, text="Equivalent Thermal Conductivity of composite wall is: \n Keq =                             W/m.K",
               font="times 15 bold", fill="red")
coord3e = 250, 140
C2.create_text(coord3e, text="Total heat transfer through the composite wall is: \n Q =                               Watts",
               font="times 15 bold", fill="red")
C2.place(x=10, y=490)

# Small Canvas for answers
C3 = tkinter.Canvas(root, width=88, height=40)
C3.place(x=125, y=557)
C4 = tkinter.Canvas(root, width=100, height=40)
C4.place(x=110, y=627)
# function for calculation of thermal conductivity
def conduc():
    C3.delete("all")
    C4.delete("all")
    s1 = float(scroll1.get())
    # Creating figure Canvas
    C1 = tkinter.Canvas(root, width=600, height=400, bg="white")
    # Walls
    coord1 = 150, 20, 150, 380
    C1.create_line(coord1, width=2.5)
    coord2 = 450, 20, 450, 380
    C1.create_line(coord2, width=2.5)

    # First material
    coord1a = 150, 65, 150, 315, 225, 315, 225, 65
    C1.create_polygon(coord1a, fill="yellow")
    coord1b= 180,75
    C1.create_text(coord1b, text="Material-1",font="times 10 bold italic")

    # Second material
    coord2a = 242, 65, 242, 315, 342, 315, 342, 65
    C1.create_polygon(coord2a, fill="light green")
    coord2b = 280, 75
    C1.create_text(coord2b, text="Material-2",font="times 10 bold italic")
    # Third material
    coord3a = 360, 65, 360, 315, 450, 315, 450, 65
    C1.create_polygon(coord3a, fill="light pink")
    coord3b = 400, 75
    C1.create_text(coord3b, text="Material-3",font="times 10 bold italic")
    # Length line 1
    coord1b = 160, 320, 150, 330, 160, 340
    C1.create_line(coord1b, fill="black", width=2)
    coord2b = 150, 330, 225, 330
    C1.create_line(coord2b, fill="black", width=2)
    coord3b = 215, 320, 225, 330, 215, 340
    C1.create_line(coord3b, fill="black", width=2)
    coord4b = 185, 340
    C1.create_text(coord4b, text=" 15 mm", font="bold")

    # Length line 2
    coord1c = 252, 320, 242, 330, 252, 340
    C1.create_line(coord1c, fill="black", width=2)
    coord2c = 242, 330, 342, 330
    C1.create_line(coord2c, fill="black", width=2)
    coord3c = 332, 320, 342, 330, 332, 340
    C1.create_line(coord3c, fill="black", width=2)
    coord4c = 290, 340
    C1.create_text(coord4c, text="20 mm", font="bold")

    # Length line 3
    coord1c = 370, 320, 360, 330, 370, 340
    C1.create_line(coord1c, fill="black", width=2)
    coord2c = 360, 330, 450, 330
    C1.create_line(coord2c, fill="black", width=2)
    coord3c = 440, 320, 450, 330, 440, 340
    C1.create_line(coord3c, fill="black", width=2)
    coord4d = 408, 340
    C1.create_text(coord4d, text="18 mm", font="bold")

    # Inside House and outside House
    coord1d = 80, 80
    C1.create_text(coord1d, text="Inside House \n\n\n\n\n\nTin (wall) = 28°C")
    coord2d = 530, 80
    C1.create_text(coord2d, text="Outside House \n\n\n\n\n\nTout (wall) = -30°C")
    C1.place(x=10, y=80)
    # Fetching k1 value
    if tkvar1.get() == 'Asbestos-cement board (0.58 W/m.K)':
        k1 = float(0.58)
    elif tkvar1.get() == 'Gypsum or plaster board (0.17 W/m.K)':
        k1 = float(0.17)
    elif tkvar1.get() == 'Hardwoods (0.16 W/m.K)':
        k1 = float(0.16)
    elif tkvar1.get() == 'Softwoods (0.12 W/m.K)':
        k1 = float(0.12)
    elif tkvar1.get() == 'Cement mortar (0.72 W/m.K)':
        k1 = float(0.72)
    elif tkvar1.get() == 'Brick (0.72 W/m.K)':
        k1 = float(0.72)
    elif tkvar1.get() == 'Sand/gravel, 20cm thick (1.0 W/m.K)':
        k1 = float(1.0)
    elif tkvar1.get() == 'Cement plaster, Sand aggregate (0.72 W/m.K)':
        k1 = float(0.72)
    elif tkvar1.get() == 'Gypsum plaster, Sand aggregate (0.22 W/m.k)':
        k1 = float(0.22)
    elif tkvar1.get() == 'Glass fiber, paper faced (0.046 W/m.K)':
        k1 = float(0.046)
    elif tkvar1.get() == 'Typical Silicon powder (0.0017 W/m.K)':
        k1 = float(0.0017)
    elif tkvar1.get() == 'Foam (0.23 W/m.K)':
        k1 = float(0.23)

    # Fetching k2 value
    if tkvar2.get() == 'Asbestos-cement board (0.58 W/m.K)':
        k2 = float(0.58)
    elif tkvar2.get() == 'Gypsum or plaster board (0.17 W/m.K)':
        k2 = float(0.17)
    elif tkvar2.get() == 'Hardwoods (0.16 W/m.K)':
        k2 = float(0.16)
    elif tkvar2.get() == 'Softwoods (0.12 W/m.K)':
        k2 = float(0.12)
    elif tkvar2.get() == 'Cement mortar (0.72 W/m.K)':
        k2 = float(0.72)
    elif tkvar2.get() == 'Brick (0.72 W/m.K)':
        k2 = float(0.72)
    elif tkvar2.get() == 'Sand/gravel, 20cm thick (1.0 W/m.K)':
        k2 = float(1.0)
    elif tkvar2.get() == 'Cement plaster, Sand aggregate (0.72 W/m.K)':
        k2 = float(0.72)
    elif tkvar2.get() == 'Gypsum plaster, Sand aggregate (0.22 W/m.k)':
        k2 = float(0.22)
    elif tkvar2.get() == 'Glass fiber, paper faced (0.046 W/m.K)':
        k2 = float(0.046)
    elif tkvar2.get() == 'Typical Silicon powder (0.0017 W/m.K)':
        k2 = float(0.0017)
    elif tkvar2.get() == 'Foam (0.23 W/m.K)':
        k2 = float(0.23)

    # Fetching k3 value
    if tkvar3.get() == 'Asbestos-cement board (0.58 W/m.K)':
        k3 = float(0.58)
    elif tkvar3.get() == 'Gypsum or plaster board (0.17 W/m.K)':
        k3 = float(0.17)
    elif tkvar3.get() == 'Hardwoods (0.16 W/m.K)':
        k3 = float(0.16)
    elif tkvar3.get() == 'Softwoods (0.12 W/m.K)':
        k3 = float(0.12)
    elif tkvar3.get() == 'Cement mortar (0.72 W/m.K)':
        k3 = float(0.72)
    elif tkvar3.get() == 'Brick (0.72 W/m.K)':
        k3 = float(0.72)
    elif tkvar3.get() == 'Sand/gravel, 20cm thick (1.0 W/m.K)':
        k3 = float(1.0)
    elif tkvar3.get() == 'Cement plaster, Sand aggregate (0.72 W/m.K)':
        k3 = float(0.72)
    elif tkvar3.get() == 'Gypsum plaster, Sand aggregate (0.22 W/m.k)':
        k3 = float(0.22)
    elif tkvar3.get() == 'Glass fiber, paper faced (0.046 W/m.K)':
        k3 = float(0.046)
    elif tkvar3.get() == 'Typical Silicon powder (0.0017 W/m.K)':
        k3 = float(0.0017)
    elif tkvar3.get() == 'Foam (0.23 W/m.K)':
        k3 = float(0.23)
    a = int(1)
    l1 = float(0.015)
    l2 = float(0.020)
    l3 = float(0.018)
    l = float(0.053)
    Ra = l1/(k1*a)
    Rb = l2/(k2*a)
    Rc = l3/(k3*a)
    Rtot = Ra + Rb + Rc + s1 + s1
    K = round(float(l/(Rtot*a)), 3)
    Q = round(float(58/Rtot*a), 3)
    coord1f = 45, 15
    C3.create_text(coord1f, text=K, font="algerian 15", fill="blue")
    coord2f = 45, 15
    C4.create_text(coord2f, text=Q, font="algerian 15", fill="blue")
    # Fetching points for Graph
    ta = round(float(28 - Q*Ra), 2)
    tb1 = round(float(ta - (Q*s1)/a), 2)
    tb2 = round(float(tb1 - Q*Rb), 2)
    tc = round(float(tb2 - (Q*s1)/a), 2)
    tout = tc - Q*Rc
    # points to show

    coord1g = 150, 99, 225, (85 + (90 - ta) * 7)/3, 242, (85 + (90 - tb1) * 7)/3, 342, (85 + (90 - tb2) * 7)/3, 360, (85 + (
            90 - tc) * 7)/3, 450, (85 + (90-tout)*7)/3
    coord1p = 130, 99
    C1.create_text(coord1p, text="Tin", font="times 12 bold")
    coord2p = 215, (85+(90-ta)*7-10)/3
    C1.create_text(coord2p, text=ta, font="times 12 bold")
    coord3p = 262, ((85 + (90 - tb1) * 7)-10)/3
    C1.create_text(coord3p, text=tb1, font="times 12 bold")
    coord4p = 332, (95 + (90 - tb2) * 7)/3
    C1.create_text(coord4p, text=tb2, font="times 12 bold")
    coord5p = 370, (75 + (90 - tc) * 7)/3
    C1.create_text(coord5p, text=tc, font="times 12 bold")
    coord6p = 480, (85 + (90-tout)*7)/3
    C1.create_text(coord6p, text="Tout", font="times 12 bold")
    line = C1.create_line(coord1g, width=2, fill="red")


def reset():
        C3.delete("all")
        C4.delete("all")
        C1 = tkinter.Canvas(root, width=600, height=400, bg="white")
        C1.delete("all")
        # Creating figure Canvas
        C1 = tkinter.Canvas(root, width=600, height=400, bg="white")
        # Walls
        coord1 = 150, 20, 150, 380
        C1.create_line(coord1, width=2.5)
        coord2 = 450, 20, 450, 380
        C1.create_line(coord2, width=2.5)

        # First material
        coord1a = 150, 65, 150, 315, 225, 315, 225, 65
        C1.create_polygon(coord1a, fill="yellow")

        # Second material
        coord2a = 242, 65, 242, 315, 342, 315, 342, 65
        C1.create_polygon(coord2a, fill="light green")

        # Third material
        coord3a = 360, 65, 360, 315, 450, 315, 450, 65
        C1.create_polygon(coord3a, fill="light pink")

        # Length line 1
        coord1b = 160, 320, 150, 330, 160, 340
        C1.create_line(coord1b, fill="black", width=2)
        coord2b = 150, 330, 225, 330
        C1.create_line(coord2b, fill="black", width=2)
        coord3b = 215, 320, 225, 330, 215, 340
        C1.create_line(coord3b, fill="black", width=2)
        coord4b = 185, 340
        C1.create_text(coord4b, text=" 15 mm", font="bold")

        # Length line 2
        coord1c = 252, 320, 242, 330, 252, 340
        C1.create_line(coord1c, fill="black", width=2)
        coord2c = 242, 330, 342, 330
        C1.create_line(coord2c, fill="black", width=2)
        coord3c = 332, 320, 342, 330, 332, 340
        C1.create_line(coord3c, fill="black", width=2)
        coord4c = 290, 340
        C1.create_text(coord4c, text="20 mm", font="bold")

        # Length line 3
        coord1c = 370, 320, 360, 330, 370, 340
        C1.create_line(coord1c, fill="black", width=2)
        coord2c = 360, 330, 450, 330
        C1.create_line(coord2c, fill="black", width=2)
        coord3c = 440, 320, 450, 330, 440, 340
        C1.create_line(coord3c, fill="black", width=2)
        coord4d = 408, 340
        C1.create_text(coord4d, text="18 mm", font="bold")

        # Inside House and outside House
        coord1d = 80, 80
        C1.create_text(coord1d, text="Inside House \n\n\n\n\n\nTin (wall) = 28°C")
        coord2d = 530, 80
        C1.create_text(coord2d, text="Outside House \n\n\n\n\n\nTout (wall) = -30°C")
        C1.place(x=10, y=80)


def canvas():
    # Creating figure Canvas
    C1 = tkinter.Canvas(root, width=600, height=400, bg="white")
    # Walls
    coord1 = 150, 20, 150, 380
    C1.create_line(coord1, width=2.5)
    coord2 = 450, 20, 450, 380
    C1.create_line(coord2, width=2.5)

    # First material
    coord1a = 150, 65, 150, 315, 225, 315, 225, 65
    C1.create_polygon(coord1a, fill="yellow")

    # Second material
    coord2a = 242, 65, 242, 315, 342, 315, 342, 65
    C1.create_polygon(coord2a, fill="light green")

    # Third material
    coord3a = 360, 65, 360, 315, 450, 315, 450, 65
    C1.create_polygon(coord3a, fill="light pink")

    # Length line 1
    coord1b = 160, 320, 150, 330, 160, 340
    C1.create_line(coord1b, fill="black", width=2)
    coord2b = 150, 330, 225, 330
    C1.create_line(coord2b, fill="black", width=2)
    coord3b = 215, 320, 225, 330, 215, 340
    C1.create_line(coord3b, fill="black", width=2)
    coord4b = 185, 340
    C1.create_text(coord4b, text=" 15 mm", font="bold")

    # Length line 2
    coord1c = 252, 320, 242, 330, 252, 340
    C1.create_line(coord1c, fill="black", width=2)
    coord2c = 242, 330, 342, 330
    C1.create_line(coord2c, fill="black", width=2)
    coord3c = 332, 320, 342, 330, 332, 340
    C1.create_line(coord3c, fill="black", width=2)
    coord4c = 290, 340
    C1.create_text(coord4c, text="20 mm", font="bold")

    # Length line 3
    coord1c = 370, 320, 360, 330, 370, 340
    C1.create_line(coord1c, fill="black", width=2)
    coord2c = 360, 330, 450, 330
    C1.create_line(coord2c, fill="black", width=2)
    coord3c = 440, 320, 450, 330, 440, 340
    C1.create_line(coord3c, fill="black", width=2)
    coord4d = 408, 340
    C1.create_text(coord4d, text="18 mm", font="bold")

    # Inside House and outside House
    coord1d = 80, 80
    C1.create_text(coord1d, text="Inside House \n\n\n\n\n\nTin (wall) = 28°C")
    coord2d = 530, 80
    C1.create_text(coord2d, text="Outside House \n\n\n\n\n\nTout (wall) = -30°C")
    C1.place(x=10, y=80)



canvas()


def theory():
    newwin = Toplevel(root)
    newwin.geometry("700x700")
    newwin.title("composite wall")
    C5 = tkinter.Canvas(newwin, width=400, height=300)
    C5.place(x=300, y=180)
    coord1f = 10, 40, 34, 40, 38, 45, 42, 35, 46, 45, 50, 35, 54, 45, 58, 40, 78, 40, 102, 40, 106, 45, 110, 35, 114, 45, 118, 35, 122, 45, 126, 40, 146, 40, 174, 40, 178, 45, 182, 35, 186, 45, 190, 35, 194, 45, 198, 40, 214, 40, 242, 40, 246, 45, 250, 35, 254, 45, 258, 35, 262, 45, 266, 40, 282, 40, 316, 40, 320, 45, 324, 35, 328, 45, 332, 35, 336, 45, 340, 40, 360, 40
    C5.create_line(coord1f, width=1.5)
    coord2f = 28, 20
    C5.create_text(coord2f, text="Tin(28°C)")
    coord3f = 44, 60
    C5.create_text(coord3f, text="R₁")
    coord4f = 78, 20
    C5.create_text(coord4f, text="T₁")
    coord5f = 106, 60
    C5.create_text(coord5f, text="Rtc")
    coord6f = 146, 20
    C5.create_text(coord6f, text="T₂")
    coord7f = 178, 60
    C5.create_text(coord7f, text="R₂")
    coord8f = 214, 20
    C5.create_text(coord8f, text="T₂'")
    coord9f = 246, 60
    C5.create_text(coord9f, text="Rtc")
    coord10f = 282, 20
    C5.create_text(coord10f, text="T₃")
    coord11f = 320, 60
    C5.create_text(coord11f, text="R₃")
    coord12f = 350, 20
    C5.create_text(coord12f, text="T₃'(-30°C)")
    L1 = Label(newwin, text="Composite wall design in a snow ambient", font="times 20 bold", fg="blue")
    L1.place(x=5, y=10)
    L2 = Label(newwin, text="Theory", font="times 20 bold italic", fg="red")
    L2.place(x=5, y=80)
    L3 = Label(newwin, text="Consider three plane walls in contact (called composite wall) as shown in the figure.The individual walls are\n labeled as 1, 2, 3 having different thermal conductivities k and thickness L.Outside the walls the temprature is \ndifferent too as shown in the figure\n",fg="green")
    L3.place(x=5, y=130)
    L4 = Label(newwin, text="Calculations:", font="times 14", fg="red")
    L4.place(x=5, y=200)
    L5 = Label(newwin, text="L=L₁ + L₂ + L₃ \n\nkeq =1 / ((L₁ / Lk₁) + (L₂ / Lk₂) + (L₃ / Lk₃))\n\nQ = keq(A)(ΔT / L) Watts",font="times 12",fg="blue")
    L5.place(x=5, y=240)
    L6 = Label(newwin, text="How to Plot: ", font="times 14 italic bold", fg="red")
    L6.place(x=5, y=350)
    L7 = Label(newwin, text="T₁ = (Tin - T₁)=(L₁/Ak₁)Q \nT₁=Tin-(L₁/Ak₁)Q",font="times 14",fg="blue")
    L7.place(x=5, y=400)
    L8 = Label(newwin, text="T₂ = (T₁ - T₂)=(Rtc)Q \nT₂=T₁-(Rtc)Q", font="times 14",fg="blue")
    L8.place(x=5, y=450)
    L9 = Label(newwin, text="T₂' = (T₂ - T₂')=(L₂/Ak₂)Q \nT₂'=T₂-(L₂/Ak₂)Q", font="times 14", fg="blue")
    L9.place(x=5, y=500)
    L10 = Label(newwin, text="T₃ = (T₂' - T₃)=(Rtc)Q \nT₃=T₂'-(Rtc)Q", font="times 14", fg="blue")
    L10.place(x=5, y=550)


# Buttons
button1 = Button(root, text="SOLVE", fg="red", width=10, height=2, command=conduc)
button1.place(x=620, y=400)
button2 = Button(root, text="RESET", fg="red", width=10, height=2, command=reset)
button2.place(x=750, y=400)
button3 = Button(root, text="EXPLANATION", fg="red", width=10, height=2, command=theory)
button3.place(x=880, y=400)

C10 = tkinter.Canvas(root, height=345, width=400)
photo = """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"""
photo = PhotoImage(data=photo)
image = C10.create_image(5, 8, image=photo, anchor=NW)
C10.place(x=650, y=620)

root.mainloop()