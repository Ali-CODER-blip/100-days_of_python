languages = ("hindi","urdu","sanskrit","culturallang")
temp = list(languages)
print(temp)
# temp.append("tamil")
# temp.remove("urdu")
# temp[3] = "telugu"
languages = tuple(temp)
print(languages)


#concatenation of tuple
a = ("hindi","english")
b = ("india","bhutan")
print(a+b)

a = ("abhay",)
print(a*5)
#"*middle" means give middle all the elements except i1st and last
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first, middle, last)

#----practical example----
marks = (45,89,65,25)
print(max(marks))
print(min(marks))
print(sum(marks))

