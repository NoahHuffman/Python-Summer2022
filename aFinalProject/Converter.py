from tkinter import *
from CurrencyClass import Currency
from PIL import Image, ImageTk
def main():

    window = Tk()
    window.geometry("525x375")
    window.title("Currency Converter")


    def changeCountryFrom(event):
        ################FLAG
        flagFile = str(countries[countryFrom.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgfrom=Image.open(flag)
        render1 = ImageTk.PhotoImage(imgfrom)
        imgLblfrom = Label(window,image=render1)
        imgLblfrom.grid(row=2,column=0,sticky=NSEW)
        window.mainloop()
        ################FLAG


    def changeCountryTo(event):
        ################FLAG
        flagFile = str(countries[countryTo.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgto=Image.open(flag)
        render2 = ImageTk.PhotoImage(imgto)
        imgLblto = Label(window,image=render2)
        imgLblto.grid(row=2,column=3,sticky=NSEW)
        window.mainloop()
        ################FLAG
  

    #####################
    ####Exchrate File
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
    ####End Exchrate File
    #####################

        
    title = Label(window,text="Currency Converter",font=('Calibri 19'),bg="blue",fg="yellow")
    cfrom = Label(window,text="  Convert from  ",font=('Calibri 16'),bg="yellow",fg="blue")
    cto = Label(window,text=  "       to       ",font=('Calibri 16'),bg="yellow",fg="blue")
    amt = Label(window,text=" ",font=('Calibri 16'),bg="black",fg="yellow")
    result = Label(window,text=" ",font=('Calibri 16'),bg="black",fg="yellow")
    
    imgfrom = Image.open("america.jpg")
    render1 = ImageTk.PhotoImage(imgfrom)
    imgto = Image.open("america.jpg")
    render2 = ImageTk.PhotoImage(imgto)
    imgLblfrom = Label(window,image=render1)
    imgLblto = Label(window,image=render2)
          
    title.grid(row=0, column=0, columnspan=6,sticky=NSEW)
    
    cfrom.grid(row=1, column=0, sticky=NSEW)
    cto.grid(row=1, column=3, sticky=NSEW)
    amt.grid(row=1, column=1, columnspan=2, sticky=NSEW)
    result.grid(row=1, column=4, columnspan=2, sticky=NSEW)
    imgLblfrom.grid(row=2,column=0,sticky=NSEW)
    imgLblto.grid(row=2,column=3,sticky=NSEW)

    yscroll1 = Scrollbar(window,orient=VERTICAL)
    yscroll1.grid(row=2,column=1,sticky=NSEW)
    conOfCountryFrom = StringVar()
    countryFrom = Listbox(window,exportselection=0,listvariable=conOfCountryFrom,yscrollcommand=yscroll1.set)    
    countryFrom.grid(row=2,column=2,sticky=E)
    conOfCountryFrom.set(tuple(countries))
    countryFrom.bind("<<ListboxSelect>>", changeCountryFrom)
    yscroll1["command"] = countryFrom.yview
    
    yscroll2 = Scrollbar(window,orient=VERTICAL)
    yscroll2.grid(row=2,column=4,sticky=NSEW)
    conOfCountryTo = StringVar()
    countryTo = Listbox(window,exportselection=0,listvariable=conOfCountryTo,yscrollcommand=yscroll2.set)
    countryTo.grid(row=2,column=5,sticky=E)
    conOfCountryTo.set(tuple(countries))
    countryTo.bind("<<ListboxSelect>>", changeCountryTo)
    yscroll2["command"] = countryTo.yview
    
    # make a new frame
    buttonFrame = Frame(window)
    buttonFrame.grid(row=3,column=0,columnspan=6)
    
    #KeyPad
    btn1 = Button(buttonFrame,text="1",width=4,bg='light blue',font=('Calibri 18'))
    btn1.grid(row=0,column=0,padx=10,pady=5)
    btn2 = Button(buttonFrame,text="2",width=4,bg='light blue',font=('Calibri 18'))
    btn2.grid(row=0,column=1,padx=10,pady=5)
    btn3 = Button(buttonFrame,text="3",width=4,bg='light blue',font=('Calibri 18'))
    btn3.grid(row=0,column=2,padx=10,pady=5)
    btn4 = Button(buttonFrame,text="4",width=4,bg='light blue',font=('Calibri 18'))
    btn4.grid(row=0,column=3,padx=10,pady=5)
    btn5 = Button(buttonFrame,text="5",width=4,bg='light blue',font=('Calibri 18'))
    btn5.grid(row=0,column=4,padx=10,pady=5)
    btn6 = Button(buttonFrame,text="6",width=4,bg='light blue',font=('Calibri 18'))
    btn6.grid(row=0,column=5,padx=10,pady=5)
    btn7 = Button(buttonFrame,text="7",width=4,bg='light blue',font=('Calibri 18'))
    btn7.grid(row=1,column=0,padx=10,pady=5)
    btn8 = Button(buttonFrame,text="8",width=4,bg='light blue',font=('Calibri 18'))
    btn8.grid(row=1,column=1,padx=10,pady=5)
    btn9 = Button(buttonFrame,text="9",width=4,bg='light blue',font=('Calibri 18'))
    btn9.grid(row=1,column=2,padx=10,pady=5)
    btn0 = Button(buttonFrame,text="0",width=4,bg='light blue',font=('Calibri 18'))
    btn0.grid(row=1,column=3,padx=10,pady=5)
    btndot = Button(buttonFrame,text=".",width=4,bg='light blue',font=('Calibri 18'))
    btndot.grid(row=1,column=4,padx=10,pady=5)
    btnClear = Button(buttonFrame,text="C",width=4,bg='light blue',font=('Calibri 18'))
    btnClear.grid(row=1,column=5,padx=10,pady=5)
        
    countryFrom.selection_set(first=0)
    countryTo.selection_set(first = 0)
    window.mainloop()
    
main()