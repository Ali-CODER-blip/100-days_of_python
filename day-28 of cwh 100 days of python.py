# #f-string
# #string formatting

# letter = "hey my name is {1} and i am from {0}"
# country = "india"
# name = "ali"
# print(letter.format(country,name))


# #
# etter = "hey my name is {1} and i am from {0}"
# country = "india"
# name = "ali"
# print(f"hey my name is {name} and i am form {country}")

# #for taking 2 decimal of a floatig value
# price = 49.000099
# txt = f"for only {price:.2f} rupees"
# # print(txt.format(price = 49.000099))
# print(txt)


# #
# print(f"{2*30}")
# print(type(f"{2*30}"))
# print(f"we use f-string like this: hey my name is {{name}} and i am from {{country}}")


#seprator and integer example
number = 100000
print(f"{number:,}")

# width and aligment

print(f"|{'python':>10}|")
print(f"|{'python':<10}|")
print(f"|{'python':^10}|")

#
total = 150
tax = 0.18
print(f"{total = }")
print(f"{tax = }")
print(f"{total*(1+tax) = }")