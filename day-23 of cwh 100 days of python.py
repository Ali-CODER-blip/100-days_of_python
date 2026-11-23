# #use of .append()
# color = ["red","blue","black"]
# color.append("green")
# print(color)

# #append adds only one subject
# a = [2,3]
# a.append([3,5])
# print(a)


# name = ["ali","lakshit",]
# name.extend(["sara","riya"])
# print(name)


# a = [6,8]
# b = [5,7]
# a.append([3,5])
# b.append([6,9])
# print(a)
# print(b)




# a = [1, 2]
# b = [1, 2]
# a.append([3, 4])
# b.extend([3, 4])
# print("append:", a)
# print("extend:", b)

# numbers = [10, 20, 30]
# removed = numbers.pop()
# print("List:", numbers)
# print("Removed:", removed)


# number = [10,20,30]
# removed = number.pop()
# print("list",number)
# print("removed",removed)



numbers = [1,3,8,7,5]
numbers.clear()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
colors = ["red","green","blue","green"]
print(colors.index("green"))

# original = [4,5,6,8]
# copied = original.copy()
# copied.append(3)
# print("original",original)
# print("copy",copied)

# print("\n===== 19. Practical Marks Example =====")
# marks = [72, 91, 45, 91, 63]
# marks.append(88)
# marks.sort(reverse=True)
# print("Marks:", marks)
# print("Highest:", marks[0])
# print("91 appears:", marks.count(91), "times")