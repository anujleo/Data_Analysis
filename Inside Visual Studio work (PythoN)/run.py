# # Age = int(input('Enter Your Age\n'))
# # if(Age>18):
# #     print("YES")
# # else:
# #     print("Hatt Bhosdk")

# THIS CODE ENDS HERE

# Marks = int(input("Enter Your Marks \n"))

# if (Marks<50 and Marks>-1):
#     print("Your Grade Is F")
# elif(Marks>=50 and Marks<60):
#     print("Your Grade Is D")
# elif(Marks>=60 and Marks<70):
#     print("Your Grade Is C")
# elif(Marks>=70 and Marks<80):
#     print("Your Grade Is B")
# elif(Marks>=80 and Marks<90):
#     print("Your Grade Is A")
# elif(Marks>=90 and Marks<100):
#     print("Your Grade Is Exceptional")
# else:
#     print("Please Enter Relevant Marks out of 100")


#  THIS CODE ENDS HERE

# i = 0
# while i<5:
#     print("Harry")
#     i=i+1

# THIS CODES ENDS HERE


# fruits = ['Banana', 'Apple', 'Brocolli', 'Mango', 'Guava']

# for text in fruits:
#     print(text)   This text word give no. of elements in list


# THIS CODE ENDS HERE 


# num = int(input("Enter the number "))
# for i in range(2, num):
#     if (num%i == 0):
#         print("The Number Is Not a Prime No.")
#     else:
#         print("this no. is a prime no.")
#         break

# THIS CODE ENDS HERE 


# num = int(input("Enter the number: "))
# prime = True
# for i in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break

# if prime:
#     print("This number is a prime number.")
# else:
#     print("This number is not a prime number.")

   # THIS CODE ENDS HERE            


# n = int(input("Enter Your Number "))
# print((n/2)*(2*n+(n-1)))


   # THIS CODE ENDS HERE   

# i = 1
# while i<=50:
#     print(i)
#     i=i+1


# THIS CODE ENDS HERE   


# num = int(input("enter your number here"))
# factorial = 1
# for i in range(1, num+1):
#     print(factorial)
#     factorial = factorial * i
# print(f"The Factorial of {num} is {factorial}")

# THIS CODE ENDS HERE   

# num = int(input("enter your number here"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
#     print(factorial)

# THIS CODE ENDS HERE   


# num = int(input("Enter Your Number Here "))
# sum = 0
# i = 1
# while i<=num:
#     sum = sum+i
#     i = 1+i
# print(f"The Sum of first {num} natural numbers is {sum}")


# THIS CODE ENDS HERE 


# num = int(input("Enter Your Number "))
# factorial = 1
# i = 1
# while i <= num:
#     factorial = factorial*i
#     i = i+1
# print(f"The factorial of {num} is {factorial}")


# THIS CODE ENDS HERE 

# num = int(input("Enter Your Number Here "))
# Prime = True
# for i in range(2, num):
#     if (num%i == 0):
#         Prime = False
#         break
    
# if Prime:
#     print(f"The number {num} is prime")
# else:
#     print(f"The Number {num} is not prime")


# THIS CODE ENDS HERE 


# num = int(input("Enter Your Number Here "))
# i = 1 
# while i<=10:
#     num1 = num*i
#     print(num, "X", i, "=", num1)
#     i = i+1

# THIS CODE ENDS HERE

# def greet(name):
#     print("Good Day," + name)

# greet("anuj")


# THIS CODE ENDS HERE


# num = 4*5

# print("The multiplication of 4 and 5 is, " + str(num))


# THIS CODE ENDS HERE


# num1 = int(input("Enter First Number "))
# num2 = int(input("Enter second Number "))
# num3 = int(input("Enter third Number "))

# if (num1>num3):
#     if (num2>num1):
#         print(f"{num2} is greatest among all")
#     else:
#         print(f"{num1} is greatest among all")
# else:
#     if (num3>num2):
#         print(f"{num3} is greatest among all")
#     else:
#         print(f"{num2} is greatest among all")


# THIS CODE ENDS HERE


# def Celcius(C):
#     return ((C*9/5)+32)

# print(Celcius(0))


# THIS CODE ENDS HERE


# def sum_r(n):
#     if (n==0):
#         return 0
#     else:
#         return n + sum_r(n-1)
    
# k = sum_r(2)
# print("The Sum of first", 2, "natural number is", str(k))   


# THIS CODE ENDS HERE
    

# f = open('table2.txt', 'w')
# i=1
# while i<=10:
#     table = (2*i)
#     f.write(f"2 X {i} = {table}\n")
#     i = i+1

# f = open('table3.txt', 'w')
# i=1
# while i<=10:
#     table = (3*i)
#     f.write(f"3 X {i} = {table}\n")
#     i = i+1


# f = open('table4.txt', 'w')
# i=1
# while i<=10:
#     table = (4*i)
#     f.write(f"4 X {i} = {table}\n")
#     i = i+1
        
   
# f = open('table5.txt', 'w')
# i=1
# while i<=10:
#     table = (5*i)
#     f.write(f"5 X {i} = {table}\n")
#     i = i+1


# f = open('table6.txt', 'w')
# i=1
# while i<=10:
#     table = (6*i)
#     f.write(f"6 X {i} = {table}\n")
#     i = i+1

# f = open('table7.txt', 'w')
# i=1
# while i<=10:
#     table = (7*i)
#     f.write(f"7 X {i} = {table}\n")
#     i = i+1


# f = open('table8.txt', 'w')
# i=1
# while i<=10:
#     table = (8*i)
#     f.write(f"8 X {i} = {table}\n")
#     i = i+1


# f = open('table9.txt', 'w')
# i=1
# while i<=10:
#     table = (9*i)
#     f.write(f"9 X {i} = {table}\n")
#     i = i+1


# f = open('table10.txt', 'w')
# i=1
# while i<=10:
#     table = (10*i)
#     f.write(f"10 X {i} = {table}\n")
#     i = i+1   

# THIS CODE ENDS HERE


# class chutiya:
#     company = "EA"
#     job = "Server maintainence"

# anuj = chutiya()
# anuj.salary = str('9500$')
# print(anuj.salary)
# print(anuj.company)
# print(anuj.job)

# THIS CODE ENDS HERE

# class employee:
#     @staticmethod
#     def greet():
#         print("Hello welcome to the club")
    
# anuj = employee()
# anuj.greet()

# THIS CODE ENDS HERE

class employee:
    def greet(uiuih):
        print("Hello welcome to the club")
    
anuj = employee()
k = anuj.greet()
print(k)

# THIS CODE ENDS HERE


# class programmer:
#     company = "accenture"
#     salary = "200k"
#     location = "India"
#     designation = "senior developer"

#     def info(self, signature, mobileno):
#         print(f"The name of  is {self.c}")
      

#     def greet():
#         print("Hello Gentleman")

   
    

# anuj = programmer()   
# print(anuj.salary)

# THIS CODE ENDS HERE



