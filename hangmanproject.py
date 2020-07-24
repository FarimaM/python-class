###code porozhe hangman _farima moghaddam##
from tkinter import *
import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.title("Hnamgman Game")
win.geometry('650x250')
win.resizable(False,False)


chances=4
##tarife tabe ke widget button hara modiriyat mikonad##
def push(alphabet):
    global chances
    answer= "PYTHON"
    if alphabet in answer:
        if alphabet=="P":
            btn01["text"] = alphabet
        elif alphabet=="Y":
            btn02["text"] = alphabet
        elif alphabet=="T":
            btn03["text"] = alphabet
        elif alphabet=="H":
            btn04["text"] = alphabet
        elif alphabet=="O":
            btn05["text"] = alphabet
        elif alphabet=="N":
            btn06["text"] = alphabet
    else:
        txt="Chances remaining "+str(chances)
        label1.configure(text=txt)
        chances = chances - 1
        if chances<0:
            messagebox.showinfo("Loose to guess","Game Over:((")
##sharti ast ke agar hame huroofe dakhele kalame ra dorost hads bzanad##            
            
    if btn01["text"]=="P" and btn02["text"]=="Y" and btn03["text"]=="T" and btn04["text"]=="H" and btn05["text"]=="O" and btn06["text"]=="N":
        messagebox.showinfo("congratulations", "You are Win^__^")
        
    print(chances)




btn01 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn01.place(x=250, y=50,width = 50, height =50)
btn02 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn02.place(x=300, y=50,width = 50, height =50)
btn03 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn03.place(x=350, y=50,width = 50, height =50)
btn04 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn04.place(x=400, y=50,width = 50, height =50)
btn05 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn05.place(x=450, y=50,width = 50, height =50)
btn06 = Button(win, text=" ",bg="white", fg="Black",font=('mitra','20'))
btn06.place(x=500, y=50,width = 50, height =50)





btn1=tk.Button(win,text='A',font=('Helvetica','20'),command=lambda: push("A"))
btn1.place(x=0,y=150,width = 50, height =50)

btn2=tk.Button(win,text='B',font=('Helvetica','20'),command=lambda: push("B"))
btn2.place(x =50, y =150,width = 50, height =50)
btn3=tk.Button(win,text='C',font=('Helvetica','20'),command=lambda: push("C"))
btn3.place(x =100, y =150,width=50,height=50)
btn4=tk.Button(win,text='D',font=('Helvetica','20'),command=lambda: push("D"))
btn4.place(x =150, y =150,width=50,height=50)
btn5=tk.Button(win,text='E',font=('Helvetica','20'),command=lambda: push("E"))
btn5.place(x =200, y =150,width=50,height=50)
btn6=tk.Button(win,text='F',font=('Helvetica','20'),command=lambda: push("F"))
btn6.place(x =250, y =150,width=50,height=50)
btn7=tk.Button(win,text='G',font=('Helvetica','20'),command=lambda: push("G"))
btn7.place(x =300, y =150,width=50,height=50)
btn8=tk.Button(win,text='H',font=('Helvetica','20'),command=lambda: push("H"))
btn8.place(x =350, y =150,width=50,height=50)
btn9=tk.Button(win,text='I',font=('Helvetica','20'),command=lambda: push("I"))
btn9.place(x =400, y =150,width=50,height=50)
btn10=tk.Button(win,text='J',font=('Helvetica','20'),command=lambda: push("J"))
btn10.place(x =450, y =150,width=50,height=50)
btn11=tk.Button(win,text='K',font=('Helvetica','20'),command=lambda: push("K"))
btn11.place(x =500, y =150,width=50,height=50)
btn12=tk.Button(win,text='L',font=('Helvetica','20'),command=lambda: push("L"))
btn12.place(x =550, y =150,width=50,height=50)
btn13=tk.Button(win,text='M',font=('Helvetica','20'),command=lambda: push("M"))
btn13.place(x =600, y =150,width=50,height=50)
btn14=tk.Button(win,text='N',font=('Helvetica','20'),command=lambda: push("N"))
btn14.place(x =0, y =200,width=50,height=50)
btn15=tk.Button(win,text='O',font=('Helvetica','20'),command=lambda: push("O"))
btn15.place(x =50, y =200,width=50,height=50)
btn16=tk.Button(win,text='P',font=('Helvetica','20'),command=lambda: push("P"))
btn16.place(x =100, y =200,width=50,height=50)
btn17=tk.Button(win,text='Q',font=('Helvetica','20'),command=lambda: push("Q"))
btn17.place(x =150, y =200,width=50,height=50)
btn18=tk.Button(win,text='R',font=('Helvetica','20'),command=lambda: push("R"))
btn18.place(x =200, y =200,width=50,height=50)
btn19=tk.Button(win,text='S',font=('Helvetica','20'),command=lambda: push("S"))
btn19.place(x =250, y =200,width=50,height=50)
btn20=tk.Button(win,text='T',font=('Helvetica','20'),command=lambda: push("T"))
btn20.place(x =300, y =200,width=50,height=50)
btn21=tk.Button(win,text='U',font=('Helvetica','20'),command=lambda: push("U"))
btn21.place(x =350, y =200,width=50,height=50)
btn22=tk.Button(win,text='V',font=('Helvetica','20'),command=lambda: push("V"))
btn22.place(x =400, y =200,width=50,height=50)
btn23=tk.Button(win,text='W',font=('Helvetica','20'),command=lambda: push("W"))
btn23.place(x =450, y =200,width=50,height=50)
btn24=tk.Button(win,text='X',font=('Helvetica','20'),command=lambda: push("X"))
btn24.place(x =500, y =200,width=50,height=50)
btn25=tk.Button(win,text='Y',font=('Helvetica','20'),command=lambda: push("Y"))
btn25.place(x =550, y =200,width=50,height=50)
btn26=tk.Button(win,text='Z',font=('Helvetica','20'),command=lambda: push("Z"))
btn26.place(x =600, y =200,width=50,height=50)
label1=Label(win,text="Total Chances are : 4")
label1.place(x=0,y=0)
win.mainloop()
