from urllib.request import urlopen
import re

item = input().replace(" ","+")

path = "https://www.ceneo.pl/szukaj-" + item 
print(path)
html = urlopen(path).read().decode('utf-8')
print(re.findall(r'data-source-tag="">([A-za-z0-9 ,/\"\'()]+)</a>',html))