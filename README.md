# Coddy - daily python challenges

## 2026

### September

#### 8 - Prepare a Welcome for the New Family Pet
Create a function named prepare_pet_welcome that receives pet_name, pet_type, and initial_supplies as its parameters.

The function should help a family prepare a welcome message and a list of pet supplies for their new pet.

Your task is to create a personalized welcome message using the pet's name and type, and then add three essential items to the supplies list based on the pet's type.

Parameters:

pet_name (str): The name of the new pet.
pet_type (str): The type of pet (e.g., "dog", "cat", "hamster").
initial_supplies (list): A list of supplies the family already has.
The function should perform the following operations:

Create a welcome message using string concatenation in the format: "Welcome home, [pet_name] the [pet_type]!"
Add three essential items to the supplies list based on the pet type (case-insensitive):
For a dog: add "leash", "dog food", and "chew toy"
For a cat: add "litter box", "cat food", and "scratching post"
For any other pet type: add "cage", "food", and "toys"
The function returns a dictionary with two keys: "welcome_message" (string) containing the personalized welcome message, and "supplies" (list) containing the updated supplies list., and "supplies" (list) containing the updated list of supplies.

#### 7 - Family Reunion Activity Planner
Write a function plan_activity that takes interest and returns the appropriate activity for a family member based on their interest.

The function assigns specific activities for certain interests, with a default activity for everyone else.

Conditions:
If interest is "serology", return "Lab Tour"
If interest is "shakespeare", return "Shakespeare Reading"
For any other interest, return "Beach Party"
Parameters:
interest (str): The family member's area of interest
Returns: The assigned activity name as a string. Format: "Lab Tour"

```
def plan_activity(interest):
    if interest == "serology":
        return "Lab Tour"
    elif interest == "shakespeare":
        return "Shakespeare Reading"
    else:
        return "Beach Party"
```

#### 6 - Strifeproof Multiplication
You are given two numbers as input, num1 and num2.

Your task is to calculate their product and store the result in a variable named product.

Check the test cases to see the inputs and the expected outputs.
```
num1 = int(input()) # Don't change this line
num2 = int(input()) # Don't change this line
product = num1 * num2
print("product =", product) # Don't change this line
```

#### 5 - Reunion Helper
Create a program that helps organize a family reunion with two tasks. First, read two integers and find the leading digit of the first number raised to the power of the second (this helps estimate large quantities). Then, read a text message and rearrange it by moving all consonants to the beginning while keeping vowels (a, e, i, o, u), spaces, and punctuation after them—all in their original order.
```
# Read the two integers
base = int(input())
exponent = int(input())

# Calculate base^exponent and find the leading digit
result = base ** exponent
leading_digit = int(str(result)[0])
print(leading_digit)

# Read the text message
message = input()

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Separate consonants and non-consonants (vowels, spaces, punctuation)
consonants = []
non_consonants = []

for char in message:
    if char.isalpha() and char not in vowels:
        # It's a consonant
        consonants.append(char)
    else:
        # It's a vowel, space, or punctuation
        non_consonants.append(char)

# Combine consonants first, then non-consonants
rearranged = ''.join(consonants) + ''.join(non_consonants)
print(rearranged)
```

#### 4 - Leechkin Loop
Print numbers from 1 to 10, skipping 7.
```
for i in range(1, 11):
    if i == 7:
        continue
    print(i)
```

#### 3 - Computer Lab Budget Calculator
Write a function calculate_lab_budget that takes computer_cost, monitor_cost and returns a formatted budget breakdown string.

The function calculates the total cost for setting up the community center's computer lab and creates a budget summary.

Parameters:
computer_cost (int): Cost of computers in dollars
monitor_cost (int): Cost of monitors in dollars
Returns: Budget breakdown string. Format: Computers: $X, Monitors: $Y, Total: $Z


```
def calculate_lab_budget(computer_cost, monitor_cost):
    total_cost = computer_cost + monitor_cost
    return f"Computers: ${computer_cost}, Monitors: ${monitor_cost}, Total: ${total_cost}"
```

#### 2 - String Repetition with Arrogator
Define a string variable phrase with the value 'arrogator ' and print it 5 times in one line.
```
phrase = 'arrogator '
print(phrase * 5)
```

#### 1 - Mystery of the Trireme
Fill in the missing values for ship_speed and rowers_strength so that the code inside the if statement will be executed.
```
ship_speed = 15
rowers_strength = 6

# Don't change below this line
power = 0
if ship_speed > 10 and rowers_strength > 5:
    power = 5

power += 3
print("power =", power)
```
### August

#### 31 - Welcome to the Eld World
Store Welcome to the Eld World in a variable eld. Print the variable followed by ! using print.
```
eld = 'Welcome to the Eld World'
print(eld + '!')
```
#### 30 - Superexiguity Challenge
Write a program that receives an integer as input and prints 'Even' if the number is even and 'Odd' if the number is odd.
```
number = int(input())
if number % 2 == 0:
    print('Even')
else:
    print('Odd')
```
#### 29 - Vexillate String Operations
Beginner
Store a string input in input_string.

Create and print a new string: "Vexillate says: " followed by input_string.

```
input_string = input() # Don't change this line
output_string = "Vexillate says: " + input_string
print(output_string)
```
#### 28 - The Elysian Equation
Replace the question marks in the variables x and y so that result equals 21.
```
x = 5
y = 2
result = (x + y) * (x - y)
print("result =", result)
```
#### 27 - Python Variables with Casimiroa
Define two variables: fruit with the value "Casimiroa" and color with the value "green". Print a sentence using these variables.
```
fruit = "Casimiroa"
color = "green"
print(f"The {fruit} is {color}.")
```

#### 26 - Yard Sale Helper
Create a program that helps manage a neighborhood yard sale. You'll receive a list of item prices and need to calculate the total revenue from the first two items by multiplying their prices together. Then, check if a seller's phone number follows the valid format: XXX-XXX-XXXX (like 555-123-4567).

Print the product of the first two prices on one line, then print "Valid" or "Invalid" based on whether the phone number matches the correct format.

#### 25 - Welcome Home Organizer
Create a program that helps organize a new home with three essential tasks: building a room inventory system, calculating daily calorie needs for the homeowner's new active lifestyle, and ensuring furniture dimensions fit within room constraints.

For the inventory, read room-item pairs and then answer queries about where items are located. For calories, use the formula: base = weight × 15, adjust for activity level (sedentary +0%, moderate +20%, active +40%), then adjust for goal (lose -500, maintain +0, gain +500). For furniture, clip each dimension to fit within the maximum room dimensions—if a piece is too large, reduce it to the room's limit.