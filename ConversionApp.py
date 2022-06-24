from ast import Expression
from ctypes import resize
from logging import root
from tkinter import *
from tkinter import font
from turtle import left, width
from PIL import Image,ImageTk
from CurrencyClass import Currency
from tkinter import ttk



expression = ''
#Button Functions

def record():
    content=entName.get()
    content=float(content)
    content="{0:s}{1:,.2f}".format('$',content)
    result["text"]=content
    

def pressNum(num):
    
    global expression
    expression = expression+str(num)
    equation.set(expression)
def clear():
    global expression
    expression = ''
    equation.set(expression)
    


def changeCountryFrom(event):
        ################FLAG
        flagFile = str(countries[countryFrom.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgfrom=Image.open(flag)
      #  imgfrom.resize((300,333),Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(imgfrom)
        imgLblfrom = Label(window,image=render1)
        imgLblfrom.grid(row=3,column=2,padx=10,sticky=W)
        window.mainloop()
        ################FLAG
def changeCountryTo(event):
        ################FLAG
        flagFile = str(countries[countryTo.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgto=Image.open(flag)
        render2 = ImageTk.PhotoImage(imgto)
        imgLblto = Label(window,image=render2)
        imgLblto.grid(row=3,column=5,padx=5,sticky=W)
        window.mainloop()
        ################FLAG



infile = open("Exchrate.txt")
countryDict = {}
countries = []
for line in infile:
    info = line.rstrip().split(',')
    currency = Currency(info[1],info[2]=="left",info[3]=="comma",float(info[4]))
    countryDict[info[0]] = currency
infile.close()
for c in countryDict.keys():
    countries.append(c)



window = Tk()
window.title("Currency Converter")

window.geometry('665x560')
window.iconbitmap('Conversion.ico')
bg = (PhotoImage(file = "Anotherbackground.png"))
bg2 =(PhotoImage(file='background2.png'))

label1 =Label(window,image=bg)
label1.place(x=0,y=0)


titleTop = Label(window,bg="salmon")
titleBot = Label(window,bg="salmon")
converMssg1 = Label(window,text="    Convert from     ")
converMss2 = Label(window,text= "       Convert to        ")
result = Label(window,text="")


titleTop.grid(row=0,column=0,columnspan=7,sticky=EW)
titleBot.grid(row=6,column=0,columnspan=7,sticky=EW)
converMssg1.grid(row=2,column=1,padx=10,pady=10,sticky=W)
converMss2.grid(row=2,column=4,padx=10,pady=10,sticky=W)
result.grid(row=2,column=5,padx=10,pady=5,sticky=EW)


buttonFrame = Frame(window)
background_frame = Label(buttonFrame)#,image=bg2)
background_frame.place(x=0,y=0)
buttonFrame.grid(row=5,column=0,columnspan=6,padx=100,pady=65)



#Flag images -- setting default
imgfrom = Image.open("america.jpg")
render1 = ImageTk.PhotoImage(imgfrom)
imgto = Image.open("america.jpg")
render2 = ImageTk.PhotoImage(imgto)
imgLblfrom = Label(window,image=render1)
imgLblto = Label(window,image=render2)
imgLblfrom.grid(row=3,column=2,padx=10,sticky=W)
imgLblto.grid(row=3,column=5,padx=5,sticky=W)



equation = StringVar()

#Entrybox for Buttons
conOfentNum = StringVar(window, value = equation)
entName = Entry(window,  textvariable=equation)
entName.grid(row=2,column=2,sticky=W)
entName.focus_set()


btn1 = Button(buttonFrame,text="1",width=4,bg='silver',font=('Calibri 18'),command=lambda: pressNum(1))
btn1.grid(row=0,column=0,padx=10,pady=5)
btn2 = Button(buttonFrame,text="2",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(2))
btn2.grid(row=0,column=1,padx=10,pady=5)
btn3 = Button(buttonFrame,text="3",width=4,bg='silver',font=('Calibri 18'),command= lambda:pressNum(3))
btn3.grid(row=0,column=2,padx=10,pady=5)
btn4 = Button(buttonFrame,text="4",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(4))
btn4.grid(row=1,column=0,padx=10,pady=5)
btn5 = Button(buttonFrame,text="5",width=4,bg='silver',font=('Calibri 18'),command= lambda:pressNum(5))
btn5.grid(row=1,column=1,padx=10,pady=5)
btn6 = Button(buttonFrame,text="6",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(6))
btn6.grid(row=1,column=2,padx=10,pady=5)

btn7 = Button(buttonFrame,text="7",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(7))
btn7.grid(row=3,column=0,padx=10,pady=5)
btn8 = Button(buttonFrame,text="8",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(8))
btn8.grid(row=3,column=1,padx=10,pady=5)
btn9 = Button(buttonFrame,text="9",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(9))
btn9.grid(row=3,column=2,padx=10,pady=5)
btn0 = Button(buttonFrame,text="0",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(0))
btn0.grid(row=1,column=3,padx=10,pady=5)
btndot = Button(buttonFrame,text=".",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum('.'))
btndot.grid(row=1,column=4,padx=10,pady=5)
btnClear = Button(buttonFrame,text="C",width=4,bg='silver',font=('Calibri 18'),command=lambda:clear())
btnClear.grid(row=1,column=5,padx=10,pady=5)


#Record button
btn_record = Button(buttonFrame,text="Record",width=16,bg='red',font=('Calibri 18'),command=lambda:record())
btn_record.grid(row=0,column=3,columnspan=3)

#Help button
btn_help = Button(buttonFrame,text="Help?", width=16,bg = 'silver', font=('Calibri 18'))
btn_help.grid(row=3, column=3, columnspan=3)

#ListBox Left Side
conOfCountryFrom = StringVar()
countryFrom = Listbox(window,exportselection=0,listvariable=conOfCountryFrom)    
countryFrom.grid(row=3,column=1,sticky=W)
conOfCountryFrom.set(tuple(countries))
countryFrom.bind("<<ListboxSelect>>", changeCountryFrom)

#Listboxt Right Side
conOfCountryTo = StringVar()
countryTo =Listbox(window,exportselection=0,listvariable=conOfCountryTo)
countryTo.grid(row=3,column=4,sticky=W,columnspan=1)
conOfCountryTo.set(tuple(countries))
countryTo.bind('<<ListboxSelect>>', changeCountryTo)


#Scrolls
scrollLS = Scrollbar(window,orient=VERTICAL)
scrollLS.grid(row=3,column=0,sticky=NSEW)
scrollLS["command"] = countryFrom.yview

scrollRS = Scrollbar(window,orient=VERTICAL)
scrollRS.grid(row=3,column=3,sticky=NSEW)
scrollRS['command']= countryTo.yview








countryFrom.selection_set(first=0)
countryTo.selection_set(first = 0)
window.mainloop()