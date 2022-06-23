from tkinter import *
from CurrencyClass import Currency
from PIL import Image, ImageTk
def main():

    window = Tk()
    window.geometry("500x500")
    window.title("Currency Converter")
    # bgphoto = ImageTk.PhotoImage(file = 'bgimage1.png')
    # label1 = Label( window, image = bgphoto)
    # label1.place(x = 0, y = 0) 

    def pressBtn(num):
        pass



    #Getting list of countries
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

    #Creating Widgets
    title = Label(window,text="Currency Converter",font=('Calibri 19'),bg="black")
    amtTxt = Label(window,text="  Amount  ",font=('Calibri 16'),fg="blue")
    amt = Entry(window,text="Enter Amount")
    result = Label(window,text=" result ",font=('Calibri 16'),fg="black")
    f = Label(window,text="  From  ",font=('Calibri 16'),fg="blue")
    t = Label(window,text="  To  ",font=('Calibri 16'),fg="blue")
    btn = Button(window, text="CONVERT",bg="grey",fg="black",width=14,height=3)
    
    #Displaying Widgets
    title.grid(row=0,column=0,columnspan=3,sticky=EW)
    result.grid(row=6,column=1,pady=20,columnspan=2,sticky=W)
    amt.grid(row=1,column=1)
    btn.grid(row=6,column=0)

    #Make content span enter window.
    window.grid_columnconfigure(0,weight=1)

    #################################
    #################################
            # DROP DOWN MENU
    # datatype of menu text
    dropFrom = StringVar()
    dropTo = StringVar()
    
    # initial menu text
    dropFrom.set( countries[0] )
    dropTo.set( countries[0] )
    
    # Create Dropdown menu
    drop1 = OptionMenu( window , dropFrom , *countries )
    drop2 = OptionMenu( window , dropTo , *countries )
    drop1.config(width=20,height=3)
    drop2.config(width=20,height=3)
    amtTxt.config(width=20,height=3)
    f.config(width=20,height=3)
    t.config(width=20,height=3)
    amtTxt.grid(row=1,column=0,sticky=W)
    f.grid(row=2,column=0,sticky=W)
    t.grid(row=3,column=0,sticky=W)
    drop1.grid(row=2,column=1,pady=13,padx=10)
    drop2.grid(row=3,column=1,pady=13,padx=10)





    buttonFrame = Frame(window)
    buttonFrame.grid(row=4,column=0,columnspan=6)
    
    #KeyPad
    btn1 = Button(buttonFrame,text="1",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(1))
    btn1.grid(row=0,column=0,padx=10,pady=5)
    btn2 = Button(buttonFrame,text="2",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(2))
    btn2.grid(row=0,column=1,padx=10,pady=5)
    btn3 = Button(buttonFrame,text="3",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(3))
    btn3.grid(row=0,column=2,padx=10,pady=5)
    btn4 = Button(buttonFrame,text="4",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(4))
    btn4.grid(row=0,column=3,padx=10,pady=5)
    btn5 = Button(buttonFrame,text="5",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(5))
    btn5.grid(row=0,column=4,padx=10,pady=5)
    btn6 = Button(buttonFrame,text="6",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(6))
    btn6.grid(row=0,column=5,padx=10,pady=5)
    btn7 = Button(buttonFrame,text="7",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(7))
    btn7.grid(row=1,column=0,padx=10,pady=5)
    btn8 = Button(buttonFrame,text="8",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(8))
    btn8.grid(row=1,column=1,padx=10,pady=5)
    btn9 = Button(buttonFrame,text="9",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(9))
    btn9.grid(row=1,column=2,padx=10,pady=5)
    btn0 = Button(buttonFrame,text="0",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(0))
    btn0.grid(row=1,column=3,padx=10,pady=5)
    btndot = Button(buttonFrame,text=".",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn("."))
    btndot.grid(row=1,column=4,padx=10,pady=5)
    btnClear = Button(buttonFrame,text="C",width=4,bg='light blue',font=('Calibri 18'),command=pressBtn(""))
    btnClear.grid(row=1,column=5,padx=10,pady=5)




    window.mainloop()

main()
