import json
import csv
import os
import glob

outputFile = open("query.sql", "w+")
outputWriter = csv.writer(outputFile)
value_id = 1

files = glob.glob('json/*.json')
for filename in files:
	with open(filename, 'r') as sourceFile:
		data = sourceFile.read()
		if data != '' and data != 'null':
			json_data = json.loads(data)
			row = []
			value_display = json_data["display_pid"]
			value_origin = json_data["basic"]["origin"]
			value_category = json_data["basic"]["category"]
			value_blooming = json_data["basic"]["blooming"]
			value_color = json_data["basic"]["color"]
			value_size = json_data["maintenance"]["size"]
			value_soil = json_data["maintenance"]["soil"]
			value_sunlight = json_data["maintenance"]["sunlight"]
			value_watering = json_data["maintenance"]["watering"]
			value_fertilization = json_data["maintenance"]["fertilization"]
			value_pruning = json_data["maintenance"]["pruning"]
			value_max_light_mmol = json_data["parameter"]["max_light_mmol"]
			value_min_light_mmol = json_data["parameter"]["min_light_mmol"]
			value_max_light_lux = json_data["parameter"]["max_light_lux"]
			value_min_light_lux = json_data["parameter"]["min_light_lux"]
			value_max_temp = json_data["parameter"]["max_temp"]
			value_min_temp = json_data["parameter"]["min_temp"]
			value_max_env_humid = json_data["parameter"]["max_env_humid"]
			value_min_env_humid = json_data["parameter"]["min_env_humid"]
			value_max_soil_moist = json_data["parameter"]["max_soil_moist"]
			value_min_soil_moist = json_data["parameter"]["min_soil_moist"]
			value_max_soil_ec = json_data["parameter"]["max_soil_ec"]
			value_min_soil_ec = json_data["parameter"]["min_soil_ec"]
			#image = json_data["image"]
			sql_query = "INSERT INTO plant VALUES("+str(value_id)+", `"+value_display+"`, `"+value_origin+"`, `"+value_category+"`, `"+str(value_blooming)+"`, `"+str(value_color)+"`, `"+value_size+"`, `"+value_soil+"`, `"+value_sunlight+"`, `"+value_watering+"`, `"+value_fertilization+"`, `"+value_pruning+"`, "+str(value_max_light_mmol)+", "+str(value_min_light_mmol)+", "+str(value_max_light_lux)+", "+str(value_min_light_lux)+", "+str(value_max_temp)+", "+str(value_min_temp)+", "+str(value_max_env_humid)+", "+str(value_min_env_humid)+", "+str(value_max_soil_moist)+", "+str(value_min_soil_moist)+", "+str(value_max_soil_ec)+", "+str(value_min_soil_ec)+", `image`);"
			value_id += 1
			row.append(sql_query)
			outputWriter.writerow(row)

outputFile.close()