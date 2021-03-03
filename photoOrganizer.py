# Author:  D.J. Platt
# Date:    Mar 2021
# Purpose: Copy photos to YYYY/MM/DD directory structure
#
import os
import shutil
from tkinter import *
from exif import Image
from tkinter import filedialog
from tkinter import scrolledtext 
#
########################################################################
#
def getYear(dstring):
    return (dstring[0:4])

def getMonth(dstring):
    return (dstring[5:7])

def getDay(dstring):
    return (dstring[8:10])

def getOS():
    return os.name

def extension(x):
    ext=x.split(".")
    return (ext[1])

def isPicture(lname):
    extList = ['jpg', 'JPG','jpeg']
    for i in extList:
       if extension(lname) == i:
          return True

def findSource():
    img_dir = filedialog.askdirectory()
    dirName.set(img_dir)
    os.chdir(img_dir)
   
    
def findDestRoot():
    img_dir = filedialog.askdirectory()
    destName.set(img_dir)
   

def process():
    if getOS() == "posix":
        slash = "/"
    else:
        slash = "\\"

    print(getOS())
    src = srcDirText.get()
    dest = destDirText.get()
    print (src)
    dayDir = ''
    #
    #  iterate over all files in the source directory
    #
    for file in os.listdir(src):
        fname = src + slash + file
    #
    #  if it is not a directory and is a picturefile ...
    #
        if os.path.isfile(fname):
            if isPicture(file):
                my_image = Image(fname)
                print(my_image.datetime_original)
    #
    #  determine what the names of the destination directories should be
    #
                yearDir = dest + slash + (getYear(my_image.datetime_original))
                monthDir = yearDir + slash + (getMonth(my_image.datetime_original))
                dayDir = monthDir + slash + (getDay(my_image.datetime_original))
    #
    #  check to see if the year/month/day directories exist and create them if not
    #
                isYear = os.path.isdir(yearDir)            
                if isYear:
                    pass
                else:
                    textArea.insert('insert','Creating ' + yearDir + '\n')
                    os.mkdir(yearDir)
                    
                isMonth = os.path.isdir(monthDir)    
                if isMonth:
                    pass
                else:
                    textArea.insert('insert','Creating ' + monthDir + '\n')
                    os.mkdir(monthDir)
                   
                isDay = os.path.isdir(dayDir)
                if isDay:
                    pass
                else:
                    textArea.insert('insert','Creating ' + dayDir + '\n')
                    os.mkdir(dayDir)
    #
    #  don't copy the file if it exists already
    #
                destfile = dayDir + slash + file
                print (destfile)
                if os.path.isfile(destfile):
                    print('skipping')
                else:
                    shutil.copyfile(fname,destfile)
                    textArea.insert('insert','Copying ' +  destfile + '\n')
###############################################################################
#
# Create the root window
#
window = Tk()
window.title('Photo Organizer')
window.geometry("500x700")
window.config(background = "white")
#  
# screen element definition
#
label_file_explorer = Label(window,text = "Photo Organizer",width = 50, height = 4, fg = "blue") 
button_src = Button(window, text = "Select Source Directory", command = findSource)
button_dest = Button(window, text = "Select Destination Directory", command = findDestRoot)
dirName = StringVar()
srcDirText = Entry(window, width = 50, textvariable = dirName)
destName = StringVar()
destDirText = Entry(window, width = 50, textvariable = destName)
textArea = scrolledtext.ScrolledText(window, width = 70, height = 10,font = ("Helvetica",8)) 
button_copy = Button(window, text = "Copy",command = process) 
button_exit = Button(window, text = "Exit",command = exit) 
#  
# place screen elements
#
label_file_explorer.place(x = 50, y = 20)
button_src.place(x=150,y=150)
srcDirText.place(x=50,y=200)

button_dest.place(x=135, y=250)
destDirText.place(x=50,y=300)
textArea.place(x=50,y=350)
button_copy.place(x=300,y=600)  
button_exit.place(x=400,y=600)
#
# Let the window wait for any events
#
window.mainloop()
