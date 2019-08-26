READ ME

# GreenHouse

You can count with 5000+ (5516) types of plants.
The were taken from https://github.com/vrachieru/plant-database/tree/master/json

You can add as many types of plants as you may like.
To do so, you have to add to the json folder more plants in the format of .json
(Just copy-paste, and make the changes)

If for some reason you want to create a CSV file for a single plant, open createSingleCSV.py file and change sourceFile to the name of the desired Plant.
Then, in its folder directory run the command:

	python createSingleCSV.py


## Generating CSV file

To generate the csv file with all the types of plants, do:
1. Run in the command-line (opened in the folder directory):

	python CSVGenerator.py


## Generating mySQL queries

To generate all the mySQL queries from all the .json files, you can do the following:
1. Run in the command-line (opened in the folder directory):

Starting with the command: python db.py

	python db.py
	python parseFinalQueries.py
	python final.py