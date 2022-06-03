import json
from secrets import choice
while True:
      emp_dic = [{
      "name" : input("Enter employee name : "),
      "emp_id" : "2022-001",
      "city" : input ("Enter city : "),
      "experience" : int(input("Enter experience :")),
      "ctc" : int(input("Enter CTC : ")),
      "age" : int(input("Enter age : ")),
      "contact" : int(input("Enter contact : "))
      }]
      dic = json.dumps(emp_dic , indent=4)
      with open ("emp.json","w") as outfile:
        outfile.write(dic)
      print(dic)
      choice = input("Do you want to Enter another employee details Press 'y'if yes : ")
      if choice !="y" :
        break

      


      
      

    



     