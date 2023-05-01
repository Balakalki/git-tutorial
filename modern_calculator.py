import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('500x380')
root.title('calculator')
txbox=tk.Text(root,height=3,bg='AntiqueWhite2',fg='black',font=('Arial',19))
txbox.pack(padx=20,pady=20)
frbox=tk.Frame(root)

frbox.columnconfigure(0,weight=1)
frbox.columnconfigure(1,weight=1)
frbox.columnconfigure(2,weight=1)
frbox.columnconfigure(3,weight=1)

def click_button(txt):
    txbox.insert(tk.END,txt)
def ac():
    txbox.delete('1.0',tk.END)
btnac=tk.Button(frbox,text='AC',bg='orange',fg='red',font=('Arial',15),command=ac)
btnac.grid(row=0,column=0,sticky=tk.W+tk.E)

btnemt=tk.Button(frbox,text='emt',font=('Arial',15))
btnemt.grid(row=0,column=1,sticky=tk.W+tk.E)

btnmod=tk.Button(frbox,text='%',bg='aquamarine4',font=('Arial',15),command=lambda:click_button('%'))
btnmod.grid(row=0,column=2,sticky=tk.W+tk.E)

btnby=tk.Button(frbox,text='/',bg='aquamarine4',font=('Arial',15),command=lambda:click_button('/'))
btnby.grid(row=0,column=3,sticky=tk.W+tk.E)

btn1=tk.Button(frbox,text='1',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(1))
btn1.grid(row=3,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(frbox,text='2',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(2))
btn2.grid(row=3,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(frbox,text='3',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(3))
btn3.grid(row=3,column=2,sticky=tk.W+tk.E)

btnp=tk.Button(frbox,text='+',bg='aquamarine4',font=('Arial',15),command=lambda:click_button('+'))
btnp.grid(row=3,column=3,sticky=tk.W+tk.E)

btnm=tk.Button(frbox,text='X',bg='aquamarine4',font=('Arial',15),command=lambda:click_button('*'))
btnm.grid(row=1,column=3,sticky=tk.W+tk.E)

btn4=tk.Button(frbox,text='4',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(4))
btn4.grid(row=2,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(frbox,text='5',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(5))
btn5.grid(row=2,column=1,sticky=tk.W+tk.E)

btn6=tk.Button(frbox,text='6',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(6))
btn6.grid(row=2,column=2,sticky=tk.W+tk.E)

btnmin=tk.Button(frbox,text='-',bg='aquamarine4',font=('Arial',15),command=lambda:click_button('-'))
btnmin.grid(row=2,column=3,sticky=tk.W+tk.E)

btn7=tk.Button(frbox,text='7',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(7))
btn7.grid(row=1,column=0,sticky=tk.W+tk.E)

btn8=tk.Button(frbox,text='8',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(8))
btn8.grid(row=1,column=1,sticky=tk.W+tk.E)

btn9=tk.Button(frbox,text='9',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(9))
btn9.grid(row=1,column=2,sticky=tk.W+tk.E)

btn0=tk.Button(frbox,text='0',bg='CadetBlue1',fg='black',font=('Arial',15),command=lambda:click_button(0))
btn0.grid(row=4,column=0,sticky=tk.W+tk.E)

btndot=tk.Button(frbox,text='.',bg='goldenrod2',font=('Arial',15),command=lambda:click_button('.'))
btndot.grid(row=4,column=1,sticky=tk.W+tk.E)

def dl():
    dlt=txbox.get('1.0',tk.END)[:-2]
    txbox.delete('1.0',tk.END)
    txbox.insert('1.0',dlt)

btnback=tk.Button(frbox,text='del',bg='DeepPink1',font=('Arial',15),command=dl)
btnback.grid(row=4,column=2,sticky=tk.W+tk.E)

def eql():
    a=True
    while(a==True):
        try:
            res=eval(txbox.get('1.0',tk.END))
            txbox.delete('1.0',tk.END)
            txbox.insert('1.0',res)
            a=False
        except Exception as e:
            if txbox.get('1.0',tk.END)[0]=='0':
                s=txbox.get('1.0',tk.END)[1:]
                txbox.delete('1.0',tk.END)
                txbox.insert('1.0',s)
            else:
                txbox.delete('1.0',tk.END)
                txbox.insert('1.0','Error')
                a=False

btneq=tk.Button(frbox,text='=',bg='blue',fg='white',font=('Arial',15),command=eql)
btneq.grid(row=4,column=3,sticky=tk.W+tk.E)

frbox.pack(fill='x',padx=20,pady=20)

root.mainloop()