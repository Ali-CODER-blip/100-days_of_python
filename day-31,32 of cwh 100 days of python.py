# s = {2,4,8}
# print(s)


# harry = {}
# print(type(harry))

# # for empty set
# harry = set()
# print(type(harry))

# numbers = {1,2,2,3,3,4,5}
# print(numbers)





# fruits = {"apple","banana","mango"}
# for fruit in fruits:
#     print(fruit)

# print("apple" in fruits)

# fruits.add("pineapple")

# print(fruits)

# fruits.remove("apple")

# print(fruits)





# #wap to ask for a sentence and print unique words using input(),split(),and set().
# sentence = input("enter a sentence: ")
# words = sentence.split()
# unique_word = set(words)
# print(unique_word)




# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9}
# print(a.union(b))
# print(a|b)

# print(a.intersection(b))
# print(a&b)


# print(a.difference(b))
# print(b.difference(a))
# print(a-b)
# print(b-a)


# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# print(a^b)



# a.update(b)
# print(a)

# a.intersection_update(b)
# print(a)

# a.difference_update(b)
# print(a)

# a.symmetric_difference_update(b)
# print(a)




# a = {1,2}
# b = {1,2,3,4}
# print(a.issubset(b))
# print(a<=b)


# print(b.issuperset(a))
# print(b>=a)



# disjoint(when no element is common)



ali = {"python","maths","english"}
rahul = {"python","science","maths"}

print(ali&rahul)