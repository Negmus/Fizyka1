from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *
import math
import string

def tsr():
    s1r= float(Entry.get(s1))
    s2r= float(Entry.get(s12))
    s3r= float(Entry.get(s13))
    s4r= float(Entry.get(s14))
    s5r= float(Entry.get(s15))
    m1r= float(Entry.get(m1))
    sum1= s1r+s2r+s3r+s4r+s5r
    sum1=sum1/5
    kwa1=sum1*sum1
    d1.set(kwa1)
    v1.set(sum1)
    dzielnik=m1r*4*3.14
    wynik1=dzielnik/kwa1
    kw1.set(wynik1)

    s1r2= float(Entry.get(s2))
    s2r2= float(Entry.get(s22))
    s3r2= float(Entry.get(s23))
    s4r2= float(Entry.get(s24))
    s5r2= float(Entry.get(s25))
    m2r= float(Entry.get(m2))
    sum2= s1r2+s2r2+s3r2+s4r2+s5r2
    sum2=sum2/5
    kwa2=sum2*sum2
    d2.set(kwa2)
    v2.set(sum2)
    wynik2=dzielnik/kwa2
    kw2.set(wynik2)

    s1r3= float(Entry.get(s3))
    s2r3= float(Entry.get(s32))
    s3r3= float(Entry.get(s33))
    s4r3= float(Entry.get(s34))
    s5r3= float(Entry.get(s35))
    m3r= float(Entry.get(m3))
    sum3= s1r3+s2r3+s3r3+s4r3+s5r3
    sum3=sum3/5
    kwa3=sum3*sum3
    d3.set(kwa3)
    v3.set(sum3)
    wynik3=dzielnik/kwa3
    kw3.set(wynik3)

    s1r4= float(Entry.get(s4))
    s2r4= float(Entry.get(s42))
    s3r4= float(Entry.get(s43))
    s4r4= float(Entry.get(s44))
    s5r4= float(Entry.get(s45))
    m4r= float(Entry.get(m4))
    sum4= s1r4+s2r4+s3r4+s4r4+s5r4
    sum4=sum4/5
    kwa4=sum4*sum4
    d4.set(kwa4)
    v4.set(sum4)
    wynik4=dzielnik/kwa4
    kw4.set(wynik4)
    return None
root = Tk()
x= Entry(root)
#Pierwszy wiersz
Label(root, text="L.p").grid(row=0, column=0)
Label(root, text="t1=10T.1").grid(row=0, column=1)
Label(root, text="t1=10T.2").grid(row=0, column=2)
Label(root, text="t1=10T.3").grid(row=0, column=3)
Label(root, text="t1=10T.4").grid(row=0, column=4)
#Drugi wiersz
Label(root, text="Masa").grid(row=1, column=0)
m1= Entry(root)
m1.grid(row=1, column=1)
m2= Entry(root)
m2.grid(row=1, column=2)
m3= Entry(root)
m3.grid(row=1, column=3)
m4= Entry(root)
m4.grid(row=1, column=4)
#1 pomiar
Label(root, text="1").grid(row=2, column=0)
s1= Entry(root)
s1.grid(row=2, column=1)
s2= Entry(root)
s2.grid(row=2, column=2)
s3= Entry(root)
s3.grid(row=2, column=3)
s4= Entry(root)
s4.grid(row=2, column=4)
#2 pomiar
Label(root, text="2").grid(row=3, column=0)
s12= Entry(root)
s12.grid(row=3, column=1)
s22= Entry(root)
s22.grid(row=3, column=2)
s32= Entry(root)
s32.grid(row=3, column=3)
s42= Entry(root)
s42.grid(row=3, column=4)
#3 pomiar
Label(root, text="3").grid(row=4, column=0)
s13= Entry(root)
s13.grid(row=4, column=1)
s23= Entry(root)
s23.grid(row=4, column=2)
s33= Entry(root)
s33.grid(row=4, column=3)
s43= Entry(root)
s43.grid(row=4, column=4)
#4 pomiar
Label(root, text="4").grid(row=5, column=0)
s14= Entry(root)
s14.grid(row=5, column=1)
s24= Entry(root)
s24.grid(row=5, column=2)
s34= Entry(root)
s34.grid(row=5, column=3)
s44= Entry(root)
s44.grid(row=5, column=4)
#5 pomiar
Label(root, text="5").grid(row=6, column=0)
s15= Entry(root)
s15.grid(row=6, column=1)
s25= Entry(root)
s25.grid(row=6, column=2)
s35= Entry(root)
s35.grid(row=6, column=3)
s45= Entry(root)
s45.grid(row=6, column=4)
#Sredni czas
Label(root, text="Tsr").grid(row=7, column=0)
v1 = StringVar()
Label(root, textvariable=v1).grid(row=7, column=1)
v2 = StringVar()
Label(root, textvariable=v2).grid(row=7, column=2)
v3 = StringVar()
Label(root, textvariable=v3).grid(row=7, column=3)
v4 = StringVar()
Label(root, textvariable=v4).grid(row=7, column=4)
#Sredni czas do kwadratu
Label(root, text="Tsr^2").grid(row=8, column=0)
d1 = StringVar()
Label(root, textvariable=d1).grid(row=8, column=1)
d2 = StringVar()
Label(root, textvariable=d2).grid(row=8, column=2)
d3 = StringVar()
Label(root, textvariable=d3).grid(row=8, column=3)
d4 = StringVar()
Label(root, textvariable=d4).grid(row=8, column=4)
#Obliczamy k
Label(root, text="Wynik dla k").grid(row=9, column=0)
kw1 = StringVar()
Label(root, textvariable=kw1).grid(row=9, column=1)
kw2 = StringVar()
Label(root, textvariable=kw2).grid(row=9, column=2)
kw3 = StringVar()
Label(root, textvariable=kw3).grid(row=9, column=3)
kw4 = StringVar()
Label(root, textvariable=kw4).grid(row=9, column=4)
Button(root, text="Licz", command=tsr).grid(row=10, column=0)

root.mainloop()
