# num = int(input("enter a number"))
# fact = 1
# for i in range(1,num+1):
#     fact*=i
# print(fact)    




# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact=fact*i

#     return fact

# num = int(input("enter a number: "))
# result = factorial(num)
# print(result) 


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


# def numbers(n):
#     if n==0:
#         return
    
#     numbers(n-1)
#     print(n)

# numbers(8)   

# def numbers(n):
#     if n==0:
#         return
#     print(n)
#     numbers(n-1)


# numbers(5)




# def total(n):
#     if n == 0:
#         return 0

#     return n + total(n-1)
# print(total(8))


# def power(a,n):
#     if n==0:
#         return 1
#     return a * power(a,n-1)
# print(power(2,4))


# def digit_sum(n):
#     if n==0:
#         return 0
#     return n%10 + digit_sum(n//10)
# print(digit_sum(8956))


# def digit_count(n):
#     if n == 0:
#         return 0
#     return 1 + digit_count(n//10)
# print(digit_count(12569))

# def reverse(s):
#     if s == "":
#         return ""
#     return reverse(s[1:]) + s[0]
# print(reverse("alihasan"))


# def palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]==s[-1]:
#         return False
#     return palindrome(s[1:-1])
# print(palindrome('alihasan'))
# print(palindrome('madam'))



# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))


