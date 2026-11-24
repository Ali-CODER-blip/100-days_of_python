# #lists


# marks = [3,4,5,"harry",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[2])

# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])



# mark = [3,4,5,6]
# print(mark[0])

# names = ["ali","harry","sara","rahul"]
# print("ali" in names)
# if "ali" in names:
#     print("ali is present")




# values = [1,2,3,"4"]
# print( 4 in values)
# print("4 in values")


# #list preserves order
# item = ["first","second","third"]
# print(item)
# print(item[0])
# print(item[1])
# print(item[2])


# #list are mutable
# number = [10,30,40]
# print("before",number)
# number[1] = 50
# print("after",number)


# numbers = [0,1,2,3,4]
# print(numbers[:5])
# print(numbers[2:])
# print(numbers[:])
# print(numbers[::-1])



# square = [i*i for i in range(5)]
# print(square)


# value = [i for i in range(4)]
# print(value)


# odd_numbers = [i for i in range(11) if i%2!=0]
# print(odd_numbers)


# smaller_than_seven = [i for i in range(8) if i<7]
# print(smaller_than_seven)


# names = ["ali","harry","aditya","harshit"]
# upper_names = [name.upper() for name in names]
# print(upper_names)



# square_loop = []
# for i in range(6):
#     square_loop.append(i*i)

# print(square_loop)    

# square_with_comprehension = [i*i for i in range(6)]
# print(square_with_comprehension)


# #finding whether a student is in list or not
# students = ["ali","sara","rakshit","abhay"]
# name = "rakshit"
# if name in students:
#     print("name is in the list")
# else:
#     print("name is not in the list")    

# odd_squares = [i*i for i in range(10) if i%2!=0]
# print(odd_squares)

ANSWERS = """
--- Concept Answers ---

A1. A list is a Python data structure that stores multiple values under one
    variable name.

A2. Lists let us store and work with collections of related values together.

A3. Square brackets: `[]`.

A4. Yes. A list can contain different data types.

A5. 0.

A6. 0, 1, 2, 3, 4.

A7. 4.

A8. The number of elements in the list.

A9. Negative indexing accesses elements by counting from the end.

A10. The last element.

A11. It checks whether a value exists in the list.

A12. Because integer 4 and string "4" are different values/types.

A13. Yes. Lists preserve the order of their elements.

A14. It means the list can be changed after it has been created.

A15. `my_list[start:end]`

A16. No. The end index is excluded.

A17. It returns elements from the beginning up to, but not including, index 4.

A18. It returns elements from index 2 through the end.

A19. A slice containing the whole list.

A20. `my_list[start:end:step]`

A21. It controls how far the slice jumps between indexes.

A22. It selects every second element, starting from the beginning.

A23. It commonly reverses the list.

A24. A compact syntax for creating a new list from an iterable, optionally with a
    condition.

A25. `[expression for item in iterable]`

A26. `[expression for item in iterable if condition]`

A27. It can express common list-building operations concisely.

A28. Python raises `IndexError: list index out of range`.

A29. Indexing selects one element; slicing selects a range/sequence of elements.

A30. Because the first element is at index 0, so the index of an element is not
     usually the same as its human counting position.


--- Output / Trace Answers ---

A31.
        10
        30

A32.
        yellow
        green

A33.
        [1, 2, 3]

A34.
        [0, 1, 2]
        [3, 4, 5]

A35.
        [0, 2, 4]

A36.
        [4, 3, 2, 1, 0]

A37.
        True
        False

A38.
        False
        True

A39.
        [1, 99, 3, 4]

A40.
        [0, 1, 4, 9, 16]

A41.
        [0, 2, 4, 6, 8]

A42.
        [20, 30, 40]


--- Coding Answers ---

A43.
        numbers = [10, 20, 30, 40, 50]
        print(numbers)

A44.
        names = ["Ali", "Sara", "Rahul", "Aman", "Neha"]
        print(names[0])
        print(names[-1])

A45.
        marks = [78, 92, 65, 88, 70]
        print(marks[2])

A46.
        print(my_list[-1])

A47.
        languages = ["C", "Python", "Java", "C++"]

        if "Python" in languages:
            print("Present")

A48.
        numbers[1] = 100

A49.
        numbers = [0, 1, 2, 3, 4, 5, 6]
        print(numbers[2:6])

A50.
        print(numbers[::2])

A51.
        print(numbers[::-1])

A52.
        squares = [i * i for i in range(11)]
        print(squares)

A53.
        even = [i for i in range(21) if i % 2 == 0]
        print(even)

A54.
        names = ["ali", "sara", "rahul"]
        upper_names = [name.upper() for name in names]
        print(upper_names)

A55.
        numbers = [5, 12, 8, 20, 15]
        result = [number for number in numbers if number > 10]
        print(result)

A56.
        cubes = [i ** 3 for i in range(1, 11)]
        print(cubes)

A57.
        numbers = [10, 20, 30, 40, 50]
        result = numbers[::2]
        print(result)

A58.
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = [number ** 2 for number in numbers if number % 2 == 0]
        print(result)

A59.
        marks = [32, 45, 67, 28, 90]
        passed = [mark for mark in marks if mark >= 40]
        print(passed)

A60.
        names = ["ali", "sara", "rahul"]
        upper_names = [name.upper() for name in names]
        print(upper_names)


--- Reasoning Answers ---

B1. One list lets you store, access, inspect, and process all the marks as one
    collection instead of managing many unrelated variable names.

B2. Python's indexing design makes the first element index 0. For beginners,
    the practical rule to remember is that indexing starts at zero.

B3. Because indexing starts at 0. Eight elements occupy indexes 0 through 7.

B4. It lets you say "last element" directly without calculating the length first.

B5. If a list has length n, its last positive index is n - 1.

B6. An invalid index does not refer to an actual element. Raising an error makes
    the programmer aware that the requested position does not exist.

B7. Excluding the end makes ranges easier to combine and is consistent with
    Python's other range-style operations.

B8. `numbers[2]` gives one element. `numbers[2:3]` gives a list containing that
    element.

B9. Slicing lets you select a section without manually accessing every element.

B10. The step lets you skip elements, such as taking every second or third item.

B11. The slice starts from the end when the step is negative, so `[::-1]` walks
     backward through the entire list.

B12. `"4"` is a string while `4` is an integer. The list contains the string, not
     the integer.

B13. Python lists are flexible containers and do not require every element to
     have the same type.

B14. You can change an existing list after creating it, for example by assigning
     a new value to one of its indexes.

B15. Lists are mutable, so indexed assignment changes the existing list.

B16. A normal loop can be clearer when the logic is complicated or requires
     multiple steps. List comprehension is concise for straightforward
     transformations/filtering.

B17. `range(5)` produces 0, 1, 2, 3, 4. The expression squares each of those,
     producing five values.

B18. "Take every number from 0 to 19, keep only the even ones, and put those
     numbers into a new list."

B19. A one-line expression can become difficult to understand if it contains
     too many nested conditions or complicated transformations.

B20. Indexing can inspect specific marks, negative indexing can inspect from the
     end, slicing can select sections, `in` can check membership, and list
     comprehension can create filtered/transformed lists.
"""

