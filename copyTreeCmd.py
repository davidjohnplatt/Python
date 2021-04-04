#
#   Author: D.J. Platt
#     Date: April 2021
# Function: Make sure all files in a source directory tree are in the other. Note
#           that files are not compared - existance is all. This is non gui version
#
import os
import shutil
# 
# Set the directory you want to start from, go to and whether to actually copy the files
# Not copying files is useful when testing the settings for the source and destination directories
#
sourceDir = '/home/david/Pictures'
lenSource = len(sourceDir)
targetDir = '/home/david/Gdrive/Pictures'
lenTarget = len(targetDir)
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
        
        


