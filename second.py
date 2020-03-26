import tkinter
from tkinter import *

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
root = tkinter.Tk()
root.geometry("900x720")
root.title("Fourier's Law of Heat Conduction")
def linenew():
    coord = 140, 100, 300, 100
    C5.create_line(coord, fill="red", width=3)
    coord1 = 290, 90, 300, 100, 290, 110
    C5.create_line(coord1, fill="red", width=3)
    C5.after(1000, c5)


def c5() :
    L16 = Label(root, text="Conclusion:", font="Arial 20 bold italic")
    L16.place(x=480, y=320)
    L17 = Label(root, text="Heat transfer is shown from A to B is",font="times 14",fg="blue")
    L23 = Label(root, text="shown in the figure.",font="times 14",fg="blue")
    L18 = Label(root, text="No matter how you select the ",font="times 14",fg="blue")
    L19 = Label(root, text="origin or points 1 and 2, heat transfer",font="times 14",fg="blue")
    L20 = Label(root, text="always occurs form hot to cold surface",font="times 14",fg="blue")
    L17.place(x=480, y=360)
    L23.place(x=480,y=390)
    L18.place(x=480, y=410)
    L19.place(x=480, y=440)
    L20.place(x=480, y=470)

def c3() :
    L15 = Label(root, text="Q = -kA dT/dx = -1 X 1 X -100=100",font=("times 17"),fg="green")
    L15.place(x=470, y=190)
    L15.after(1000, linenew)


def c2() :
    L14 = Label(root, text="dT/dx = (T2-T1)/(x2-x1) =(0-100)/(1-0)= -100",font=("times 17"),fg="green")
    L14.place(x=470, y=150)
    L14.after(1000, c3)


def call() :
    x1=1
    x2=0
    T1=0
    T2=100
    v= (T2-T1)/(x2-x1)
    L13= Label(root,text="T1=100 T2=0 x1=0 x2= 1",font=("times 17"),fg="green")
    L13.place(x=470,y=100)
    L13.after(1000,c2)

def c32() :
    L28 = Label(root, text="Q = -kA dT/dx = -1 X 1 X 100=-100", font=("times 17"),fg="green")
    L28.place(x=470, y=190)
    L28.after(1000, linenew)


def c22() :
    L27 = Label(root, text="dT/dx = (T2-T1)/(x2-x1) =(0-100)/(-1-0)= 100",font=("times 17"),fg="green")
    L27.place(x=470, y=150)
    L27.after(1000, c32)


def call2() :
    x1=0
    x2=-1
    T1=100
    T2=0
    v= (T2-T1)/(x2-x1)
    L26= Label(root, text="T1=100 T2=0 x1=0 x2=-1",font=("times 17"),fg="green")
    L26.place(x=470, y=100)
    L26.after(1000, c22)



def combine_funcs():
    call()
    change1()

def combine_funcs2():
    call2()
    change2()

def combine_funcs3():
    call2()
    change3()

def combine_funcs4():
    call()
    change4()


# Figure


C5 = tkinter.Canvas(root, bg="white", height=270, width=450)
coord1 = 180, 20, 180, 240, 270, 240, 270, 20
C5.create_polygon(coord1, fill="light green")
a_point = 180, 10
C5.create_text(a_point, text="A")
b_point = 270, 10
C5.create_text(b_point, text="B")
C5.place(x=0, y=450)


# Code before Figure
L1 = Label(root, text="Fourier's Law of Heat Conduction", font="times 20 bold", fg="red")
L1.place(x=200, y=10)


L2= Label(root, text="The law of heat conduction is also known as Fourier’s law. Fourier’s law states that",fg="blue")
L10= Label(root, text="“The time rate of heat transfer through \n a material is proportional to the negative gradient\n "
                      "in the temperature and to the area.”",font="Arial 12 bold", fg="red")
L11= Label(root, text="Fourier’s equation of heat conduction:\nQ = -kA(dT/dx) where \n‘Q’ is the heat flow rate by "
                      "conduction (W)\n‘k’ is the thermal conductivity of body material (W/mK)\n‘A’ is the "
                      "cross-sectional area normal to direction of heat flow (m2) and\n‘dT/dx’ is the temperature "
                      "gradient (K/m).""", fg="blue")
L2.place(x=0, y=50)
L10.place(x=10, y=70)
L11.place(x=0, y=130)
L3 = Label(root, text="L=1m , k=2 W/mK , A=3m²", font="Tahoma 12 bold", fg="green")
L3.place(x=15, y=225)
L4 = Label(root, text="How would you like to place the origin?", font="Arial 12 bold italic", fg="Blue")
L4.place(x=10, y=245)
L5 = Label(root, text="Origin will be named as 1", font="Tahoma 12 bold", fg="green")
L5.place(x=10, y=265)


def change1():
    C5.delete("all")
    coord1 = 180, 20, 180, 240, 270, 240, 270, 20
    C5.create_polygon(coord1, fill="light green")
    a_point = 180, 10
    C5.create_text(a_point, text="A (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="B (0°C)")
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


R1 = Radiobutton(root, text="At A pointing towards B", value=1, command=combine_funcs)
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
    a_point = 180, 10
    C5.create_text(a_point, text="A (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="B (0°C)")
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


R2 = Radiobutton(root, text="At A pointing away from B", value=2, command=combine_funcs2)
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
    a_point = 180, 10
    C5.create_text(a_point, text="A (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="B (0°C)")
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


R3 = Radiobutton(root, text="At B pointing towards A", value=3, command=combine_funcs3)
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
    a_point = 180, 10
    C5.create_text(a_point, text="A (100°C)")
    b_point = 270, 10
    C5.create_text(b_point, text="B (0°C)")
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


R4 = Radiobutton(root, text="At B pointing away from A", value=4, command=combine_funcs4)
R4.place(x=0, y=418)
C4 = tkinter.Canvas(root, bg="white", height=40, width=40)
coordJ = 10, 10, 10 , 35 ,35 , 35
lineJ = C4.create_line(coordJ, fill="black")
coordK = 5,15,10,10,15,15
lineK = C4.create_line(coordK, fill="black")
coordL = 30,30,35,35,30,40
lineL = C4.create_line(coordL, fill="black")
C4.place(x=190, y=406)

C7 = tkinter.Canvas(root, height=345, width=400)
photo = """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"""
photo = PhotoImage(data=photo)
image = C7.create_image(5, 8, image=photo, anchor=NW)
C7.place(x=450, y=600)

root.mainloop()
