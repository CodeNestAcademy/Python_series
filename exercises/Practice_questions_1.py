#Ques 1 solve:
name = input("What is your name? ")
age = int(input("What is your age? "))
print("5 years later, you will be",age + 5,"years old")
#Ques 2 solve:
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
print("Addition: ",n1 + n2)
print("Substraction: ",n1 -n2)
print("Product: ", n1 * n2)
print("Division: ",n1 // n2)
#Ques 3 solve:
a = int(input("Give me a number: "))
b = int(input("Give me another number: "))
print("a, b before:",(a,b))
a,b = b,a
print("a, b after:",(a,b))
#Ques 4 solve:
a = int(input("What is the length of your rectangle? "))
b = int(input("What is the width of your rectangle? "))
print("The perimeter of your rectangle is: ",2*(a + b))
#Ques 5 solve:
P = int(input("What is your principal amount? "))
R = int(input("What is the rate of interest? "))
T = int(input("Time? "))
I = (P*R*T) / 100
print("Your simple interest is, ",I)
