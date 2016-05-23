import json

def json_loader(file):
	json_data=open(file)

	data = json.load(json_data)
	json_data.close()
	return data
		