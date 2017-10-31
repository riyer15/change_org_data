import json, requests
import csv

petitions = []
API_KEY = "40876ecd7088cefc8acf9087ca9037e043a28d165019070e915ede832396aed3"
for i in range(10,50):
	url = "https://api.change.org/v1/users/"+ str(i) +"/petitions?api_key=" + API_KEY
	response = requests.get(url)
	json_obj = json.loads(response.text)
	if 'petitions' in json_obj.keys():
		if json_obj["petitions"]:
			petitions.extend(json_obj["petitions"])

keys = petitions[0].keys()
#print keys
with open('petitions.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    for pet in petitions:
    	for key in pet.keys():
    		pet[key] = unicode(pet[key]).encode("utf-8")
    	dict_writer.writerow(pet)

