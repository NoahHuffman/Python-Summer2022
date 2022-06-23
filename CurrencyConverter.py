from tkinter import *
from CurrencyClass import Currency
from PIL import Image, ImageTk
def main():

    window = Tk()
    window.geometry("450x300")
    window.title("Currency Converter")
    # bgphoto = ImageTk.PhotoImage(file = 'bgimage1.png')
    # label1 = Label( window, image = bgphoto)
    # label1.place(x = 0, y = 0) 

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
    title = Label(window,text="Currency Converter",font=('Calibri 19'),bg="blue",fg="yellow")
    amtTxt = Label(window,text="  Amount  ",font=('Calibri 16'),fg="blue")
    amt = Entry(window,text="Enter Amount")
    result = Label(window,text=" result ",font=('Calibri 16'),fg="black")
    f = Label(window,text="  From  ",font=('Calibri 16'),fg="blue")
    t = Label(window,text="  To  ",font=('Calibri 16'),fg="blue")
    btn = Button(window, text="CONVERT",bg="grey",fg="black")
    
    #Displaying Widgets
    title.grid(row=0,column=0,columnspan=2,sticky=EW)
    result.grid(row=4,column=1,pady=20,sticky=EW)
    amt.grid(row=1,column=1)
    btn.grid(row=4,column=0)

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
    drop1.config(width=20,height=2)
    drop2.config(width=20,height=2)
    amtTxt.config(width=20,height=2)
    f.config(width=20,height=2)
    t.config(width=20,height=2)
    amtTxt.grid(row=1,column=0,sticky=W)
    f.grid(row=2,column=0,sticky=W)
    t.grid(row=3,column=0,sticky=W)
    drop1.grid(row=2,column=1,padx=60)
    drop2.grid(row=3,column=1)



    window.mainloop()

main()