import tkinter
from tkinter import *
import array

root = tkinter.Tk()
root.geometry("1300x750")
root.title("Conduction and Convection in a Natural Composite wall")
root.configure(background="white")
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)

# Heading
label1 = Label(root, text="Conduction and Convection in a Natural Composite wall", fg="dark red", font="algerian 18 bold "

                     "italic",bg="white")
label1.place(x=150, y=30)

# Inputs

label2 = Label(root, text="Inputs", fg="Black", font="algerian 15 bold",bg="white")
label2.place(x=620, y=65)


label3 = Label(root, text="Enter T₁ wall(°C)", fg="blue", font="times 15",bg="white")
label3.place(x=620, y=95)
e1 = Entry(root, bd=5, highlightcolor="blue", width=8)
e1.place(x=800, y=95)
label4 = Label(root, text="Enter T∞(°C)", fg="blue", font="times 15",bg="white")
label4.place(x=620, y=130)
e3 = Entry(root, bd=5, highlightcolor="blue", width=8)
e3.place(x=800, y=130)
Label(root, text="Natural Convection occurs at outside wall surface.\n So to predict the Natural heat transfer rate we "
                 "need\n to know T2 to Calculate Fluid properties ", fg="green", font="times 11 bold", bg="white").place(x=620, y=160)
label3 = Label(root, text="Enter T₂_assumed(°C)", fg="blue",
font="times 15",bg="white")
label3.place(x=620, y=220)
e2 = Entry(root, bd=5, highlightcolor="blue", width=8)
e2.place(x=820, y=220)
arr = []


def conduc():

    # Creating figure Canvas
    C1 = tkinter.Canvas(root, width=600, height=400, bg="white")
    # Walls
    coord1 = 150, 20, 150, 380
    C1.create_line(coord1, width=2.5)
    coord2 = 450, 20, 450, 380
    C1.create_line(coord2, width=2.5)

    # First material
    coord1a = 150, 65, 150, 315, 245, 315, 245, 65
    C1.create_polygon(coord1a, fill="yellow")
    coord1b= 182,75
    coord1c=182,95
    C1.create_text(coord1b, text="Hardwoods",font="times 10 bold italic")
    C1.create_text(coord1c, text="0.16 W/m.K", font="times 10 bold italic")

    # Second material
    coord2a = 242, 65, 242, 315, 342, 315, 342, 65
    C1.create_polygon(coord2a, fill="light green")
    coord2b = 280, 75
    coord2c = 280, 95
    C1.create_text(coord2b, text="Foam",font="times 10 bold italic")
    C1.create_text(coord2c, text="0.23 W/m.K", font="times 10 bold italic")
    # Third material
    coord3a = 342, 65, 342, 315, 450, 315, 450, 65
    C1.create_polygon(coord3a, fill="light pink")
    coord3b = 400, 75
    coord3c = 400, 95
    C1.create_text(coord3b, text="Cement mortar",font="times 10 bold italic")
    C1.create_text(coord3c, text="0.72 W/m.K", font="times 10 bold italic")
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
    coord1e = 100,124
    Label(root,text="T1",fg="red", bg="white", font="times 15 bold").place(x=130, y=100)
    Label(root, text="T2", fg="red", bg="white", font="times 15 bold").place(x=470, y=100)
    Label(root, text="Inside House", fg="red", bg="white", font="times 12 bold").place(x=30, y=140)
    Label(root, text="Outside House", fg="red", bg="white",
font="times 12 bold").place(x=470, y=140)
    Label(root, text="T₁ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=30, y=340)
    Label(root, text=float(e1.get()), fg="red", bg="white",
font="times 12 bold").place(x=120, y=340)
    Label(root, text="T∞ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=240)
    Label(root, text=float(e3.get()), fg="red", bg="white", font="times 12 bold").place(x=560, y=240)
    Label(root, text="T₂ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=340)
    Label(root, text=float(e2.get()), fg="red", bg="white",
font="times 12 bold").place(x=560, y=340)
    C1.place(x=10, y=80)


    Label(root,text="Based on the T₂_assumed above the conduction\nheat transfer rate is",bg="white", fg="blue",
          font="times 13 bold italic").place(x=650,y=350)
    Label(root, text="Q(Watts) = ",bg="white", fg="blue", font="times 13 bold italic").place(x=650, y=410)
    #Air properties
    To=float(e3.get())
    arr.append(float(e2.get()))

    Tf=((float(To)+float(e2.get()))/2)+273
    df=6.81368+(-0.51573)*(Tf)**0.5+(0.0109321)*Tf
    cpf=(297.303+(126.386)*(Tf)**0.5+(-7.54029*(Tf)+0.150637*(Tf)**(3/2)))
    kf=(-0.00719331+(0.00118869)*(Tf)**0.5+(0.000042988)*(Tf))
    visf=((0.00625687+(0.00153069*(Tf)**0.5)+(-0.0000210769*(Tf)))**3)
    beta=1/Tf
    Gr=(9.81*beta)*abs(float(e2.get())-float(To))/(pow(visf,2))
    Pr=(cpf*visf)/kf
    a=0.59
    m=0.25
    s=Gr*Pr
    Nu=a*(pow(s,m))
    h=Nu*kf
    q1=(float(e1.get())-float(e2.get()))/((0.015/0.16)+(0.02/0.23)+(0.018/0.72))
    T2=(q1/h)+float(To)
    T3=(float(T2)+float(e2.get()))/2
    Label(root, height=1, width=10, bg="white").place(x=770, y=410)
    Label(root, text=round(q1,3),bg="white", fg="red", font="times 13").place(x=770, y=410)

    Label(root, text="Q = (h)(A)(T₂-T∞)",bg="white", fg="blue", font="times 13 bold italic").place(x=650, y=450)
    Label(root, text="T₂_calculated(°C) = ",bg="white", fg="blue", font="times 13 bold italic").place(x=650, y=490)
    Label(root, height=1, width=10, bg="white").place(x=810, y=490)
    Label(root, text=round(T2,3),bg="white", fg="red", font="times 13").place(x=810, y=490)
    def iterations():
        for i in range(0, 10):
            Label(root, text=round(arr[i], 3), bg="white", fg="Blue", font="times 12 bold italic").place(x=1140,y=100 + (i * 20))
            Label(root, text="T₂_assumed ", bg="white", fg="Black", font="times 12 bold italic").place(x=1035,y=100 + (i * 20))
            Label(root, text=i + 1, bg="white", fg="Blue", font="times 12 bold italic").place(x=1120,y=100 + (i * 20))




    if (abs((float(e2.get())-T2)/float(e2.get()))) < 0.05:
        Label(root, text="Since T₂_assumed and T₂_calculated are quite  close\nWe can say that T₂_final=", bg="white",
              fg="blue", font="times 14 bold italic").place(x=650, y=530)
        Label(root, height=3, width=20, bg="white").place(x=955, y=550)
        show = (float(e2.get()) + float(T2)) / 2
        Label(root, text=round(show, 3), bg="white", fg="red", font="times 13 bold italic").place(x=965, y=555)

        # Conclusion
        Label(root, text="Conclusion", fg="black", bg="white", font="algerian 14 bold").place(x=650, y=595)
        Label(root, text="So, based on the given inputs and the iterations the value of T₂_final:", bg="white",
              fg="red", font="times 13 bold italic").place(x=650, y=640)
        show = (float(e2.get()) + float(T2)) / 2
        Label(root, text=round(show, 3), bg="white", fg="orange", font="times 13 bold italic").place(x=1170, y=640)
        Label(root, text="and heat transfer rate Q(Watts):", bg="white", fg="red", font="times 13 bold italic").place(x=650, y=670)
        Label(root, text=round(q1, 3), fg="orange", bg="white", font="times 13 bold italic").place(x=920, y=670)

        # Button for iteration
        c23 = Button(root, text="See Iterations", command=iterations)
        c23.place(x=1040, y=500)
    else:

        Label(root, text=" Your assumed value T₂_assumed is not accurate You need to", bg="white", fg="blue",
              font="times 12 bold italic").place(x=650, y=530)
        Label(root, text="iterate once more for T₂_assumed:", bg="white", fg="blue", font="times 12 bold italic").place(x=650, y=550)
        Label(root, text=round(T3, 3), bg="white", fg="red", font="times 11 bold italic").place(x=920, y=550)


def reset():
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        Label(root, height=50, width=100, bg="white").place(x=650, y=350)
        Label(root, height=30, width=250, bg="white").place(x=10, y=430)
        Label(root, height=500, width=250, bg="white").place(x=1040, y=100)
        del arr[:]
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
        coord1a = 150, 65, 150, 315, 245, 315, 245, 65
        C1.create_polygon(coord1a, fill="yellow")
        coord1b = 182, 75
        coord1c = 182, 95
        C1.create_text(coord1b, text="Hardwoods", font="times 10 bold italic")
        C1.create_text(coord1c, text="0.16 W/m.K", font="times 10 bold italic")

        # Second material
        coord2a = 242, 65, 242, 315, 342, 315, 342, 65
        C1.create_polygon(coord2a, fill="light green")
        coord2b = 280, 75
        coord2c = 280, 95
        C1.create_text(coord2b, text="Foam", font="times 10 bold italic")
        C1.create_text(coord2c, text="0.23 W/m.K", font="times 10 bold italic")

        # Third material
        coord3a = 342, 65, 342, 315, 450, 315, 450, 65
        C1.create_polygon(coord3a, fill="light pink")
        coord3b = 400, 75
        coord3c = 400, 95
        C1.create_text(coord3b, text="Cement mortar", font="times 10 bold italic")
        C1.create_text(coord3c, text="0.72 W/m.K", font="times 10 bold italic")

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

        Label(root, text="T1", fg="red", bg="white", font="times 15 bold").place(x=130, y=100)
        Label(root, text="T2", fg="red", bg="white", font="times 15 bold").place(x=470, y=100)
        Label(root, text="Inside House", fg="red", bg="white", font="times 12 bold").place(x=30, y=140)
        Label(root, text="Outside House", fg="red", bg="white", font="times 12 bold").place(x=470, y=140)
        Label(root, text="T₁ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=30, y=340)
        Label(root, text="T∞ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=240)
        Label(root, text="T₂ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=340)


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
    coord1a = 150, 65, 150, 315, 245, 315, 245, 65
    C1.create_polygon(coord1a, fill="yellow")
    coord1b = 182, 75
    coord1c = 182, 95
    C1.create_text(coord1b, text="Hardwoods", font="times 10 bold italic")
    C1.create_text(coord1c, text="0.16 W/m.K", font="times 10 bold italic")

    # Second material
    coord2a = 242, 65, 242, 315, 342, 315, 342, 65
    C1.create_polygon(coord2a, fill="light green")
    coord2b = 280, 75
    coord2c = 280, 95
    C1.create_text(coord2b, text="Foam", font="times 10 bold italic")
    C1.create_text(coord2c, text="0.23 W/m.K", font="times 10 bold italic")

    # Third material
    coord3a = 342, 65, 342, 315, 450, 315, 450, 65
    C1.create_polygon(coord3a, fill="light pink")
    coord3b = 400, 75
    coord3c = 400, 95
    C1.create_text(coord3b, text="Cement mortar", font="times 10 bold italic")
    C1.create_text(coord3c, text="0.72 W/m.K", font="times 10 bold italic")

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
    Label(root, text="T1", fg="red", bg="white", font="times 15 bold").place(x=130, y=100)
    Label(root, text="T2", fg="red", bg="white", font="times 15 bold").place(x=470, y=100)
    Label(root, text="Inside House", fg="red", bg="white", font="times 12 bold").place(x=30, y=140)
    Label(root, text="Outside House", fg="red", bg="white", font="times 12 bold").place(x=470, y=140)
    Label(root, text="T₁ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=30, y=340)
    Label(root, text="T∞ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=240)
    Label(root, text="T₂ wall(°C):", fg="red", bg="white", font="times 12 bold").place(x=470, y=340)
    C1.place(x=10, y=80)



canvas()
# Button
b = Button(root, text="Calculate", command=conduc)
b.place(x=640, y=265)
cc = Button(root, text="Reset", command=reset)
cc.place(x=730, y=265)



C10 = tkinter.Canvas(root, height=80, width=220,bg="white")
photo = """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"""
photo = PhotoImage(data=photo)
image = C10.create_image(5, 8, image=photo, anchor=NW)
C10.place(x=30, y=620)

root.mainloop()