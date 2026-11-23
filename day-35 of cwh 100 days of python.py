##for loop with else
##use:image if we are searching for a number in a list if u find it stop. ifu finish without finding it ,repor that it wasn't there
numbers = [10,20,30,40,50]
target = 40
for number in numbers:
    if number == target:
        print("number found")
        break
else:
    print("number not found!")    
