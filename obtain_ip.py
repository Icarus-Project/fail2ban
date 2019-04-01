import requests

def obtain(ip):
	json_response = requests.get("http://10.159.25.85:8080/json/"+ip).json()
	for i in json_response.keys():
		if json_response[i] == '':
			json_response[i] = "NULL"
	return json_response
#	return pritty_print_json(json_response)



def pretty_print_json(json_dict):
	for i in json_dict.keys():
		print(i,json_dict[i])




def info_module():
	print("obtain(ip) -> Query al server, restituisce json con info IP")
	print("pretty_print_json(json_dict) -> printa il json in maniera leggibile")
