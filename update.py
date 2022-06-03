import json
def write_json(new_data, filename='emp.json'):
	with open(filename,'r+') as file:
		file_data = json.load(file)
		file_data["emp_details"].append(new_data)
		file.seek(0)
		json.dump(file_data, file, indent = 4)

	# python object to be appended
y = {"name" : input("Enter employee name : "),
      "emp_id" : "2022-001",
      "city" : input ("Enter city : "),
      "experience" : int(input("Enter experience :")),
      "ctc" : int(input("Enter CTC : ")),
      "age" : int(input("Enter age : ")),
      "contact" : int(input("Enter contact : "))
    }
	
write_json(y)
