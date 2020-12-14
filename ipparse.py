import re

file = open('/tmp/nmapper.dat', 'r')
for eachline in file.readlines():
#   ip_regex = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', eachline)
    ip_regex = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', eachline)
    print ip_regex

