# a = input("enter the number: ")
# print(f"multiplication table of {a} is: ")
# try:
#   for i in range(1,11):
#       print(f"{int(a)} x {int(i)} = {int(a)*i}")
# except Exception as e:
#    print("invalid input!")

# print("some imp lines of code")
# print("end of program")


# try:
#    num = int(input("enter an integer: "))
#    a = [6,3]
#    print(a[num])
# except ValueError:
#    print("number entered is not an integer")
# except IndexError:
#    print("index error")
   

# try:
#     a = int(input("enter num1: "))
#     b = int(input("enter num2: "))
#     c = a/b
#     print(c)
# except ValueError:
#     print("inavalid value")
# except ZeroDivisionError:
#     print("you can't divide with zero")


##day:37 python provides a special block for code that should run whether an exception occurs or not(finally)
# try:
#     number = int(input("enter a number: "))
#     print(number)
# except ValueError:
#     print("invalid input")
# finally:
#     print("this will run at end")



##if return comes(the return statement preperes to return "hello" , before the function actually returns,the finally block executes.,the function tehn return "hello",which gets printed)
# def example():
#     try:
#         return "hello"
#     finally:
#         print("finally executed")
# print(example())

#uses of finally
# file handling : close a file even if an error occurs
# database connection : release a connection after use
# network connection : clean-up resources
# functions with return : executes necessary cleanup before returning