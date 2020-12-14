import Tkinter, tkFileDialog, MySQLdb, os, csv, sys
from dateutil.parser import parse
from decimal import Decimal

def insertInvestments(laccount):
    try:
        inscomm = "INSERT INTO investments (account,dateloaded,conversionrate,sector,symbol,quantity,price,currency,totalbookcost,totalmarketvalue,gainloss,averagecost,annualdividend,dividenddate) "\
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"  
        args = (laccount, gloaddate, currencyConv, gsector, gsymbol, gquantity, gprice, gcurrency,gtotalbookcost,gtotalmarketvalue,ggainloss,gaveragecost,gannualdividend,gdividenddate)
        cursor.execute(inscomm, args)
        db.commit()
    except Exception, e: 
         print "Error - insertInvestments"
         print repr(e)
         db.rollback()

def countName(lsymbol):
    try:
        lcursor = db.cursor()
        lcursor.execute("SELECT count(*) FROM symbolname where symbol = '%s'" % lsymbol)
        row = lcursor.fetchone()
        return row[0]
    except Exception, e:
        print "Error - countName"
        print repr(e)

def getBatchNum():
    try:
        lcursor = db.cursor()
        lcursor.execute("SELECT batchnum from batch")
        row = lcursor.fetchone()
        return row[0] + 1
        
    except Exception, e:
        print "Error - countName"
        print repr(e)


def insertCash(laccount):
    try:
        inscomm = "INSERT INTO investments (account,dateloaded,conversionrate,symbol,currency,totalbookcost,totalmarketvalue) "\
        " VALUES (%s, %s, %s, %s, %s, %s, %s)"  
        args = (laccount, gloaddate, currencyConv, 'Cash', gcurrency,0,gcash)
        cursor.execute(inscomm, args)
    except Exception, e: 
         print "Error - insertCash"
         print repr(e)
         db.rollback()


def insertSymbolname(lsymbol,lproduct,lname):
    try:
        inscomm = "INSERT INTO symbolname (symbol,product,name) "\
        " VALUES (%s, %s, %s)"  
        args = (lsymbol, lproduct, lname)
        cursor.execute(inscomm, args)
    except Exception, e: 
         print "Error - insertSymbolname"
         print repr(e)
         db.rollback()

def createWorkfile(lfilename):
    command = "grep ',,,,' " + lfilename  + " > /tmp/workfile"
    print command
    os.system(command)

def NVL(lstring, lreturn):
    if lstring == '':
        return lreturn
    else:
        return lstring  
    
def NA(lstring, lreturn):
    if lstring == 'N/A':
        return lreturn
    else:
        return lstring  
    
root = Tkinter.Tk()
root.withdraw()

if len(sys.argv) == 2:
    print "Processing:   " + sys.argv[1]
    file_path = sys.argv[1]
else:
    file_path = tkFileDialog.askopenfilename()

print file_path

ifile = open(file_path,"r")
createWorkfile(file_path)

db = MySQLdb.connect("localhost","david","david","RBC" )
cursor = db.cursor()

while True:
    iline = ifile.readline()
    if not iline: 
        break
#   print iline[17:23]
    if (iline[0:8] == "Account:"):
        accountNum = iline[9:18]
        print accountNum
    elif (iline[4:19] == "Holdings Export"):
        print "loaddate = " + iline[26:49]
        gloaddate = parse(iline[26:49])
        print gloaddate
    elif (iline[0:31] == "Currency,Cash,Investments,Total"):
        iline = ifile.readline()
        i = iline.find('"')
        j = iline.find('"',i + 1)
        gcash = Decimal(iline[ i + 1:j])
    elif (iline[17:23] == "USD = "):
        currencyConv = Decimal(iline[23:30])
        print currencyConv
        

ifile.close()

with open('/tmp/workfile') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        gsector = row[0]
        gproduct = row[1]
        gsymbol = row[2]
        gname = row[3]
        gquantity = row[4]
        gprice = row[5]
        gcurrency = row[6]
        gtotalbookcost = NA(row[9],0)
        gtotalmarketvalue = row[10]
        ggainloss = NA(row[11],0)
        gaveragecost = NA(row[13],0)
        gannualdividend = NVL(row[14],0)
        gdividenddate = row[15]

        insertInvestments(accountNum)
        if countName(gsymbol) == 0:
            insertSymbolname(gsymbol,gproduct,gname)
        db.commit()

insertCash(accountNum)
db.commit()

db.close()
