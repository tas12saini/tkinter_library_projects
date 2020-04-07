import tkinter
from tkinter import *

root = tkinter.Tk()
root.geometry("1090x750")
root.title("Composite Wall Design in a Snowy Ambient")
root.configure(background="white")
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)

# Heading
label1 = Label(root, text="Composite Wall Design in a Snowy Ambient", fg="dark red", font="algerian 18 bold "
                                                                                            "italic",bg="white")
label1.place(x=150, y=30)

# Inputs

label2 = Label(root, text="Inputs", fg="Black", font="algerian 15 bold",bg="white")
label2.place(x=620, y=130)

label3 = Label(root, text="Select material 1:", fg="blue", font="times 15",bg="white")
label3.place(x=620, y=180)
choice1 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar1.set('Softwoods (0.12 W/m.K)')
popupMenu1 = OptionMenu(root, tkvar1, *choice1)
popupMenu1.place(x=820, y=180)

label4 = Label(root, text="Select material 2:", fg="blue", font="times 15",bg="white")
label4.place(x=620, y=230)
choice2 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar2.set('Gypsum or plaster board (0.17 W/m.K)')
popupMenu2 = OptionMenu(root, tkvar2, *choice2)
popupMenu2.place(x=820, y=230)

label5 = Label(root, text="Select material 3:", fg="blue", font="times 15",bg="white")
label5.place(x=620, y=280)
choice3 = {'Asbestos-cement board (0.58 W/m.K)', 'Gypsum or plaster board (0.17 W/m.K)', 'Hardwoods (0.16 W/m.K)',
           'Softwoods (0.12 W/m.K)', 'Cement mortar (0.72 W/m.K)', 'Brick (0.72 W/m.K)',
           'Sand/gravel, 20cm thick (1.0 W/m.K)', 'Cement plaster, Sand aggregate (0.72 W/m.K)',
           'Gypsum plaster, Sand aggregate (0.22 W/m.k)', 'Glass fiber, paper faced (0.046 W/m.K)',
           'Typical Silicon powder (0.0017 W/m.K)', 'Foam (0.23 W/m.K)'}
tkvar3.set('Foam (0.23 W/m.K)')
popupMenu3 = OptionMenu(root, tkvar3, *choice3)
popupMenu3.place(x=820, y=280)

label6 = Label(root, text="Contact Resistance (k/W):", fg="blue", font="times 15",bg="white")
label6.place(x=620, y=330)
label7 = Label(root, text="(Rtc1'', Rtc2'' (m²K/W))",bg="white")
label7.place(x=620, y=355)
scroll1 = Scale(root, from_=0, to=0.1, resolution=0.001, orient=HORIZONTAL, activebackground="orange",bg="white")
scroll1.place(x=910, y=315)

# Outputs
C2 = tkinter.Canvas(root, width=900, height=200,bg="white")
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
C3 = tkinter.Canvas(root, width=88, height=40,bg="white")
C3.place(x=125, y=557)
C4 = tkinter.Canvas(root, width=100, height=40,bg="white")
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
    newwin.configure(background="white")
    C5 = tkinter.Canvas(newwin, width=400, height=300,bg="white")
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
    L1 = Label(newwin, text="Composite wall design in a snowy ambient", font="times 20 bold", fg="blue",bg="white")
    L1.place(x=5, y=10)
    L2 = Label(newwin, text="Theory", font="times 20 bold italic", fg="red",bg="white")
    L2.place(x=5, y=80)
    L3 = Label(newwin, text="Consider three plane walls in contact (called composite wall) as shown in the figure.The individual walls are\n labeled as 1, 2, 3 having different thermal conductivities k and thickness L.Outside the walls the temprature is \ndifferent too as shown in the figure\n",fg="green",bg="white")
    L3.place(x=5, y=130)
    L4 = Label(newwin, text="Calculations:", font="times 14", fg="red",bg="white")
    L4.place(x=5, y=200)
    L5 = Label(newwin, text="L=L₁ + L₂ + L₃ \n\nkeq =1 / ((L₁ / Lk₁) + (L₂ / Lk₂) + (L₃ / Lk₃))\n\nQ = keq(A)(ΔT / L) Watts",font="times 12",fg="blue",bg="white")
    L5.place(x=5, y=240)
    L6 = Label(newwin, text="From the Electric Circuit:", font="times 14 italic bold", fg="red",bg="white")
    L6.place(x=5, y=350)
    L7 = Label(newwin, text="T₁ = (Tin - T₁)=(L₁/Ak₁)Q \nT₁=Tin-(L₁/Ak₁)Q",font="times 14",fg="blue",bg="white")
    L7.place(x=5, y=400)
    L8 = Label(newwin, text="T₂ = (T₁ - T₂)=(Rtc)Q \nT₂=T₁-(Rtc)Q", font="times 14",fg="blue",bg="white")
    L8.place(x=5, y=450)
    L9 = Label(newwin, text="T₂' = (T₂ - T₂')=(L₂/Ak₂)Q \nT₂'=T₂-(L₂/Ak₂)Q", font="times 14", fg="blue",bg="white")
    L9.place(x=5, y=500)
    L10 = Label(newwin, text="T₃ = (T₂' - T₃)=(Rtc)Q \nT₃=T₂'-(Rtc)Q", font="times 14", fg="blue",bg="white")
    L10.place(x=5, y=550)

# Buttons
button1 = Button(root, text="SOLVE", fg="red", width=10, height=2, command=conduc)
button1.place(x=620, y=400)
button2 = Button(root, text="RESET", fg="red", width=10, height=2, command=reset)
button2.place(x=750, y=400)
button3 = Button(root, text="EXPLANATION", fg="red", width=10, height=2, command=theory)
button3.place(x=880, y=400)

C10 = tkinter.Canvas(root, height=345, width=400,bg="white")
photo = """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"""
photo = PhotoImage(data=photo)
image = C10.create_image(5, 8, image=photo, anchor=NW)
C10.place(x=650, y=620)

root.mainloop()