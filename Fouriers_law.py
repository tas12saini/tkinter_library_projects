import tkinter
from tkinter import *

#SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
root = tkinter.Tk()
root.geometry("900x760")
root.title("Fourier's Law of Heat Conduction")
root.configure(background="white")
def linenew():
    coord = 140, 100, 300, 100
    C5.create_line(coord, fill="red", width=3)
    coord1 = 290, 90, 300, 100, 290, 110
    C5.create_line(coord1, fill="red", width=3)
    C5.after(1000, c5)


def c5() :
    L16 = Label(root, text="Conclusion:" ,font=("Arial 20 bold italic"),bg="white")
    L16.place(x=460, y=350)
    L17 = Label(root, text="The sign of Q and your chosen origin will tell you that:",font="times 12",fg="blue",bg="white")
    L23 = Label(root, text="No matter how you select the origin (or points 1 and 2) heat transfer ",font="times 12",fg="blue",bg="white")
    L18 = Label(root, text="rate Q as predicted from Fourier's Law will always be from Hot  ",font="times 12",fg="blue",bg="white")
    L19 = Label(root, text="Surface(H) to cold Surface (C), as shown by the red arrow",font="times 12",fg="blue",bg="white")

    L17.place(x=460, y=400)
    L23.place(x=460,y=430)
    L18.place(x=460, y=460)
    L19.place(x=460, y=490)



def c3() :
    L15 = Label(root, text="Q = -(k)(A) (dT/dx) = -(2)(3)(-100)=600 Watts",font=("times 14"),fg="green",bg="white")
    L15.place(x=470, y=210)
    L15.after(1000, linenew)


def c2() :
    L14 = Label(root, text="dT/dx = (T₂-T₁)/(x₂-x₁) = (0-100)/(1-0) = -100°C/m",font=("times 14"),fg="green",bg="white")
    L14.place(x=470, y=170)
    L14.after(1000, c3)


def call() :

    L13= Label(root,text="T₁=100 T₂=0 \nx₁=0 x₂= 1",font=("times 14"),fg="green",bg="white")
    L13.place(x=470,y=100)
    L13.after(1000,c2)

def c32() :
    L28 = Label(root, text="Q = -(k)(A) (dT/dx) = -(2)(3)(100)=-600 Watts", font=("times 14"),fg="green",bg="white")
    L28.place(x=470, y=210)
    L28.after(1000, linenew)


def c22() :
    L27 = Label(root, text="dT/dx = (T₂-T₁)/(x₂-x₁) = (0-100)/(-1-0) = 100°C/m",font=("times 14"),fg="green",bg="white")
    L27.place(x=470, y=170)
    L27.after(1000, c32)


def call2() :

    L26= Label(root, text="T₁=100 T₂=0 \nx₁=0 x₂=-1",font=("times 14"),fg="green",bg="white")
    L26.place(x=470, y=100)
    L26.after(1000, c22)


def c23() :
    L29 = Label(root, text="dT/dx = (T₂-T₁)/(x₂-x₁) = (100-0)/(1-0) =  100°C/m",font=("times 14"),fg="green",bg="white")
    L29.place(x=470, y=170)
    L29.after(1000, c32)


def call3() :


    L31= Label(root, text="T₁=0 T₂=100 \nx₁=0 x₂=1",font=("times 14"),fg="green",bg="white")
    L31.place(x=470, y=100)
    L31.after(1000, c23)

def c24() :
    L32 = Label(root, text="dT/dx = (T₂-T₁)/(x₂-x₁) =(100-0)/(-1-0)=(-100)°C/m",font=("times 14"),fg="green",bg="white")
    L32.place(x=470, y=170)
    L32.after(1000, c3)


def call4() :


    L34= Label(root, text="T₁=0 T₂=100 \nx₁=0 x₂=-1",font=("times 14"),fg="green",bg="white")
    L34.place(x=470, y=100)
    L34.after(1000, c24)



def combine_funcs():
    call()
    change1()

def combine_funcs2():
    call2()
    change2()

def combine_funcs3():
    call3()
    change3()

def combine_funcs4():
    call4()
    change4()

# Figure


C5 = tkinter.Canvas(root, bg="white", height=270, width=450)
coord1 = 180, 20, 180, 240, 270, 240, 270, 20
C5.create_polygon(coord1, fill="light green")
a_point = 180, 10
C5.create_text(a_point, text="H")
b_point = 270, 10
C5.create_text(b_point, text="C")
C5.place(x=0, y=450)


# Code before Figure
L1 = Label(root, text="Fourier's Law of Heat Conduction", font="times 20 bold", fg="red",bg="white")
L1.place(x=200, y=10)


L2= Label(root, text="The law of heat conduction is also known as Fourier’s law. Fourier’s law states that",fg="blue",bg="white")
L10= Label(root, text="“The time rate of heat transfer through \n a material is proportional to the negative gradient\n "
                      "in the temperature and to the area.”",font="Arial 12 bold", fg="red",bg="white")
L11= Label(root, text="Fourier’s equation of heat conduction:\nQ = -kA(dT/dx) where \n‘Q’ is the heat flow rate by "
                      "conduction (W)\n‘k’ is the thermal conductivity of body material (W/mK)\n‘A’ is the "
                      "cross-sectional area normal to direction of heat flow (m2) and\n‘dT/dx’ is the temperature "
                      "gradient (K/m).""", fg="blue",bg="white")
L2.place(x=0, y=50)
L10.place(x=10, y=70)
L11.place(x=0, y=130)
L4 = Label(root, text="How would you like to place the origin?", font="Arial 12 bold italic", fg="Blue",bg="white")
L4.place(x=10, y=225)
L5 = Label(root, text="(Origin will be named as 1)", font="Arial 10 bold", fg="blue",bg="white")
L5.place(x=10, y=245)


def change1():
    C5.delete("all")
    coord1 = 180, 20, 180, 240, 270, 240, 270, 20
    C5.create_polygon(coord1, fill="light green")
    coord10 = 180, 130, 270, 130
    C5.create_line(coord10, fill="blue")
    A_point = 80, 120
    C5.create_text(A_point, text="k=2 W/mK \n\nA=3m²")
    l_point = 215, 120
    C5.create_text(l_point, text="L=1m")
    a_point = 180, 10
    C5.create_text(a_point, text="H (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="C (0°C)")
    point_1 = 180, 247
    C5.create_text(point_1, text="1")
    point_2 = 270, 247
    C5.create_text(point_2, text="2")
    C5.place(x=0, y=450)
    coorda = 180, 240, 180, 160
    C5.create_line(coorda, fill="red", width=5)
    coordb = 180, 240, 250, 240
    C5.create_line(coordb, fill="red", width=5)
    coordarrow1 = 170, 165, 180, 160, 190, 165
    C5.create_line(coordarrow1, fill="red", width=3)
    coordarrow2 = 240, 230, 250, 240, 240, 250
    C5.create_line(coordarrow2, fill="red", width=3)


R1 = Radiobutton(root, text="At H pointing towards C", value=1, command=combine_funcs)
R1.place(x=0, y=295)
C1 = tkinter.Canvas(root, bg="white", height=40, width=40)
coordA = 10, 10, 10, 35, 35, 35
lineA = C1.create_line(coordA, fill="black")
coordB = 5, 15, 10, 10, 15, 15
lineB = C1.create_line(coordB, fill="black")
coordC = 30, 30, 35, 35, 30, 40
lineC = C1.create_line(coordC, fill="black")
C1.place(x=190, y=285)


def change2():
    C5.delete("all")
    coord1 = 180, 20, 180, 240, 270, 240, 270, 20
    C5.create_polygon(coord1, fill="light green")
    coord10 = 180, 130, 270, 130
    C5.create_line(coord10, fill="blue")
    A_point = 80, 120
    C5.create_text(A_point, text="k=2 W/mK \n\nA=3m²")
    l_point = 215, 120
    C5.create_text(l_point, text="L=1m")
    a_point = 180, 10
    C5.create_text(a_point, text="H (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="C (0°C)")
    point_1 = 180, 247
    C5.create_text(point_1, text="1")
    point_2 = 270, 247
    C5.create_text(point_2, text="2")
    C5.place(x=0, y=450)
    coorda = 180, 240, 180, 160
    C5.create_line(coorda, fill="red", width=5)
    coordb = 180, 240, 110, 240
    C5.create_line(coordb, fill="red", width=4.7)
    coordarrow1 = 170, 165, 180, 160, 190, 165
    C5.create_line(coordarrow1, fill="red", width=3)
    coordarrow2 = 120, 230, 110, 240, 120, 250
    C5.create_line(coordarrow2, fill="red", width=3)


R2 = Radiobutton(root, text="At H pointing away from C", value=2, command=combine_funcs2)
R2.place(x=0, y=340)
C2 = tkinter.Canvas(root, bg="white", height=40, width=40)
coordD = 35, 10, 35, 35, 10, 35
lineD = C2.create_line(coordD, fill="black")
coordE = 30, 15, 35, 10, 40, 15
lineE = C2.create_line(coordE, fill="black")
coordF = 15, 30, 10, 35, 15, 40
lineF = C2.create_line(coordF, fill="black")
C2.place(x=190, y=325)


def change3():
    C5.delete("all")
    coord1 = 180, 20, 180, 240, 270, 240, 270, 20
    C5.create_polygon(coord1, fill="light green")
    coord10 = 180, 130, 270 ,130
    C5.create_line(coord10, fill="blue")
    A_point = 80, 120
    C5.create_text(A_point, text="k=2 W/mK \n\nA=3m²")
    l_point = 215 , 120
    C5.create_text(l_point, text="L=1m")
    a_point = 180, 10
    C5.create_text(a_point, text="H (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="C (0°C)")
    point_1 = 180, 247
    C5.create_text(point_1, text="2")
    point_2 = 270, 247
    C5.create_text(point_2, text="1")
    C5.place(x=0, y=450)
    coorda = 270, 240, 270, 160
    C5.create_line(coorda, fill="red", width=5)
    coordb = 270, 240, 200, 240
    C5.create_line(coordb, fill="red", width=4.7)
    coordarrow1 = 260, 170, 270, 160, 280, 170
    C5.create_line(coordarrow1, fill="red", width=3)
    coordarrow2 = 210, 230, 200, 240, 210, 250
    C5.create_line(coordarrow2, fill="red", width=3)


R3 = Radiobutton(root, text="At C pointing towards H", value=3, command=combine_funcs3)
R3.place(x=0, y=380)
C3 = tkinter.Canvas(root, bg="white", height=40, width=40)
coordG = 35, 10, 35, 35, 10, 35
lineG = C3.create_line(coordG, fill="black")
coordH = 30,15,35,10,40,15
lineH= C3.create_line(coordH, fill="black")
coordI = 15,30,10,35,15,40
lineI = C3.create_line(coordI, fill="black")
C3.place(x=190, y=365)


def change4():
    C5.delete("all")
    coord1 = 180, 20, 180, 240, 270, 240, 270, 20
    C5.create_polygon(coord1, fill="light green")
    coord10 = 180, 130, 270, 130
    C5.create_line(coord10, fill="blue")
    A_point = 80, 120
    C5.create_text(A_point, text="k=2 W/mK \n \nA=3m²")
    l_point = 215, 120
    C5.create_text(l_point, text="L=1m")
    a_point = 180, 10
    C5.create_text(a_point, text="H (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="C (0°C)")
    point_1 = 180, 247
    C5.create_text(point_1, text="2")
    point_2 = 270, 247
    C5.create_text(point_2, text="1")
    C5.place(x=0, y=450)
    coorda = 270, 240, 270, 160
    C5.create_line(coorda, fill="red", width=5)
    coordb = 270, 240, 340, 240
    C5.create_line(coordb, fill="red", width=4.7)
    coordarrow1 = 260, 170, 270, 160, 280, 170
    C5.create_line(coordarrow1, fill="red", width=3)
    coordarrow2 = 330, 230, 340, 240, 330, 250
    C5.create_line(coordarrow2, fill="red", width=3)


R4 = Radiobutton(root, text="At C pointing away from H", value=4, command=combine_funcs4)
R4.place(x=0, y=418)
C4 = tkinter.Canvas(root, bg="white", height=40, width=40)
coordJ = 10, 10, 10 , 35 ,35 , 35
lineJ = C4.create_line(coordJ, fill="black")
coordK = 5,15,10,10,15,15
lineK = C4.create_line(coordK, fill="black")
coordL = 30,30,35,35,30,40
lineL = C4.create_line(coordL, fill="black")
C4.place(x=190, y=406)

C7 = tkinter.Canvas(root, height=70, width=220,bg="white")
photo = """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"""
photo = PhotoImage(data=photo)
image = C7.create_image(5, 8, image=photo, anchor=NW)
C7.place(x=450, y=600)

root.mainloop()

