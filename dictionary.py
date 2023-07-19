'''->data type
-> defined into element key and values
-> stores data in a key value pair format
->values are mutable
->keys must be single element (are immutable)
->values of any type'''

emp = {"name": "vishal", "age":21, "salary":29000, "company":"google"}
print(type(emp))
print("printing Employee data .... ") 
print("Name : %s" %emp["name"]) 
print("Age : %d" %emp["age"]) 
print("Salary : %d" %emp["salary"]) 
print("Company : %s" %emp["company"]) 

#updating dictionary
emp["name"]="shanker"
emp["age"]=20
emp["salary"]=50000
emp["company"]="amazon"
print("Name : %s" %emp["name"]) 
print("Age : %d" %emp["age"]) 
print("Salary : %d" %emp["salary"]) 
print("Company : %s" %emp["company"]) 