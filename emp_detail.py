import json
from textwrap import indent

print("Manage Employee Detail: ")
print("(a) for Add")
print("(u) for Update")
print("(d) for Delete")
Choice = (input("Enter Your choice: "))
#condition for ADD
if Choice=="a" :
    emp_dic =[{
      "name" : input("Enter employee name : "),
      "emp_id" : "2022-001",
      "city" : input ("Enter city : "),
      "experience" : int(input("Enter experience :")),
      "ctc" : int(input("Enter CTC : ")),
      "age" : int(input("Enter age : ")),
      "contact" : int(input("Enter contact : ")) 
      }]
    #read & append the data.
    with open ("emp.json","r") as file:
        data=json.load(file)
        data.append(emp_dic)
    #write the data in json file & display it.
    with open("emp.json","w") as file:
     json.dump(data, file , indent=4)
    print(data)

#condition for UPDATE
elif Choice=="u" :
  #show the existing file
    jsonfile=open("emp.json","r")
    data=json.load(jsonfile)
    print(data)

  #ask the emp_id which the user want to update.
    enter_id = input("Enter emp_id you want to update: ")
    jsonfile=open("emp.json","r")
    data=json.load(jsonfile)

   #check the id exists or not 
    if enter_id== ["emp_id"]:
        data["name"] = input("Enter employee name : ")
        data["emp_id"] = "2022-001"
        data["city"] = input ("Enter city : ")
        data["experience"]= int(input("Enter experience :"))
        data["ctc"] = int(input("Enter CTC : "))
        data["age"] = int(input("Enter age : "))
        data["contact"] = int(input("Enter contact : ")) 
        jsonfile =open("emp.json", "w") 
        json.dump(data, jsonfile, indent=4)
        print(data)
    else:
      print("emp_id is not found.")
      
#condition for Delete
elif Choice == "d":
  #show the existing file
    jsonfile=open("emp.json","r")
    data=json.load(jsonfile)
    print(data)

    #ask the emp_id which the user want to update.
    enter_id = input("Enter emp_id you want to delete: ")
    jsonfile=open("emp.json","r")
    data=json.load(jsonfile)
    jsonfile.close()

    #check the id exists or not
    if enter_id==[{'emp_id'}]:
    #asking for confirmation
        enter_confirmation =input("Are you want to delete,if yes enter (y): ")
        if enter_confirmation == "y":
          del data[enter_id]
    else:
      print("emp_id is not found.")

#when the input is other than a,u,d:
else:
    print("invalid input: ")



 
     



      
      