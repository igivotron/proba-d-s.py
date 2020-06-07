import random
from tkinter import *



def commencer():
    i = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    while i < 1000:
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = a + b
        print (c)
        i+=1
        if c == 1:
            m+=1
        if c == 2:
            n+=1
        if c == 3:
            o+=1
        if c == 4:
            p+=1
        if c ==5:
            q+=1
        if c == 6:
            r+=1
        if c == 7:
            s+=1
        if c == 8:
            t+=1
        if c == 9:
            u+=1
        if c == 10:
            v+=1
        if c == 11:
            w+=1
        if c == 12:
            x+=1

    print ("1 =", m)
    print ("2 =", n)
    print ("3 =", o)
    print ("4 =", p)
    print ("5 =", q)
    print ("6 =", r)
    print ("7 =", s)
    print ("8 =", t)
    print ("9 =", u)
    print ("10 =", v)
    print ("11 =", w)
    print ("12 =", x)

    label1 = Label(fen, text=m)
    label1.pack()
    label2 = Label(fen, text=n)
    label2.pack()
    label3 = Label(fen, text=o)
    label3.pack()
    label4 = Label(fen, text=p)
    label4.pack()
    label5 = Label(fen, text=q)
    label5.pack()
    label6 = Label(fen, text=r)
    label6.pack()
    label7 = Label(fen, text=s)
    label7.pack()
    label8 = Label(fen, text=t)
    label8.pack()
    label9 = Label(fen, text=u)
    label9.pack()
    label10 = Label(fen, text=v)
    label10.pack()
    label11 = Label(fen, text=w)
    label11.pack()
    label12 = Label(fen, text=x)
    label12.pack()
    
    

   
        
        

      
            



fen = Tk()


start=Button(fen, text="commencer", command=commencer)
start.pack()


        
fen.mainloop()

   
