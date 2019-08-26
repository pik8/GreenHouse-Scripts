import json
import csv

sourceFile = open("json/Plant1.json", "r")

json_data = json.load(sourceFile)

print json_data["basic"]["origin"]

outputFile = open("file2.csv", "a")

outputWriter = csv.writer(outputFile)

row_naming = ["name", "min_env_humid", "min_light_lux", "max_light_lux",
"max_soil_moist", "min_soil_ec", "max_env_humid", "max_soil_ec", "max_light_mmol",
"min_temp", "min_light_mmol", "min_soil_moist", "max_temp"]
outputWriter.writerow(row_naming)

row_array = []
row_array.append(json_data["display_pid"])

for parameter in json_data["parameter"].iteritems():
	attribute = parameter[1]
	row_array.append(attribute)

outputWriter.writerow(row_array)

sourceFile.close()
outputFile.close()