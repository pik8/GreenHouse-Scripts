import simplejson
import csv
import os
import glob

outputFile = open("Plants.csv", "a")
outputWriter = csv.writer(outputFile)
row_naming = ["name", "min_env_humid", "min_light_lux", "max_light_lux",
"max_soil_moist", "min_soil_ec", "max_env_humid", "max_soil_ec", "max_light_mmol",
"min_temp", "min_light_mmol", "min_soil_moist", "max_temp", "image"]
outputWriter.writerow(row_naming)

files = glob.glob('json/*.json')
for filename in files:
	with open(filename, 'r') as sourceFile:
		data = sourceFile.read()
		if data != '' and data != 'null':
			json_data = simplejson.loads(data)
			row_array = []
			row_array.append(json_data["display_pid"])
			for parameter in json_data["parameter"].iteritems():
				attribute = parameter[1]
				row_array.append(attribute)
			row_array.append(filename)
			outputWriter.writerow(row_array)

outputFile.close()