import os
from Tkinter import *

def show_entry_fields():
    command = "ping -c 1 -q "
    syscommand = command + e1.get() + "." + e2.get() + "." + e3.get() + "."
    redirect = " >> /tmp/pinger.dat"
    for i in range (1,256):
        print("%s" % syscommand + str(i))
        os.system(syscommand + str(i) + redirect)
  

master = Tk()
Label(master, text="Octet 1").grid(row=0)
Label(master, text="Octet 2").grid(row=1)
Label(master, text="Octet 3").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.insert(10,"104")
e2.insert(10,"207")
e3.insert(10,"136")

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
