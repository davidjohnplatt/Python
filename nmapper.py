#!/usr/bin/python
import os
import re
from Tkinter import *


def show_entry_fields():
    command = "nmap -sP "
    syscommand = command + " " + e1.get() + "." + e2.get() + "." + e3.get() + "." + e4.get()
    redirect = " > /tmp/nmapper.dat"
    os.system(syscommand + redirect)


def parseIP(line):
    ip_regex = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    return str(ip_regex)[2:findQuote(line,3)]

def executeCommand():
    command = "nmap  "
    syscommand = command + e5.get() + " " + e1.get() + "." + e2.get() + "." + e3.get() + "." + e4.get()
    os.system(syscommand)

def findSpace(line,pos):
    return line.find(" ", pos)

def findQuote(line,pos):
    return line.find("'", pos) - 1

def writePythonProg():
    ifile=open('/tmp/nmapper.dat', 'r')
    ofile=open("hostnmapper.py","w")
    ofile.write("import os\n")
    ofile.write("from Tkinter import *\n\n")

    ofile.write("def execSysCommand(lparm,lip):\n")
    ofile.write("    command = 'nmap -v '\n")
    ofile.write("    syscommand = command + lparm + ' ' + lip\n")
    ofile.write("    os.system(syscommand)\n\n")

    ofile.write("master = Tk()\n")
    ofile.write("master.title('Host Mapper')\n\n")
    i = 0
    while True:
        dline = ifile.readline()
        if not dline : break
        if len(dline) < 2:
            nulInstr = "TRUE"
        else:
            if dline[0:6] == "Nmap s":
                i = i + 1
                ip = parseIP(dline)
                print ip
                ofile.write("Label(master, text='Host " + str(i) + "').grid(row=" + str(i) + ")\n")
                ofile.write("e" + str(i) + " = Entry(master)\n")
                ofile.write("e" + str(i) + ".grid(row = " + str(i) + " , column = 2)\n")
                if len(ip) < 15:
                    ofile.write("e" + str(i) + ".insert(10,'" + ip + "')\n")
                ofile.write("Button(master, text='Stealth', command=lambda: execSysCommand('-sS','" + ip + "')).grid(row=" + str(i) + ", column=3, sticky=W, pady=4)\n")
                ofile.write("Button(master, text='Connect', command=lambda: execSysCommand('-sT','" + ip + "')).grid(row=" + str(i) + ", column=4, sticky=W, pady=4)\n")
                ofile.write("Button(master, text='Version', command=lambda: execSysCommand('-sV','" + ip + "')).grid(row=" + str(i) + ", column=5, sticky=W, pady=4)\n\n")
                ofile.write("Button(master, text='OS', command=lambda: execSysCommand('-O','" + ip + "')).grid(row=" + str(i) + ", column=6, sticky=W, pady=4)\n\n")
    ofile.write("mainloop()\n")
    ofile.flush()
    ifile.close()
    ofile.close()



master = Tk()
master.title("nMapper")

Label(master, text="Octet 1").grid(row=0)
Label(master, text="Octet 2").grid(row=1)
Label(master, text="Octet 3").grid(row=2)
Label(master, text="Octet 4").grid(row=3)
Label(master, text="Stealth(r)  -sS").grid(row=3,column=7)
Label(master, text="Pimg -sP").grid(row=4,column=7)
Label(master, text="Connect -sT").grid(row=5,column=7)
Label(master, text="Version -sV").grid(row=5,column=7)
Label(master, text="OS(r) -O").grid(row=6,column=7)
Label(master, text="Active Port Scan -Pn").grid(row=7,column=7)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.insert(5,"192")
e2.insert(5,"168")
e3.insert(5,"1")
e4.insert(7,"0/24")
e5.insert(7,"-sS -v")

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=1, column=7)

Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='NmapAll', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Execute', command=executeCommand).grid(row=1, column=6, sticky=W, pady=4)
Button(master, text='Hosts', command=writePythonProg).grid(row=5, column=2, sticky=W, pady=4)

mainloop( )

