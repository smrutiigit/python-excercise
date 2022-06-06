import json

filename = "emp.json"
def Choices():
	print ("Manage Employee details")
	print ("(y) Add New Employee details")
	print ("(n) Exit")
	

def add_data():
	item_data = {}
	with open (filename, "r") as f:
		temp = json.load(f)
	item_data["name"] = input("Enter employee name:")
	item_data["emp ID"] = 2022-0
	item_data["city"] = input("Enter City: ")
	item_data["expiriance"] = input("Enter exprience: ")
	item_data["ctc"] = input("Enter CTC: ")
	item_data["age"] = input("Enter age: ")
	item_data["contact"] = input("Enter contact: ")
	temp.append(item_data)
	with open(filename, "w") as f:
          json.dump( temp,f, indent=4)
          print(item_data)
while True:
	Choices()
	Choice = input ("\nSelect a option: ")
	if Choice == "y":
		add_data()
	if Choice == "n":
		break
	
