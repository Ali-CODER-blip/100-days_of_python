# student = {
#     "name":"ali",
#     "age":19,
#     "marks":85,
# }
# print(student["name"])
# print(student["age"])
# print(student["marks"])
# print(student)

# print(student.get("name"))
# print(student.get("city")) #this will not cuse error, just shows not found
# print(student.get("city","unknown"))  #returns unknown for use

# print("name" in student)
# print("city" in student)

# print("ali" in student.values())
# print(len(student))


# del student["age"] #for deleting
# print(student)


# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key,":",value)




# #for making emty dictionary
# student = {}
# #or
# student = dict()
# print(student) 

 
# # nested dictonary
# students = {
#     "student1" :{
#         "name" : "ali",
#         "age" : 19
#     },
#     "student2" : {
#         "name" : "rahul",
#         "age" : 20
#     }
# }

# print(students["student1"]["age"])
# print(students["student2"]["name"])

# #dictionary with different data types
# food = {
#     "starter":"russian salad",
#     "main course":["mutton biryani","chicken biryani","veg biryani"],
#     "dessert":"gulab-gamun"
# }
# print(food["main course"])
# print(food["main course"][1])


# #update dictionary
# person = {
#     "name":"ali",
#     "city":"mumbai"
# }

# person["city"] = "delhi"
# person["age"] = 19

# print(person)


# #update by different approach 
# student = {
#     "name":"ali",
#     "age":19
# }
# student.update({
#     "age":20,
#     "city":"delhi"
# })
# print(student)




# student = {
#     "name": "Ali",
#     "age": 19,
#     "city": "Delhi"
# }

# removed_value = student.pop("age")    #pop() removes the item and return its value
# print(removed_value)
# print(student)


# removed_item = student.popitem()   #popitem removes and return the last inseerted key-value pair
# print(removed_item)
# print(student)

# student.clear()
# print(student)


##get a value or insert a missing key
student = {"name":"ali","age":19}
result = student.setdefault("city","delhi")
print(result)
print(student)

##if the key already exists , setdefault return its existing value without cahnging it
student.setdefault("age",25)
print(student["age"])


##fromkeys()-create a dictionary from keys
subjects = ["python","c","maths"]
marks = dict.fromkeys(subjects,100)
print(marks)


##dictionary comprehension
square = {number:number**2 for number in range(1,6)}
for number,sq_values in square.items():
    print(f"{number}:{sq_values}")