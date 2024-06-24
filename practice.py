range(1,10)
for number in range(1,10):
  if number%2==0:
    print(number)
#question1
"""def find_oldest_age(age1, age2, age3):
    return max(age1, age2, age3)


age1 = int(input("Enter the first age: "))
age2 = int(input("Enter the second age: "))
age3 = int(input("Enter the third age: "))
oldest_age=find_oldest_age(age1, age2, age3)
print("The oldest age is: ",oldest_age)
#question2
def sum_of_number(a,b):
    return a+b
a=int(input("enter one numer: "))
b=int(input("enter two number: "))
result=sum_of_number(a,b)
print("the sum is: ",result)

#question3
def largest_number(lst):
    return max(lst)
input_list = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, input_list.split()))
largest = largest_number(numbers)
print("The largest number is:", largest)
#question4
def check_number(number):
    if input_number % 2 == 0:
        return "even"
    else:
        return "odd"

input_number=int(input("Enter a number: "))
result=check_number(input_number)
print(result)"""
#question5
a=int(input("enter first number: "))
b=int(input("enter second number: "))
divide=a/b
sum=a+b
difference=a-b
product=a*b
quotient=a**b
print("divide",divide)
print("sum=",sum)
print("difference",difference)
print("product",product)
print("quotient",quotient)
