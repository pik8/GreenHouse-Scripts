import json
import csv
import os

this = os.listdir("json/")[2]
print this

i = 0
for filename in os.listdir("json"): 
	dst ="Plant" + str(i) + ".json"
	src ='json/'+ filename
	dst ='json/'+ dst
	print src
	print dst
	os.rename(src, dst)
	i += 1