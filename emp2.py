from fileinput import filename
import json
from secrets import choice
import json

filename = "emp.json"
def Choices():
	print ("Manage Employee details")
	print ("(y) Add New Employee details")
	print ("(n) Exit")
	

def update_data():
 item_data = {}
 with open (filename, "r") as f:
  temp = json.load(f)
  item_data["name"] = input("Enter employee name: ")
  item_data["emp ID"] = 2202-1
  item_data["city"] = input("Enter City: ")
  item_data["expiriance"] =int( input("Enter exprience: "))
  item_data["ctc"] = int(input("Enter CTC: "))
  item_data["age"] = int(input("Enter age: "))
  item_data["contact"] = int(input("Enter contact: "))
       
  temp.append(item_data)
 with (filename, "w") as f:
		json.dump(temp, f, indent=4)




while True:
	Choices()
	Choice = input ("\nSelect a option: ")
	if Choice == "y":
		update_data()
	if Choice == "n":
		break
	else:
		print ("Please select a valid option.")