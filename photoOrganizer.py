# Author:  D.J. Platt
# Date:    Mar 2021
# Purpose: Copy photos to YYYY/MM/DD directory structure
#
import os
import shutil
from tkinter import *
from exif import Image
from tkinter import filedialog
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
    extList = ['jpg', 'NEF', 'png', 'ARW','JPG','gif','jpeg']
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
        home = "/home/david/Pictures"
    else:
        slash = "\\"
        home = "C:\\Users\\user\\Pictures"

    print(getOS())
    #
    ## ensure that the directory structure is in place
    #
    dayDir = ''
    for file in os.listdir(home):
        fname = home + slash + file
        if os.path.isfile(fname):
            if isPicture(file):
                my_image = Image(fname)
                print(my_image.datetime_original)
                yearDir = home + slash + (getYear(my_image.datetime_original))
                monthDir = yearDir + slash + (getMonth(my_image.datetime_original))
                dayDir = monthDir + slash + (getDay(my_image.datetime_original))

                isDay = os.path.isdir(dayDir)
                if isDay:
                    pass   
                else:
                    isMonth = os.path.isdir(monthDir)
                    if isMonth:
                        pass
                    else:
                        isYear = os.path.isdir(yearDir)
                        if isYear:
                            pass
                        else:
                            print("Creating " + yearDir)
                            os.mkdir(yearDir)

                        print("Creating " + monthDir)
                        os.mkdir(monthDir)

                    print("Creating " + dayDir)
                    os.mkdir(dayDir)
    #
    #  don't copy the fole if it exists already
    #
            destfile = dayDir + slash + file
            if os.path.isfile(destfile):
                print('skipping')
            else:
                shutil.copyfile(fname,destfile)


###############################################################################
#
# Create the root window
#
window = Tk()
window.title('Photo Organizer')
window.geometry("500x500")
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
button_copy.place(x=300,y=400)  
button_exit.place(x=400,y=400)
#
# Let the window wait for any events
#
window.mainloop()
