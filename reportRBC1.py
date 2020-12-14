import Tkinter, MySQLdb, os, csv

#root.withdraw()

def CDN(lcurrency, lrate, lamount):
    if lcurrency == 'USD':
        return (lrate * lamount)
    else:
        return lamount


try:
    db = MySQLdb.connect("localhost","david","david","RBC" )
except Exception, e:
    print(e)

gtotbookcost = 0
gtotmarketcost = 0
gcurrency = 0
gconv = 0

try:
    cursor = db.cursor()
    cursor.execute("SELECT account,dateloaded,name,conversionrate,currency,totalbookcost,totalmarketvalue ,sector, product,investments.symbol FROM investments,symbolname where investments.symbol = symbolname.symbol AND dateloaded LIKE '2018-06-03%' AND account = '79753365' ORDER BY account,product,name")
 
    row = cursor.fetchone()
 
    while row is not None:
        gaccount = row[0]
        gdateloaded = row[1]
        gname = row[2]
        gconv = float(row[3])
        gcurrency = row[4]
        gbookcost = float(row[5])
        gtotmarket = float(row[6])
        gsector = row[7]
        gproduct = row[8]
        gsymbol = row[9]
        print "%s %s %-20s %-15s %-9s %-70s %s %10.2f %s %10.2f CDN %10.2f" % (gaccount,gdateloaded, gsector, gproduct, gsymbol, gname, gcurrency,gbookcost, gcurrency, gtotmarket, CDN(gcurrency,gconv,gtotmarket))
        gtotbookcost = gtotbookcost + gbookcost
        gtotmarketcost = gtotmarketcost + gtotmarket
        row = cursor.fetchone()
 
except Exception, e:
    print(e)

print "Book cost   USD %10.2f CDN %10.2f" % (gtotbookcost, CDN(gcurrency, gconv, gtotbookcost))
print "Market cost USD %10.2f CDN %10.2f" % (gtotmarketcost, CDN(gcurrency, gconv, gtotmarketcost))
db.close()
