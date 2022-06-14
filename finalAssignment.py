# import json
import json
import pprint
from textwrap import indent
# filename
filename = "emp.json"
emp_dic =[{
      "name" : input("Enter employee name : "),
      "employee_id":"A2022-1",
      "city" : input ("Enter city : "),
      "experience" :int(input("Enter experience :")),
      "ctc" : int(input("Enter CTC : ")),
      "age" : int(input("Enter age : ")),
      "contact" : int(input("Enter contact : ")) 
      }]
dic = json.dumps(emp_dic , indent=4)
with open (filename,"w") as file:
     file.write(dic)
     print(dic)

# Choices function for user to select add,update,delete
def Choices():
    print("manage employee system")
    print("a - add the new employee detail")
    print("u - update the employee detail")
    print("d - delete the employee detail")
    

while True:

    # open the json file and store the datas in data variable
    with open(filename, "r") as file:
        data = json.load(file)

    # to get the last employee id in a list
    id = [int(data[-1]['employee_id'][6:])]

    Choices()
    # user need to select the option
    Choice = input("\nEnter option for what you want to do: ")
    # add a new data to json file
    if Choice == "a":
        # to create a new employee id for new user
        emp_id = id[-1] + 1
        id.append("A2022" + "-" +str(emp_id))
        #exception handle
        try:
        # getting all the input data from the user for new employee to add in json file
         emp_dic = {"name": input("enter your name : "),
                     "employee_id": id[-1],
                     "city": input("enter the city : "),
                     "experience": int(input("enter the experience : ")),
                     "ctc": int(input("enter your ctc : ")),
                     "age": int(input("enter the age : ")),
                     "contact_no": int(input("enter the contact number : "))
                     }
        except ValueError:
         print("Invalid input") 
        except TypeError:
         print("Invalid input")
        except IndexError:
         print("Invalid input")
        
        # open the file and read the data and store in data variable
        with open(filename, "r") as file:
            data = json.load(file)

        # append the new employee data to data variable
        data.append(emp_dic)
         
        # data variable had some datas , write the data to json file
        with open(filename, "w") as file:
            json.dump(data, file,indent=4)
        

        print("new employee details added")

    # update the data on existing employee
    elif Choice == "u":

        # open the file and read the data and store it in data variable
        with open(filename, "r") as file:
            data = json.load(file)
            pprint.pprint(data)

            #  asking the user which employee id that user must update
            Enter_id = input("Enter the employee id to update: ")

            # getting the data from file separately using index
            for index, emp in enumerate(data):

                # checking user given employee id is in the dataset already
                if Enter_id == emp['employee_id']:
                    #asking for key which you want to change
                   change= input("enter what you want to change : ")
                   
                   if change == "name":
                     data[index]["name"] = input("enter your name : ")
                   elif change=="city": 
                    data[index]["city"] = input("Enter city : ")
                   elif change=="experience":
                    data[index]["experience"] = int(input("Enter experience :"))
                   elif change=="ctc":
                    data[index]["ctc"] = int(input("Enter CTC : "))
                   elif change=="age":
                    data[index]["age"] = int(input("Enter age : "))
                   elif change=="contact_no":
                    data[index]["contact_no"] = int(input("Enter contact : "))
                   else:
                    print("Invalid change selection")
                    break
                    # open the file and write the updated data to file
                   with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                        print("employee detail updated")
                        break
            # if the user gives not matching employee id
            else:
                 print("Invalid employee id")
    # delete the employee data in json file
    elif Choice == "d":

        # open the file and read the data and store it in data variable
        with open(filename, "r+") as file:
            data = json.load(file)
            print(data)

        # asking the employee id which user need to delete
        Enter_id = input("Enter employee_id you want to delete: ")

        # getting the data from file separately using index
        for index, emp in enumerate(data):

            # checking emp id is in the dataset
            if Enter_id == emp["employee_id"]:
                confirm = input("Do you want to delete,press y : ")

                if confirm == "y":
                    del data[index]

                    # open the file and write the data to json file
                    with open(filename, 'w') as data_file:
                        data = json.dump(data, data_file,indent=4)
                    break
        else:
            print("emp_id is not found.")

    else :
        print("Invalid Input")