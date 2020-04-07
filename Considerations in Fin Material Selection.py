import tkinter as tk
from tkinter import *
import math

mainWindow = tk.Tk()
mainWindow.configure(background='White')
mainWindow.title("Considerations in Fin Material Selection")
mainWindow.geometry("1790x790")
tkvar1 = StringVar(mainWindow)
tkvar2 = StringVar(mainWindow)
tkvar3 = StringVar(mainWindow)

label1 = tk.Label(mainWindow, text="Considerations in Fin Material Selection", fg="Red", font="algerian 18 bold", bg="white")
label1.pack()

label2 = tk.Label(mainWindow, text="We have here, a hot surface at Tb= 150 °C in a colder ambient temperature of 20 °C. We wish to cool down this hot surface\n by attaching an array of fins of some mateirial", font="8", bg="white")
label2.place(x=20,y=30)

label3 = tk.Label(mainWindow, text="For the purpose of comparison, let's experiment with long cylindrical fins of diameter 4mm, and assume\n that heat transfer coefficient(h) on all surface is 35 W/m²K .", font="8", bg="white")
label3.place(x=20,y=80)

label4 = tk.Label(mainWindow, text="Select any three materials to compare the Temperature Variation:",fg="teal", font="8", bg="white")
label4.place(x=20,y=140)

label5a = tk.Label(mainWindow, text="Select material 1:", font="10", bg="white")
label5a.place(x=420,y=180)

label5b = tk.Label(mainWindow, text="Select material 2:", font="10", bg="white")
label5b.place(x=420,y=390)

label5c = tk.Label(mainWindow, text="Select material 3:", font="10", bg="white")
label5c.place(x=420,y=590)

choice1 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar1.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu1 = OptionMenu(mainWindow, tkvar1, *choice1)
popupMenu1.place(x=400, y=210)

choice2 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar2.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu2 = OptionMenu(mainWindow, tkvar2, *choice2)
popupMenu2.place(x=400, y=420)

choice3 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar3.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu3 = OptionMenu(mainWindow, tkvar3, *choice3)
popupMenu3.place(x=400, y=620)


C1 = tk.Canvas(mainWindow, width=35, height=480,bg="red")
C1.place(x=40,y=260)
coord1 = 20, 230
C1.create_text(coord1, text="\t\tTb=150°C", angle=90, fill="black", font="times 15 bold")

C2 = tk.Canvas(mainWindow, width=945, height=35,bg="#FFB6C1")
C2.place(x=76,y=290)

C3 = tk.Canvas(mainWindow, width=945, height=35,bg="#FFFF00")
C3.place(x=76,y=490)

C4 = tk.Canvas(mainWindow, width=945, height=35,bg="#00FF00")
C4.place(x=76,y=690)

coord2a = 23,20
C2.create_text(coord2a, text="x=0.5", fill="black", font="times 15 ")

coord2b = 77,20
C2.create_text(coord2b, text="1", fill="black", font="times 15 ")

coord2c = 162,20
C2.create_text(coord2c, text="2", fill="black", font="times 15 ")

coord2d = 247,20
C2.create_text(coord2d, text="3", fill="black", font="times 15 ")

coord2e = 332,20
C2.create_text(coord2e, text="4", fill="black", font="times 15 ")

coord2f = 417,20
C2.create_text(coord2f, text="5", fill="black", font="times 15 ")

coord2g = 502,20
C2.create_text(coord2g, text="8", fill="black", font="times 15 ")

coord2h = 587,20
C2.create_text(coord2h, text="10", fill="black", font="times 15 ")

coord2i = 672,20
C2.create_text(coord2i, text="12", fill="black", font="times 15 ")

coord2j = 757,20
C2.create_text(coord2j, text="15", fill="black", font="times 15 ")

coord2k = 842,20
C2.create_text(coord2k, text="18", fill="black", font="times 15 ")

coord2l = 912,20
C2.create_text(coord2l, text="20", fill="black", font="times 15 ")



coord3a = 23,20
C3.create_text(coord3a, text="x=0.5", fill="black", font="times 15 ")

coord3b = 77,20
C3.create_text(coord3b, text="1", fill="black", font="times 15 ")

coord3c = 162,20
C3.create_text(coord3c, text="2", fill="black", font="times 15 ")

coord3d = 247,20
C3.create_text(coord3d, text="3", fill="black", font="times 15 ")

coord3e = 332,20
C3.create_text(coord3e, text="4", fill="black", font="times 15 ")

coord3f = 417,20
C3.create_text(coord3f, text="5", fill="black", font="times 15 ")

coord3g = 502,20
C3.create_text(coord3g, text="8", fill="black", font="times 15 ")

coord3h = 587,20
C3.create_text(coord3h, text="10", fill="black", font="times 15 ")

coord3i = 672,20
C3.create_text(coord3i, text="12", fill="black", font="times 15 ")

coord3j = 757,20
C3.create_text(coord3j, text="15", fill="black", font="times 15 ")

coord3k = 842,20
C3.create_text(coord3k, text="18", fill="black", font="times 15 ")

coord3l = 912,20
C3.create_text(coord3l, text="20", fill="black", font="times 15 ")


coord4a = 23,20
C4.create_text(coord4a, text="x=0.5", fill="black", font="times 15 ")

coord4b = 77,20
C4.create_text(coord4b, text="1", fill="black", font="times 15 ")

coord4c = 162,20
C4.create_text(coord4c, text="2", fill="black", font="times 15 ")

coord4d = 247,20
C4.create_text(coord4d, text="3", fill="black", font="times 15 ")

coord4e = 332,20
C4.create_text(coord4e, text="4", fill="black", font="times 15 ")

coord4f = 417,20
C4.create_text(coord4f, text="5", fill="black", font="times 15 ")

coord4g = 502,20
C4.create_text(coord4g, text="8", fill="black", font="times 15 ")

coord4h = 587,20
C4.create_text(coord4h, text="10", fill="black", font="times 15 ")

coord4i = 672,20
C4.create_text(coord4i, text="12", fill="black", font="times 15 ")

coord4j = 757,20
C4.create_text(coord4j, text="15", fill="black", font="times 15 ")

coord4k = 842,20
C4.create_text(coord4k, text="18", fill="black", font="times 15 ")

coord4l = 912,20
C4.create_text(coord4l, text="20", fill="black", font="times 15 ")

def solve():
        # Fetching k1 value
    if tkvar1.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k1 = float(14.4)
    elif tkvar1.get() == 'Bronze (K=26 W/mK)':
        k1 = float(26)
    elif tkvar1.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k1 = float(43)
    elif tkvar1.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k1 = float(50)
    elif tkvar1.get() == 'Cast Iron (K=52 W/mK)':
        k1 = float(52)
    elif tkvar1.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k1 = float(61)
    elif tkvar1.get() == 'Brass (K=111 W/mK)':
        k1 = float(111)
    elif tkvar1.get() == 'Al alloy 204 (K=125 W/mK)':
        k1 = float(125)
    elif tkvar1.get() == 'Al alloy 6066 (K=167 W/mK)':
        k1 = float(167)
    elif tkvar1.get() == 'Aluminium (K=237 W/mk)':
        k1 = float(237)
    elif tkvar1.get() == 'Copper (K=386 W/mK)':
        k1 = float(386)

    # Fetching k2 value
    if tkvar2.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k2 = float(14.4)
    elif tkvar2.get() == 'Bronze (K=26 W/mK)':
        k2 = float(26)
    elif tkvar2.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k2 = float(43)
    elif tkvar2.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k2 = float(50)
    elif tkvar2.get() == 'Cast Iron (K=52 W/mK)':
        k2 = float(52)
    elif tkvar2.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k2 = float(61)
    elif tkvar2.get() == 'Brass (K=111 W/mK)':
        k2 = float(111)
    elif tkvar2.get() == 'Al alloy 204 (K=125 W/mK)':
        k2 = float(125)
    elif tkvar2.get() == 'Al alloy 6066 (K=167 W/mK)':
        k2 = float(167)
    elif tkvar2.get() == 'Aluminium (K=237 W/mk)':
        k2 = float(237)
    elif tkvar2.get() == 'Copper (K=386 W/mK)':
        k2 = float(386)

    # Fetching k3 value
    if tkvar3.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k3 = float(14.4)
    elif tkvar3.get() == 'Bronze (K=26 W/mK)':
        k3 = float(26)
    elif tkvar3.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k3 = float(43)
    elif tkvar3.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k3 = float(50)
    elif tkvar3.get() == 'Cast Iron (K=52 W/mK)':
        k3 = float(52)
    elif tkvar3.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k3 = float(61)
    elif tkvar3.get() == 'Brass (K=111 W/mK)':
        k3 = float(111)
    elif tkvar3.get() == 'Al alloy 204 (K=125 W/mK)':
        k3 = float(125)
    elif tkvar3.get() == 'Al alloy 6066 (K=167 W/mK)':
        k3 = float(167)
    elif tkvar3.get() == 'Aluminium (K=237 W/mk)':
        k3 = float(237)
    elif tkvar3.get() == 'Copper (K=386 W/mK)':
        k3 = float(386)

    T2a1=(math.exp(-math.sqrt(35/k1)*0.5)*130)+20
    T2a = round(T2a1,2)
    entry2a=tk.Entry(mainWindow,width=5)
    entry2a.place(x=60,y=270)
    entry2a.insert(0,T2a)

    T2b1=(math.exp(-math.sqrt(35/k1)*1)*130)+20
    T2b = round(T2b1,2)
    entry2b=tk.Entry(mainWindow,width=5)
    entry2b.place(x=145,y=270)
    entry2b.insert(0,T2b)

    T2c1=(math.exp(-math.sqrt(35/k1)*2)*130)+20
    T2c = round(T2c1,2)
    entry2c=tk.Entry(mainWindow,width=5)
    entry2c.place(x=230,y=270)
    entry2c.insert(0,T2c)

    T2d1=(math.exp(-math.sqrt(35/k1)*3)*130)+20
    T2d = round(T2d1,2)
    entry2d=tk.Entry(mainWindow,width=5)
    entry2d.place(x=315,y=270)
    entry2d.insert(0,T2d)

    T2e1=(math.exp(-math.sqrt(35/k1)*4)*130)+20
    T2e = round(T2e1,2)
    entry2e=tk.Entry(mainWindow,width=5)
    entry2e.place(x=400,y=270)
    entry2e.insert(0,T2e)

    T2f1=(math.exp(-math.sqrt(35/k1)*5)*130)+20
    T2f = round(T2f1,2)
    entry2f=tk.Entry(mainWindow,width=5)
    entry2f.place(x=485,y=270)
    entry2f.insert(0,T2f)

    T2g1=(math.exp(-math.sqrt(35/k1)*8)*130)+20
    T2g = round(T2g1,2)
    entry2g=tk.Entry(mainWindow,width=5)
    entry2g.place(x=570,y=270)
    entry2g.insert(0,T2g)

    T2h1=(math.exp(-math.sqrt(35/k1)*10)*130)+20
    T2h = round(T2h1,2)
    entry2h=tk.Entry(mainWindow,width=5)
    entry2h.place(x=655,y=270)
    entry2h.insert(0,T2h)

    T2i1=(math.exp(-math.sqrt(35/k1)*12)*130)+20
    T2i = round(T2i1,2)
    entry2i=tk.Entry(mainWindow,width=5)
    entry2i.place(x=740,y=270)
    entry2i.insert(0,T2i)

    T2j1=(math.exp(-math.sqrt(35/k1)*15)*130)+20
    T2j = round(T2j1,2)
    entry2j=tk.Entry(mainWindow,width=5)
    entry2j.place(x=825,y=270)
    entry2j.insert(0,T2j)

    T2k1=(math.exp(-math.sqrt(35/k1)*18)*130)+20
    T2k = round(T2k1,2)
    entry2k=tk.Entry(mainWindow,width=5)
    entry2k.place(x=910,y=270)
    entry2k.insert(0,T2k)

    T2l1=(math.exp(-math.sqrt(35/k1)*20)*130)+20
    T2l = round(T2l1,2)
    entry2l=tk.Entry(mainWindow,width=5)
    entry2l.place(x=995,y=270)
    entry2l.insert(0,T2l)


    T3a1=(math.exp(-math.sqrt(35/k2)*0.5)*130)+20
    T3a = round(T3a1,2)
    entry3a=tk.Entry(mainWindow,width=5)
    entry3a.place(x=60,y=470)
    entry3a.insert(0,T3a)

    T3b1=(math.exp(-math.sqrt(35/k2)*1)*130)+20
    T3b = round(T3b1,2)
    entry3b=tk.Entry(mainWindow,width=5)
    entry3b.place(x=145,y=470)
    entry3b.insert(0,T3b)

    T3c1=(math.exp(-math.sqrt(35/k2)*2)*130)+20
    T3c = round(T3c1,2)
    entry3c=tk.Entry(mainWindow,width=5)
    entry3c.place(x=230,y=470)
    entry3c.insert(0,T3c)

    T3d1=(math.exp(-math.sqrt(35/k2)*3)*130)+20
    T3d = round(T3d1,2)
    entry3d=tk.Entry(mainWindow,width=5)
    entry3d.place(x=315,y=470)
    entry3d.insert(0,T3d)

    T3e1=(math.exp(-math.sqrt(35/k2)*4)*130)+20
    T3e = round(T3e1,2)
    entry3e=tk.Entry(mainWindow,width=5)
    entry3e.place(x=400,y=470)
    entry3e.insert(0,T3e)

    T3f1=(math.exp(-math.sqrt(35/k2)*5)*130)+20
    T3f = round(T3f1,2)
    entry3f=tk.Entry(mainWindow,width=5)
    entry3f.place(x=485,y=470)
    entry3f.insert(0,T3f)

    T3g1=(math.exp(-math.sqrt(35/k2)*8)*130)+20
    T3g = round(T3g1,2)
    entry3g=tk.Entry(mainWindow,width=5)
    entry3g.place(x=570,y=470)
    entry3g.insert(0,T3g)

    T3h1=(math.exp(-math.sqrt(35/k2)*10)*130)+20
    T3h = round(T3h1,2)
    entry3h=tk.Entry(mainWindow,width=5)
    entry3h.place(x=655,y=470)
    entry3h.insert(0,T3h)

    T3i1=(math.exp(-math.sqrt(35/k2)*12)*130)+20
    T3i = round(T3i1,2)
    entry3i=tk.Entry(mainWindow,width=5)
    entry3i.place(x=740,y=470)
    entry3i.insert(0,T3i)

    T3j1=(math.exp(-math.sqrt(35/k2)*15)*130)+20
    T3j = round(T3j1,2)
    entry3j=tk.Entry(mainWindow,width=5)
    entry3j.place(x=825,y=470)
    entry3j.insert(0,T3j)

    T3k1=(math.exp(-math.sqrt(35/k2)*18)*130)+20
    T3k = round(T3k1,2)
    entry3k=tk.Entry(mainWindow,width=5)
    entry3k.place(x=910,y=470)
    entry3k.insert(0,T3k)

    T3l1=(math.exp(-math.sqrt(35/k2)*20)*130)+20
    T3l = round(T3l1,2)
    entry3l=tk.Entry(mainWindow,width=5)
    entry3l.place(x=995,y=470)
    entry3l.insert(0,T3l)


    T4a1=(math.exp(-math.sqrt(35/k3)*0.5)*130)+20
    T4a = round(T4a1,2)
    entry4a=tk.Entry(mainWindow,width=5)
    entry4a.place(x=60,y=670)
    entry4a.insert(0,T4a)

    T4b1=(math.exp(-math.sqrt(35/k3)*1)*130)+20
    T4b = round(T4b1,2)
    entry4b=tk.Entry(mainWindow,width=5)
    entry4b.place(x=145,y=670)
    entry4b.insert(0,T4b)

    T4c1=(math.exp(-math.sqrt(35/k3)*2)*130)+20
    T4c = round(T4c1,2)
    entry4c=tk.Entry(mainWindow,width=5)
    entry4c.place(x=230,y=670)
    entry4c.insert(0,T4c)

    T4d1=(math.exp(-math.sqrt(35/k3)*3)*130)+20
    T4d = round(T4d1,2)
    entry4d=tk.Entry(mainWindow,width=5)
    entry4d.place(x=315,y=670)
    entry4d.insert(0,T4d)

    T4e1=(math.exp(-math.sqrt(35/k3)*4)*130)+20
    T4e = round(T4e1,2)
    entry4e=tk.Entry(mainWindow,width=5)
    entry4e.place(x=400,y=670)
    entry4e.insert(0,T4e)

    T4f1=(math.exp(-math.sqrt(35/k3)*5)*130)+20
    T4f = round(T4f1,2)
    entry4f=tk.Entry(mainWindow,width=5)
    entry4f.place(x=485,y=670)
    entry4f.insert(0,T4f)

    T4g1=(math.exp(-math.sqrt(35/k3)*8)*130)+20
    T4g = round(T4g1,2)
    entry4g=tk.Entry(mainWindow,width=5)
    entry4g.place(x=570,y=670)
    entry4g.insert(0,T4g)

    T4h1=(math.exp(-math.sqrt(35/k3)*10)*130)+20
    T4h = round(T4h1,2)
    entry4h=tk.Entry(mainWindow,width=5)
    entry4h.place(x=655,y=670)
    entry4h.insert(0,T4h)

    T4i1=(math.exp(-math.sqrt(35/k3)*12)*130)+20
    T4i = round(T4i1,2)
    entry4i=tk.Entry(mainWindow,width=5)
    entry4i.place(x=740,y=670)
    entry4i.insert(0,T4i)

    T4j1=(math.exp(-math.sqrt(35/k3)*15)*130)+20
    T4j = round(T4j1,2)
    entry4j=tk.Entry(mainWindow,width=5)
    entry4j.place(x=825,y=670)
    entry4j.insert(0,T4j)

    T4k1=(math.exp(-math.sqrt(35/k3)*18)*130)+20
    T4k = round(T4k1,2)
    entry4k=tk.Entry(mainWindow,width=5)
    entry4k.place(x=910,y=670)
    entry4k.insert(0,T4k)

    T4l1=(math.exp(-math.sqrt(35/k3)*20)*130)+20
    T4l = round(T4l1,2)
    entry4l=tk.Entry(mainWindow,width=5)
    entry4l.place(x=995,y=670)
    entry4l.insert(0,T4l)


    Q21 = math.sqrt(5521.376*k1)*130
    Q2=round(Q21,2)
    entry2A=tk.Entry(mainWindow, width=8)
    entry2A.place(x=1055,y=295)
    entry2A.insert(0,Q2)
    entry2A.config(font="5")

    Q31 = math.sqrt(5521.376*k2)*130
    Q3=round(Q31,2)
    entry3A=tk.Entry(mainWindow, width=8)
    entry3A.place(x=1055,y=495)
    entry3A.insert(0,Q3)
    entry3A.config(font="5")

    Q41 = math.sqrt(5521.376*k3)*130
    Q4=round(Q41,2)
    entry4A=tk.Entry(mainWindow, width=8)
    entry4A.place(x=1055,y=695)
    entry4A.insert(0,Q4)
    entry4A.config(font="5")

    ε21 = Q2/(57148)
    ε2=round(ε21,2)
    entry2B=tk.Entry(mainWindow, width=5)
    entry2B.place(x=1175,y=295)
    entry2B.insert(0,ε2)
    entry2B.config(font="5")

    ε31 = Q3/(57148)
    ε3=round(ε31,2)
    entry3B=tk.Entry(mainWindow, width=5)
    entry3B.place(x=1175,y=495)
    entry3B.insert(0,ε3)
    entry3B.config(font="5")

    ε41 = Q4/(57148)
    ε4=round(ε41,2)
    entry4B=tk.Entry(mainWindow, width=5)
    entry4B.place(x=1175,y=695)
    entry4B.insert(0,ε4)
    entry4B.config(font="5")


def explanation():
    secondWindow = tk.Tk()
    secondWindow.configure()
    secondWindow.title("Explanation")
    secondWindow.geometry("650x650")

    label11 = tk.Label(secondWindow, text="Explanation", fg="red", font="times 18 bold")
    label11.pack()

    label12 = tk.Label(secondWindow, text="For an Infinite Fin", fg="black", font="times 15 bold")
    label12.place(x=210,y=30)

    C6 = tk.Canvas(secondWindow, height=450 ,width=450)
    C6.place(x=40,y=80)
    C6.create_text(60,40, text="θ", font="bold")
    C6.create_line(50,50,70,50, fill="black")
    C6.create_text(60,60, text="θb", font="bold")
    C6.create_text(80,40, text="=", font="bold")
    C6.create_text(110,40, text="e⁻ᵐˣ", font="bold")
    C6.create_text(250,40, text="where m =", font="bold")
    C6.create_line(320,20,320,80, fill="black")
    C6.create_line(320,20,410,20, fill="black")
    C6.create_line(300,70,320,80, fill="black")
    C6.create_line(320,48,410,48, fill="black")
    C6.create_text(360,35, text="h P", font="bold")
    C6.create_text(360,60, text="k Ac", font="bold")
    C6.create_text(60,300, text="Qfin =", font="bold")
    C6.create_line(110,280,110,320, fill="black")
    C6.create_line(110,280,200,280, fill="black")
    C6.create_line(95,310,110,320, fill="black")
    C6.create_text(160,295, text="h P k Ac", font="bold")
    C6.create_text(220,295, text="θb", font="bold")




button1 = tk.Button(mainWindow, text="SOLVE", font="times 15 bold", command=lambda:solve())
button1.place(x=1360,y=390)

button2 = tk.Button(mainWindow, text="EXPLANATION", font="times 15 bold", command=lambda:explanation())
button2.place(x=1360,y=590)

C5 = tk.Canvas(mainWindow, height=500 ,width=3, background="white")
C5.place(x=1035,y=240)
C5.create_line(2,2,1,980, fill="black")

label7 = tk.Label(mainWindow, text="Q(watt)", font="3", bg="white", background="white")
label7.place(x=1055,y=240)

C6 = tk.Canvas(mainWindow, height=500 ,width=3, background="white")
C6.place(x=1155,y=240)
C6.create_line(2,2,1,980, fill="black")

label8 = tk.Label(mainWindow, text="Effectiveness(ε)", font="3", bg="white")
label8.place(x=1175,y=240)

C7 = tk.Canvas(mainWindow, height=60, width=220, background="white")
C7.place(x=1070,y=120)
path="""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"""
gif1 = PhotoImage(data=path)
image = C7.create_image(1, 0, image=gif1, anchor=NW)

label9 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label9.place(x=900,y=335)

label10 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label10.place(x=900,y=535)

label11 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label11.place(x=900,y=735)

label12 = tk.Label(mainWindow, text="ambient temperature=20 °C", bg="white")
label12.place(x=80,y=390)

label13 = tk.Label(mainWindow, text="ambient temperature=20 °C", bg="white")
label13.place(x=80,y=590)


mainWindow.mainloop()