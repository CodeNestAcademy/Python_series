# Q-1: Program to print the square of a number
number = float(input("Enter a number: "))
square = number * number
print(f"The square of {number} is {square}.")
# Q-2: Program to calculate the average of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2}, and {num3} is {average}.")
# Q-3: Program to repeat a word a specified number of times
word = input("Enter a word: ")
times = int(input("Enter the number of times to repeat the word: "))
result = word * times
print(result)
# Q-4: Program to convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
# Q-5: Program to calculate the area of a circle
radius = float(input("Enter the radius of the circle: "))
area = 3.1416 * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area}.")
