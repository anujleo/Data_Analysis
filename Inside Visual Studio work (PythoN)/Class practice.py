# import numpy  as np

# k = np.log(10)
# print(k)


# number = int(input("Enter the number\n"))
# i=0

def sum_of(number):
    if number<1:
        return ("Number is invalid")
    else:
        k=0
        for i in range(0,number+1):
            k+=i
        return k  

print(sum_of(5))

# THE CODE ENDS HERE


# num1 = int(input("Input the 1st number\n "))
# num2 = int(input("Input the 2nd number\n "))
# num3 = int(input("Input the 3rd number\n "))

# if num1>num2:
#     if num1>num3:
#         print(f"{num1} is the greatest number")
#     else:
#         print(f"{num3} is the greatest number")
# else:
#     print(f"{num2} is the greatest number")


# THE CODE ENDS HERE


# num = int(input("Enter the number:"))
# i = 1
# factorial = 1
# while i <= num:
#     factorial = i*factorial
#     i=i+1
    
# print(factorial)


# THE CODE ENDS HERE

# C = int(input("Enter the celcius "))
# def Celcius(C):
#     return ((C*9/5)+32)

# print(Celcius(C))


# THE CODE ENDS HERE

number = int(input("Enter the number"))
def sum(number):
    if number<1:
        return (f"The sum of first {number} natural terms is 0")
    else:
        sum =0
        for i in range (0, number+1):
            sum += i
        return sum
print(sum(number))


# number = int(input("Enter the number"))
# def sum_of(number):
#     if number<1:
#         return ("Number is invalid")
#     else:
#         k=0
#         for i in range(0,number+1):
#             k+=i
#         return k  

# print(sum_of(number))