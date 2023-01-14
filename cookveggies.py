# Step 1
import json
import csv

with open('vegetables.csv', 'r') as f:
	rows = csv.DictReader(f)
	vegetables = list(rows)

# Step 2
print(vegetables)

# Step 3

with open('vegetables.json', 'w') as f:
	json.dump(vegetables, f)