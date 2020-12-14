from dateutil.parser import parse

a =  "Apr 11, 2018 12:31:28 PM ET"

b = parse(a)

print(b.weekday())
print b

