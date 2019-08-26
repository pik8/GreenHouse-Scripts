import json
import os

outputFile = open("finalQueries.sql", "w")

with open('query.sql', 'r+') as file:
	for line in file:
		line = line.replace('"', "")
		line = line.replace("'", "")
  		outputFile.write(line)
file.close()