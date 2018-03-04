import json, requests
import csv
import time

# 1675000
petitions = []
API_KEY = "40876ecd7088cefc8acf9087ca9037e043a28d165019070e915ede832396aed3"

def call_ids_for_petition(index_range):
	start_index = index_range*1675+1
	end_index =(index_range+1)*1675
	for i in range(start_index, end_index):
		url = "https://api.change.org/v1/users/"+ str(i) +"/petitions?api_key=" + API_KEY
		response = requests.get(url)
		json_obj = json.loads(response.text)
		if 'petitions' in json_obj.keys():
			if json_obj["petitions"]:
				petitions.extend(json_obj["petitions"])
	keys = ["status","goal","creator_name", "title","url", "overview","created_at","signature_count","end_at","organization_name", "letter_body", "petition_id", "creator_url", "image_url", "organization_url","targets"]
	with open('petitions3.csv', 'a') as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
	    dict_writer.writeheader()
	    for pet in petitions:
	    	for key in keys:
	    		if key in pet:
	    			pet[key] = repr(pet[key]).encode("utf-8")
	    	dict_writer.writerow(pet)

index = int(input("what number call is this"))
call_ids_for_petition(index)
#for i in range (10, 16):
	#call_ids_for_petition(i)
	#time.sleep(120)

#print keys


