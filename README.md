# Coddy - daily python challenges

## 2026

### August

#### 31 - Welcome to the Eld World
Store Welcome to the Eld World in a variable eld. Print the variable followed by ! using print.

eld = 'Welcome to the Eld World'
print(eld + '!')

#### 30 - Superexiguity Challenge
Write a program that receives an integer as input and prints 'Even' if the number is even and 'Odd' if the number is odd.

number = int(input())
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

#### 29 - Vexillate String Operations
Beginner
Store a string input in input_string.

Create and print a new string: "Vexillate says: " followed by input_string.
input_string = input() # Don't change this line
output_string = "Vexillate says: " + input_string
print(output_string)

#### 28 - The Elysian Equation
Replace the question marks in the variables x and y so that result equals 21.

x = 5
y = 2
result = (x + y) * (x - y)
print("result =", result)

#### 27 - Python Variables with Casimiroa
Define two variables: fruit with the value "Casimiroa" and color with the value "green". Print a sentence using these variables.
'''
fruit = "Casimiroa"
color = "green"
print(f"The {fruit} is {color}.")
'''

#### 26 - Yard Sale Helper
Create a program that helps manage a neighborhood yard sale. You'll receive a list of item prices and need to calculate the total revenue from the first two items by multiplying their prices together. Then, check if a seller's phone number follows the valid format: XXX-XXX-XXXX (like 555-123-4567).

Print the product of the first two prices on one line, then print "Valid" or "Invalid" based on whether the phone number matches the correct format.

#### 25 - Welcome Home Organizer
Create a program that helps organize a new home with three essential tasks: building a room inventory system, calculating daily calorie needs for the homeowner's new active lifestyle, and ensuring furniture dimensions fit within room constraints.

For the inventory, read room-item pairs and then answer queries about where items are located. For calories, use the formula: base = weight × 15, adjust for activity level (sedentary +0%, moderate +20%, active +40%), then adjust for goal (lose -500, maintain +0, gain +500). For furniture, clip each dimension to fit within the maximum room dimensions—if a piece is too large, reduce it to the room's limit.