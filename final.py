import json
import os

outputFile = open("finalQueries2.sql", "w")

with open('finalQueries.sql', 'r+') as file:
	for line in file:
		line = line.replace("`", "'")
  		outputFile.write(line)
file.close()