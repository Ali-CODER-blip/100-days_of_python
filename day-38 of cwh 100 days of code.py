# age = int(input("enter your age: "))
# if age<0:
#     raise ValueError("age can't be negative")
# if age<18:
#     print("not eligible")
# else:
#     print("eligible")


## raise ErrorType("your error message")  {general syntax}
try:
    age = int(input("enter your age: "))
    if age<0:
        raise ValueError("age cannot be negative")
except ValueError as e:
    print("error:",e) 
print("program continues")   


#          *return	                     |           *raise
# Sends a value back from a function	 |   Raises an exception
# Normally ends the function's execution |   Interrupts normal execution and looks for an exception handler
# Example: return 0	                     |   Example: raise ValueError("Invalid")

#
marks = int(input("enter marks: "))
if marks < 0 or marks > 100:
    raise ValueError("marks muust be between 0 and 100")
print(marks)


#
try:
    raise ValueError("Oops")

except ValueError:
    print("Handled")

# try: Python attempts to execute the code inside it.
# raise ValueError("Oops"): Python raises the error.
# except ValueError: Python looks for a handler that matches this error type.
# print("Handled"): Since a matching handler exists, Python executes this line.
# {output : handled}