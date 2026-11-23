def average(a=9,b=1):
    print("the average is ",(a+b)/2)
average(b=9)

#-program for finding average of numbers
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is :",sum/len(numbers)) 

average(10,20,50)    
average(80,56.6,89.2)
average(80,56.2,32.6,36.9,89.7,78.4,58.3,98.5)


#
def introduce(name,age):
    print("name:",name)
    print("age:",age)

introduce("ali",19)
introduce("haary",30)


#
def greet_user(name, message="Welcome"):
    print(message, name)

greet_user("Ali")
greet_user("Ali", "Good morning")

#
def order_item(item, quantity=1):
    print("Item:", item)
    print("Quantity:", quantity)

order_item("Notebook")
order_item("Pen", 5)



#
def profile(name, age ,city):
    print("name:",name)
    print("age:",age)
    print("city",city)


profile(city="delhi",name="ali",age="19")

def show_data(name,age):
    print(name, age)

show_data(age=19, name="ali")    


def show_args(*args):
    print("Value:", args)
    print("Type:", type(args))

show_args(10, 20, 30)

def show_profile(**details):
    print("Details:", details)
    print("Type:", type(details))

show_profile(name="Ali", age=19, city="Delhi")





def add_and_return(a,b):
    return a+b
result = add_and_return(10,20)
print("result:",result)



#example of why return is more powerfl
def square(number):
    return number*number
answer = square(5)
bigger_answer = square(5)+10
print("anwer:",answer)
print("bigger_answer:",bigger_answer)



#example of retirns stops the function
def check_number(number):
    if number > 0:
        return "Positive"

    print("This line runs only if the number is not positive.")
    return "Zero or negative"

print(check_number(7))
print(check_number(-2))
