def calculateGmean(a, b):
  mean = (a * b) / (a + b)
  print(mean)



def isgreater(a,b):
  if(a>b):
    print("first number is greater")
  elif(b>a):
     print("second number is greater")
  else:
     print("both number are equal")


     
  

a = 8
b = 8
isgreater(a,b)
calculateGmean(a,b)
c = 8
d=10
isgreater(c,d)
calculateGmean(c, d)



def show_message():
   print("welcome to python!")


show_message()
show_message()
show_message()



def clap():
   print("clap!")

print("the function has been defined. ")
print("now the fucntion is called: ")
clap()




def greet_person(name):
   print("Hello",name)

greet_person("ali")
greet_person("hasan")
greet_person("Ali Hasan")



def square(number):
   print("square =",number*number)

square(6)
square(8)   


def calculate_gmean(a,b):
   gmean = (a*b)**0.5
   print("gmean =",gmean)

calculate_gmean(5,6)
calculate_gmean(7,8)
   

def is_lesser(a,b):
   if a>b:
      print(b,"is lesser than",a)
   elif b>a:
      print(a,"is lesser than",b)
   else:
      print("both number are equal")
 
is_lesser(10,6)
is_lesser(58,66)


print(min(8,6,9))
print(len("ali hasan"))




def show_title():
    print("=== SIMPLE PROGRAM ===")
show_title()    

def show_status():
   print("status: Running")
show_status()   




def even_or_odd(n):
   if n%2==0:
      print("even")
   else:
      print("odd")   







def print_table(n):
   for i in range(1,11):
     print(n, "x", i, "=",n*i )


print_table(5)   
print_table(6)











