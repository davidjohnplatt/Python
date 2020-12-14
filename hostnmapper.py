import os
from Tkinter import *

def execSysCommand(lparm,lip):
    command = 'nmap -v '
    syscommand = command + lparm + ' ' + lip
    os.system(syscommand)

master = Tk()
master.title('Host Mapper')

Label(master, text='Host 1').grid(row=1)
e1 = Entry(master)
e1.grid(row = 1 , column = 2)
e1.insert(10,'192.168.1.1')
Button(master, text='Stealth', command=lambda: execSysCommand('-sS','192.168.1.1')).grid(row=1, column=3, sticky=W, pady=4)
Button(master, text='Connect', command=lambda: execSysCommand('-sT','192.168.1.1')).grid(row=1, column=4, sticky=W, pady=4)
Button(master, text='Version', command=lambda: execSysCommand('-sV','192.168.1.1')).grid(row=1, column=5, sticky=W, pady=4)

Button(master, text='OS', command=lambda: execSysCommand('-O','192.168.1.1')).grid(row=1, column=6, sticky=W, pady=4)

Label(master, text='Host 2').grid(row=2)
e2 = Entry(master)
e2.grid(row = 2 , column = 2)
e2.insert(10,'192.168.1.3')
Button(master, text='Stealth', command=lambda: execSysCommand('-sS','192.168.1.3')).grid(row=2, column=3, sticky=W, pady=4)
Button(master, text='Connect', command=lambda: execSysCommand('-sT','192.168.1.3')).grid(row=2, column=4, sticky=W, pady=4)
Button(master, text='Version', command=lambda: execSysCommand('-sV','192.168.1.3')).grid(row=2, column=5, sticky=W, pady=4)

Button(master, text='OS', command=lambda: execSysCommand('-O','192.168.1.3')).grid(row=2, column=6, sticky=W, pady=4)

Label(master, text='Host 3').grid(row=3)
e3 = Entry(master)
e3.grid(row = 3 , column = 2)
e3.insert(10,'192.168.1.8')
Button(master, text='Stealth', command=lambda: execSysCommand('-sS','192.168.1.8')).grid(row=3, column=3, sticky=W, pady=4)
Button(master, text='Connect', command=lambda: execSysCommand('-sT','192.168.1.8')).grid(row=3, column=4, sticky=W, pady=4)
Button(master, text='Version', command=lambda: execSysCommand('-sV','192.168.1.8')).grid(row=3, column=5, sticky=W, pady=4)

Button(master, text='OS', command=lambda: execSysCommand('-O','192.168.1.8')).grid(row=3, column=6, sticky=W, pady=4)

mainloop()
