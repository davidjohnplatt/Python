#
#   Author: D.J. Platt
#     Date: April 2021
# Function: Make sure all files in a source directory tree are in the other. Note
#           that files are not compared by characteristics - existance is all. 
#
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext 
# 
# Set the directory you want to start from, go to and whether to actually copy the files
# Not copying files is useful when testing the settings for the source and destination directories
#

def findSource():
    img_dir = filedialog.askdirectory()
    dirName.set(img_dir)
    os.chdir(img_dir)
   
    
def findDestRoot():
    img_dir = filedialog.askdirectory()
    destName.set(img_dir)
    
def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)
    
def process():
    sourceDir = '/home/david/Pictures'
    lenSource = len(sourceDir)
    targetDir = '/home/david/Gdrive/Pictures'
    copyFile = False

    logFile = open('logFile.txt' , 'w')
                    
    for dirName, subdirList, fileList in os.walk(sourceDir):
        print('Found directory: %s' % dirName)
        logFile.write('Found directory: %s\n' % dirName)
        newDir = targetDir + dirName[lenSource:]
    #
    #  check to see if the directory exists on the target side and make it if required
    #
        isDir = os.path.isdir(newDir)            
        if isDir:
            pass
        else:
            if (copyFile):
                os.mkdir(newDir)
        
        for fname in fileList:        
            destfile = newDir + '/' + fname
            srcFile = dirName + '/' + fname
                    
            if os.path.isfile(destfile):
                pass
            else:
                if (copyFile):
                    logFile.write('\tCopying %s to %s \n' % (srcFile,  destfile))
                    shutil.copyfile(srcFile,destfile)
                else:
                    logFile.write('\tTest mode %s to %s \n' % (srcFile,  destfile))
    print('End Process')               
    logFile.close()                  
            
###############################################################################
#
# Create the root window
#
window = Tk()
window.title('CopyTree')
window.geometry("500x700")
window.config(background = "white")
var = 1
#  
# screen element definition
#
label_file_explorer = Label(window,text = "CopyTree",font=("arial italic", 18),width = 26, height = 3, fg = "blue",bg="yellow") 
button_src = Button(window, text = "Select Source Directory", command = findSource)
button_dest = Button(window, text = "Select Destination Directory", command = findDestRoot)
dirName = StringVar()
srcDirText = Entry(window, width = 50, textvariable = dirName)
destName = StringVar()
destDirText = Entry(window, width = 50, textvariable = destName)
textArea = scrolledtext.ScrolledText(window, width = 70, height = 15,font = ("Helvetica",8))
R1 = Radiobutton(window, text="Live", variable=var, value=1,command=sel)
R2 = Radiobutton(window, text="Test", variable=var, value=2,command=sel)
button_copy = Button(window, text = "Copy",command = process) 
#  
# place screen elements
#
label_file_explorer.place(x = 50, y = 20)
button_src.place(x=150,y=150)
srcDirText.place(x=50,y=200)
button_dest.place(x=135, y=250)
destDirText.place(x=50,y=300)
textArea.place(x=50,y=350)
R1.place(x=200,y=600)
R2.place(x=200,y=620)
button_copy.place(x=300,y=600)  
#
# Let the window wait for any events
#
window.mainloop()        


