# tickets = [
#     {
#         "ticket_id": "OPS-1042",
#         "customer": "a",
#         "hours": 1,
#         "status": "open",
#         "opened_on": "2026-01-01"
#     },
#     {
#         "ticket_id": "OPS-1043",
#         "customer": "b",
#         "hours": 2,
#         "status": "closed",
#         "opened_on": "2026-01-02"
#     },
#     {
#         "ticket_id": "OPS-1044",
#         "customer": "c",
#         "hours": None,
#         "status": "open",
#         "opened_on": "2026-01-03"
#     }
# ]
# # print( tickets[1].get("customer", "unknown"))
# for ticket in tickets:
#     print(ticket.get("hours","not found"))

# while True:
#     try:
#         print("Enter a number: ")
#         number = int(input())
#         print(f"You entered: {number * 2}")
#         break
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")


# a= input("Enter a number: ")
# b= input("Enter a secondnumber: ")
# c= (int(a)+int(b))/2

# # print(a<=b and b>=a )
# print("The average of the two numbers is: ", c)


# str="apple"
# print(len(str))

from this import d
from tkinter import WORD


# str="apple"
# print(str[1:])


# str="apple"
# print(str.endswith("e") and str.endswith("a"))


# str="apple"
# print(str.capitalize())

# str="apple"
# print(str.replace("p", "z"))

# str="apple"
# print(str.upper())

# str = input("write your name")
# print(f"Hello, {str}!")
# print(len(str))
# print(str.count("a"))

# age = input("Enter your age: ")
# if((int(age)>=18)):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
#     print(f"Yor are {18-int(age)} years away from voting")


# marks = int(input("Enter your marks: "))
# if marks >= 75:
#     print("You are eligible for a scholarship") 
# elif marks >= 60:
#     print("You are semi eligible for a scholarship")
#     print(f"You are {75-int(marks)} marks away from the scholarship")
# else:print('You are not eligible for a scholarship')



#Check the even odd number by user

# num = int(input("Enter a number: "))
# if(num%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")

#Check the number multiple of 7 or not  by user
# num = int(input("Enter a number: "))
# if(num%7==0):
#     print("The number is multiple of 7")
# else:
#     print("The number is not multiple of 7")


#Check the highest number between three numbers by user
# num1 = int(input("Enter first number: ")) 
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if(num1>num2 and num1>num3):
#     print(f"The highest number is: {num1}")
# elif(num2>num1 and num2 >num3):
#     print(f"The highest number is: {num2}")
# else:
#     print(f"The highest number is: {num3}")



#Lists
# fruits = ["apple", "anana", "cherry"]
# print(fruits[1])
# fruits[1] = "zlackberry"
# print(fruits)
# fruits.append("orange")
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
# fruits.insert(0, "watermelon")
# print(fruits)


#take 3 inputs from user and add them in lists
# fruits=[]
# for i in range(3):
#     fruit = input("Enter a fruit: ")
#     fruits.append(fruit)
# print(fruits)

#take 3 inputs from user and add them in lists
# numbers=[]
# for i in range(3):
#     num=int(input("Enter a number: "))
#     numbers.append(num)
# print(numbers)
# numbers.sort()
# print(numbers)
# if(numbers.count(2)):
#     print("5 is found in the list")
# else:
#     print("5 is not found in the list")




#check the palindrome
# num=[1,3,5,3,1]
# palindrome=num.copy()
# palindrome.reverse()
# if(palindrome==num):
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")



#store following words in python dictionary
# table : "a piece of furniture", "lists of facts & figure"
# cat: "a small animal"

# dictionary = {}
# print(type(dictionary))
# dictionary["table"] = "a piece of furniture"
# print(dictionary)
# dictionary["cat"] = "a small animal"
# print(dictionary)
# dictionary.update({"dog": "sweet animal"})
# print(dictionary)
# # dictionary.pop("cat")
# # print(dictionary)
# # print(dictionary.items())


# for i in dictionary.items():
#     print(f"items {i}")


# results = {}
# sub1 = input("Enter your subject 1: ")
# marks1 = int(input("Enter your marks: "))
# sub2 = input("Enter your subject 2: ")
# marks2 = int(input("Enter your marks: "))
# sub3 = input("Enter your subject 3: ")
# marks3 = int(input("Enter your marks: "))

# results[sub1] = marks1
# results[sub2] = marks2
# results[sub3] = marks3
# print(results)






#loops


# num = 5 
# while num >= 1:
#     print(num * "*")
#     num -= 1


# num = int(input("Enter a number: "))
# num2=1 
# while num2 <= 10:
#     print(num * num2)
#     num2  += 1



# i=0

# nums = [1,2,3,2,5,6,7,29,9,10]
# while i< len(nums):
#     print(nums[i])
#     i += 1


# i=0

# nums = [1,2,3,2,5,6,7,29,9,10]
# while i< len(nums):
#     if(nums[i]==2):
#         print(f"2 is found at index {i}")
#     else:
#         print(f"2 is not found at index {i}")
#     i += 1


# for i in range(2,10):
#     print(i)



#sum of n numbers using while loop
# num = int(input("Enter a number: "))
# sum = 0
# i=1
# while i<=num:
#     print(i)
#     sum += i
#     i += 1
# print(sum)


# i=0
# num = int(input("enter a number "))
# sum = 0
# while i<=num:
#     print(i)
#     sum += i
#     i += 1
# print(sum)

#Write a program to print length of list.
# def lenght_of_list(list,num):
#     for i in list:
#         print(i)
#         ans = i+num
#         print(ans)
#     return (ans)
# list=lenght_of_list([1,2,3,4,5],2)
# print(list)




#convert usd to inr

# def convert_inr_to_usd(inr):
#     return inr/91

# val= convert_inr_to_usd(int(input("enter the amount in inr: ")))
# print(val)


# def odd_even(num):
#     if(num%2==0):
#         return "even"
#     else:
#         return "odd"
# num=int(input("enter a number: "))
# print(odd_even(num))


# def sum(n):
#     ans=0
#     for i in range(1,n+1):
#         ans+=i
#         i+=1
#         print(ans)
#     return ans


# num=sum(int(input("enter a number: ")))
# print(num)

# def sum_of_numbers(n):
#     #n=5
#     if(n==0):
#         return 0
#     else:
#         return n+sum_of_numbers(n-1)
#         #5+sum_of_numbers(4)
#         #5+4+sum_of_numbers(3)
#         #5+4+3+sum_of_numbers(2)
#         #5+4+3+2+sum_of_numbers(1)
#         #5+4+3+2+1+sum_of_numbers(0)
#         #5+4+3+2+1+0
#         #15

# num=sum_of_numbers(int(input("enter a number: ")))
# print(num)

# f=open("week-01-python-foundations/sample.txt", "w+")
# f.write("1234567890")
# # print(f.read())
# f.close()




# with open("sample2.text","w") as f:
#     f.write("This is the second demo file written by python\n this is the second line of the file\n this is the third line of the file")


# with open("./week-01-python-foundations/sample2.txt", 'r') as f:
#  str=f.read()
#  if str.find("5"):
#     new_str=str.replace("This", "HMMMMMM")  
#     print(new_str)
#  else:
#     print("5 is not found in the file")
# with open("./week-01-python-foundations/sample2.txt", 'w') as f:
#     f.write(new_str)
#     print(new_str)
# with open("./week-01-python-foundations/sample2.txt", 'r') as f:
#     print(f.read())


def checkname(word):
    line=1
    data=True
    with open("./week-01-python-foundations/sample2.txt", 'r') as f:
       while data:
        data=f.readline()
        if(word in data):
            print(f"Word {word} found at line {line}")
            return
        line+=1    
    print(f"Word {word} not found ")
    return -1
    
       
ans=checkname("third--")
print(ans)