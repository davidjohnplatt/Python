from tkinter import *

def displayError(errorString):
    e6.insert(0,errorString)

def getPrice():
    if len(e1.get()) == 0: 
        return 0
    else:
        return float(e1.get())

def getKilos():
    if len(e2.get()) == 0: 
        return 0
    else:
        return float(e2.get())

def getPounds():
    if len(e3.get()) == 0: 
        return 0.0
    else:
        return float(e3.get())

def getMgs():
    if len(e4.get()) == 0: 
        return 0.0
    else:
        return float(e4.get())
    
def clearFields():
    e5.delete(0, END)

 
def poundsToKilos(pounds):
   return  pounds / 2.205

def poundsToGrams(pounds):
   return  pounds / 2.205 * 1000

def kilosToMgs(kilos):
   return  kilos / 1000

def kilosToPounds(kilos):
   return float(kilos) * 2.2
 
def kilosToGrams(kilos):
   return kilos * 1000

def gramsToKilos(grams):
    return grams / 1000

def gramsToPounds(grams):
    return grams / 1000 * 2.2

def recalc():
    prime = 0
    
    price = getPrice()
    if price == 0:
        prime = 3

    kilos = getKilos()
    if kilos == 0:       
        prime = prime + 5
      
    lbs = getPounds()   
    if  lbs == 0:
        prime = prime + 7
        
    mgs = getMgs()
    if mgs == 0:
        prime = prime + 11
        
    displayError (prime)    
#    displayError(prime)
    
    if prime == 3:
       displayError("Error - price must be entered")
    elif prime == 5:
        e2.delete(0, END)
        kilos = poundsToKilos(lbs)
        e2.insert(0,kilos)
        e4.insert(0,kilosToGrams(kilos))
    elif prime == 7:
        e3.delete(0, END)
        e3.insert(0,kilosToPounds(kilos))
        e4.insert(0,kilosToGrams(kilos))
    elif prime == 11:
        e4.delete(0, END)
        e4.insert(0,kilosToGrams(kilos))
    elif prime == 12:
         e2.delete(0, END)
         e2.insert(0,gramsToKilos(mgs))
         e3.delete(0, END)
         e3.insert(0,gramsToPounds(mgs))
    elif prime == 16:
         e2.delete(0, END)
         e2.insert(0,poundsToKilos(lbs))
         e4.delete(0, END)
         e4.insert(0,poundsToGrams(lbs))
    elif prime == 18:
        e3.delete(0, END)
        e3.insert(0,kilosToPounds(kilos))
        e4.delete(0, END)
        e4.insert(0,kilosToGrams(kilos))
    
        
    unitCost = kilos / price
    e5.delete(0,END)
    e5.insert(0,unitCost)
            

#    e3.insert(0, kilosToPounds(getPounds()) )
#    clearFields()
 #   e5.insert(0, kilosToPounds(getKilos()) / getPrice())
 
#print poundsToKilos(1)
#print kilosToPounds(1)
#print kilosToGrams(1)
 
master = Tk()
master.title("Unit Cost Converter")

Label(master, text="Price").grid(row=0, column=5)
Label(master, text="Kilos").grid(row=1, column=5)
Label(master, text="Pounds").grid(row=2, column=5)
Label(master, text="Mgs").grid(row=3, column=5)
Label(master, text="Unit Cost").grid(row=5, column=5)
Label(master, text="Error").grid(row=8, column=5)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)

e1.grid(row=0, column=10)
e2.grid(row=1, column=10)
e3.grid(row=2, column=10)
e4.grid(row=3, column=10)
e5.grid(row=5, column=10)
e6.grid(row=8, column=10)


Button(master, text='Quit', command=master.quit).grid(row=9, column=0, sticky=W, pady=4)
Button(master, text='ReCalc', command=recalc).grid(row=9, column=20, sticky=W, pady=4)
 
mainloop( )
