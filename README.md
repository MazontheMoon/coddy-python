# Coddy - Daily Python Challenges

## 2026

### October

#### 30 - Rare Book Catalog Entry
Write a function create_catalog_entry that takes title, year, value and returns a formatted catalog entry string.

The function creates a standardized library catalog entry by combining the book information with calculated handling fee.

Parameters:

title (str): The book's title
year (int): Publication year
value (int): Estimated value in dollars
The handling fee is 5% of the value, rounded down to whole dollars. For example, a value of 25 gives a fee of 1 and a value of 10 gives 0.

Returns: Formatted catalog entry string. Format: Title: [title] | Year: [year] | Value: $[value] | Fee: $[fee]

```
def create_catalog_entry(title, year, value):
    fee = value * 5 // 100
    return f"Title: {title} | Year: {year} | Value: ${value} | Fee: ${fee}"

```

#### 29 - Planning the Herb Garden Plot
Write a function plan_herb_garden that takes plot_size (float), volunteers (int), and include_rare (bool) and returns a formatted string about the garden allocation.

The function calculates how much space each volunteer gets by dividing the total plot size by the number of volunteers, then formats this information along with whether rare herbs (like knotted marjoram) will be included.

Parameters:

plot_size (float): Total garden area in square meters
volunteers (int): Number of people helping with the garden
include_rare (bool): Whether to plant rare herbs
Returns: A formatted string showing space per volunteer and rare herb status. Format: Each volunteer gets X square meters. Rare herbs: Yes/No

#### 28 - Gorgonin Counter
Complete the code to print 'Gorgonin' when the count is greater than 3.
```
count = 0
while count < 5:
    count += 1
    if count > 3:
        print('Gorgonin')
```

#### 27 - Seats for Every Passenger
Read a passenger count and a seats-per-vehicle count on separate lines. Print the smallest number of vehicles that can seat everyone. A partly filled vehicle still counts. With zero passengers, print 0. Passengers is from 0 to 10000; seats is from 1 to 100.

End each output line with a newline. Print only the requested output, with no input prompts.
```
passengers = int(input())
seats = int(input())
print((passengers + seats - 1) // seats)

```

#### 26 - Apprentice's Weekly Assessment
Create a program that helps you manage your apothecary apprentice duties. You'll receive three ingredient measurements (in drams) and a performance score, each as a whole number on its own line.

First, check if the three measurements form a geometric progression, where each value equals the previous one multiplied by the same ratio. A sequence whose first measurement is 0 is not geometric. Print Geometric or Not geometric.

Then calculate your weekly bonus: start with 10.0 silver coins, multiply by 1.5 if your performance is from 80 to 89, or multiply by 2.0 if it is from 90 to 100. Any other score keeps the bonus at 10.0. Print the bonus with one decimal place, for example 15.0.

```
# Read the three ingredient measurements and performance score
a = int(input())
b = int(input())
c = int(input())
performance = int(input())

# Check if the measurements form a geometric progression
# In a geometric progression: b/a = c/b (the ratio is constant)
# To avoid division issues, we can check: b * b = a * c
if a != 0 and b * b == a * c:
    print("Geometric")
else:
    print("Not geometric")

# Calculate weekly bonus
bonus = 10.0
if 80 <= performance <= 89:
    bonus *= 1.5
elif 90 <= performance <= 100:
    bonus *= 2.0

print(f"{bonus:.1f}")

```

#### 25 - Turn a Row and Seat Into a Ticket Number
Read the number of seats per row, a row number and a seat number on separate lines. Ticket numbers start at 1, increase across each row, then continue on the next row. Print the ticket number using (row - 1) * seatsPerRow + seat. Seats per row and row number are from 1 to 100; the seat number is from 1 through the seats-per-row count. For inputs 4, 2 and 3, print 7.

End each output line with a newline. Print only the requested output, with no input prompts.
```
width = int(input())
row = int(input())
seat = int(input())
print((row - 1) * width + seat)

```

#### 24 - Round a Whole Number to the Nearest Ten

Read an integer from 0 to 10000. Print the nearest multiple of ten. If it is exactly halfway between two multiples, choose the larger one. For 25, print 30.

End each output line with a newline. Print only the requested output, with no input prompts.

```
n = int(input())
print(((n + 5) // 10) * 10)

```

#### 23 - Round a Whole Number to the Nearest Ten

Read an integer from 0 to 10000. Print the nearest multiple of ten. If it is exactly halfway between two multiples, choose the larger one. For 25, print 30.

End each output line with a newline. Print only the requested output, with no input prompts.

```
n = int(input())
print(((n + 5) // 10) * 10)
```

#### 22 - Garden Plot Assignment
Create a program that reads a garden plot name and number, then formats the name properly and determines if the plot gets extra sun exposure.

First, capitalize the first letter of each word in the plot name. Then check if the plot number is a "sunny number" - a number where adding 1 gives a perfect square (like 8, because 8+1=9=3²). Print the formatted name, then "Sunny plot" if it's sunny, or "Shaded plot" otherwise.

```
# Read the plot name and number
plot_name = input()
plot_number = int(input())

# Capitalize the first letter of each word
formatted_name = plot_name.title()

# Check if the plot number is a "sunny number"
# A sunny number is one where adding 1 gives a perfect square
next_number = plot_number + 1

# Check if next_number is a perfect square
# We can do this by taking the square root and checking if it's an integer
import math
sqrt_value = math.sqrt(next_number)
is_sunny = sqrt_value == int(sqrt_value)

# Print the formatted name
print(formatted_name)

# Print whether it's sunny or shaded
if is_sunny:
    print("Sunny plot")
else:
    print("Shaded plot")
```

#### 21 - Exactly One of Three Switches Is On
Read three switch states on separate lines. Each is 0 for off or 1 for on. Print ONE if exactly one switch is on; otherwise print OTHER.

End each output line with a newline. Print only the requested output, with no input prompts.
```
a = int(input())
b = int(input())
c = int(input())
if a + b + c == 1:
    print("ONE")
else:
    print("OTHER")
```

#### 20 - Break Seconds Into Three Clock Units
Read a nonnegative duration in seconds, from 0 to 86399. Print three integers on one line, separated by single spaces: complete hours, remaining complete minutes, remaining seconds. Do not pad the numbers with zeroes. For 3661, print 1 1 1.

End each output line with a newline. Print only the requested output, with no input prompts.

```
seconds = int(input())
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining = seconds % 60
print(hours, minutes, remaining)

```

#### 19 - Work Out a Parking Fee
A car park charges by the number of whole hours parked: up to 1 hour is free, up to 3 hours costs 4, up to 8 hours costs 9, and anything longer costs 15. Members pay half of any fee, rounded down.

Read the hours parked and whether the driver is a member (true or false). Print Fee: followed by the amount. For 5 and true:

Fee: 4

```
hours = int(input())
is_member = input() == "true"

if hours <= 1:
    fee = 0
elif hours <= 3:
    fee = 4
elif hours <= 8:
    fee = 9
else:
    fee = 15
if is_member:
    fee = fee // 2
print(f"Fee: {fee}")

```

#### 18 - Swap Two Seat Numbers
Two friends booked seats, and they want to trade. Read the first friend's seat on the first line and the second friend's seat on the second line.

Swap the values so that first_seat holds the second friend's old seat and second_seat holds the first friend's old seat. Use a third variable to keep one value while you move the other. Then print:

first_seat = 14C
second_seat = 2A
That example is for the input 2A and 14C.

```
first_seat = input()
second_seat = input()

temp = first_seat
first_seat = second_seat
second_seat = temp

print(f"first_seat = {first_seat}")
print(f"second_seat = {second_seat}")

```

#### 17 - Print a Welcome Home Banner
A family hangs a banner on the door for someone coming home from a long trip. Read that person's name on one line.

Print a banner of four lines: a row of ten equals signs ==========, then WELCOME HOME, then the name, then the same row of equals signs again.

For Mia:

==========
WELCOME HOME
Mia
==========

```
name = input()

print("==========")
print("WELCOME HOME")
print(name)
print("==========")

```

#### 16 - Apply a Discount in Whole Coins
Read a price and a discount percentage on separate lines. First compute the discount in whole coins by rounding price * percentage / 100 down. Subtract that whole-coin discount from the original price and print the result. Price is from 0 to 10000, and percentage is from 0 to 100. For price 19 and percentage 10, the discount is 1 coin and the result is 18.

End each output line with a newline. Print only the requested output, with no input prompts.

```
price = int(input())
percentage = int(input())
discount = (price * percentage) // 100
print(price - discount)

```

#### 15 - Reschedule a Dentist Appointment
A dentist's office moves an appointment and keeps a note of the old time. Read the current appointment on the first line and the new one on the second line.

Save the current appointment in a new variable named old_day, then change day to the new appointment. The starter code already prints both variables, in the form Appointment: DAY and Moved from: OLD_DAY.

For Tuesday 10:00 and Friday 15:30:

Appointment: Friday 15:30
Moved from: Tuesday 10:00

```
day = input()
new_day = input()

old_day = day
day = new_day

print(f"Appointment: {day}")
print(f"Moved from: {old_day}")

```

#### 14 - Even or Odd for Signed Input
Read an integer from -10000 to 10000. Print EVEN if it is divisible by two, including zero. Otherwise print ODD. Negative odd numbers must also print ODD.

End each output line with a newline. Print only the requested output, with no input prompts.

```
n = int(input())
if n % 2 == 0:
    print("EVEN")
else:
    print("ODD")
```

#### 13 - Print the Places of a Three-Digit Number
Read an integer from 100 to 999. Print its hundreds, tens and units digits on one line separated by single spaces, in that order. Include zero digits. For 407, print 4 0 7.

End each output line with a newline. Print only the requested output, with no input prompts.
```
n = int(input())
print(n // 100, (n // 10) % 10, n % 10)
```

#### 12 - Count Characters on an Input Line
Read one line and print its character count as an integer. Count internal spaces too; do not count the line ending. The input has 1-60 ASCII letters, digits or spaces and no leading or trailing space. For A B, print 3.

End each output line with a newline. Print only the requested output, with no input prompts.
```s = input()
print(len(s))
```

#### 11 - Add Numbers From Three Input Lines
Read three integers, each on its own line, and print their sum on one line. Each integer is between -1000 and 1000. Read the input as numbers before adding.

End each output line with a newline. Print only the requested output, with no input prompts.
```a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

#### 10 - Print
Read one line of text. Print it between [ and ], with exactly one added space after the opening bracket and before the closing bracket. Preserve every character of the input. The line has 1-60 ASCII letters, digits or spaces, with no leading or trailing space. For input Green tea, print [ Green tea ].

End each output line with a newline. Print only the requested output, with no input prompts.
```s = input()
print("[", s, "]")
```
#### 9 - Light Up a Theater Marquee
A theater puts tonight's show on the sign above its door. Read the play, the lead actor, the second actor and the curtain time, each on its own line.

Print eight lines: TONIGHT ONLY, the play, starring, the lead actor, and, the second actor, Curtain at and the time.

For Hamlet, Ada Stone, Leo Park and 19:30:
TONIGHT ONLY
Hamlet
starring
Ada Stone
and
Leo Park
Curtain at
19:30

```
play = input()
lead = input()
second = input()
time = input()

print("TONIGHT ONLY")
print(play)
print("starring")
print(lead)
print("and")
print(second)
print("Curtain at")
print(time)

```

#### 8 - Choose a Thermostat Mode
Read the room temperature on the first line and the target temperature on the second, both whole degrees.

Print Mode: Heat when the room is more than 1 degree below the target, Mode: Cool when it is more than 1 degree above it, and Mode: Hold otherwise.

For 18 and 21:

Mode: Heat

```room = int(input())
target = int(input())

if room < target - 1:
    print("Mode: Heat")
elif room > target + 1:
    print("Mode: Cool")
else:
    print("Mode: Hold")
```

#### 7 - Announce a Song on the Radio

A radio host reads the song details from a card. Read the song title, the artist and the title of the next song, each on its own line.

Print six lines: Now playing:, the song title, by, the artist, Coming up next: and the next song's title.

For Yellow Submarine, The Beatles and Here Comes the Sun:

Now playing:
Yellow Submarine
by
The Beatles
Coming up next:
Here Comes the Sun

```
song = input()
artist = input()
next_song = input()

print("Now playing:")
print(song)
print("by")
print(artist)
print("Coming up next:")
print(next_song)

```

#### 6 - Print a Wedding Table Card
Each wedding guest gets a card at their seat. Read the table number on the first line and the guest's name on the second line.

The card shows the name before the table number. Print four lines: Welcome to our wedding, the guest's name, Your table is, and the table number.

For the input 7 and Ada Lovelace:

Welcome to our wedding
Ada Lovelace
Your table is
7


```
table = input()
guest = input()

print("Welcome to our wedding")
print(guest)
print("Your table is")
print(table)
```
#### 5 - Check a Parcel Against the Weight Limit
A courier accepts parcels up to a weight limit. Read the parcel weight on the first line and the limit on the second, both whole kilograms.

Print three lines: whether the parcel is over the limit, whether it is exactly at the limit, and how many kilograms are left before the limit (negative when it is over).

For a weight of 12 and a limit of 20:
Over limit: False
Exactly at limit: False
Kilograms left: 8
Print only these lines, with no input prompts.

```
weight = int(input())
limit = int(input())

over = weight > limit
exact = weight == limit
left = limit - weight

print(f"Over limit: {over}")
print(f"Exactly at limit: {exact}")
print(f"Kilograms left: {left}")
```

#### 4 - Decide on Free Shipping
A shop ships for free when the order total is at least 50, or when the customer is a member and the order is not a bulky item.

Read the order total (a whole number), whether the customer is a member and whether the item is bulky (true or false), each on its own line. 
Print Free shipping: followed by True or False.
For 30, true and false:
Free shipping: True
Print only these lines, with no input prompts.

```
total = int(input())
is_member = input() == "true"
is_bulky = input() == "true"

free = total >= 50 or (is_member and not is_bulky)
print(f"Free shipping: {free}")
```
#### 3 - Fill In a Conference Badge
Read a first name, a last name and a role, each on its own line. Store the full badge text in a variable named badge in the form ROLE: FIRST LAST, and set a variable printed to True.

Then print both variables. For the input Ada, Lovelace and Speaker:
badge = Speaker: Ada Lovelace
printed = True
Print only these lines, with no input prompts.
```
first = input()
last = input()
role = input()

badge = f"{role}: {first} {last}"
printed = True

print(f"badge = {badge}")
print(f"printed = {printed}")

```

#### 2 - Can the Roller Coaster Start
A rider may board when they are at least 120 cm tall and at least 8 years old, or when they are at least 110 cm tall and riding with an adult.

Read the height, the age, and whether an adult rides along (true or false), each on its own line. Print Can ride: followed by True or False.

For 115, 7 and true:

Can ride: True
Print only these lines, with no input prompts.

```
height = int(input())
age = int(input())
with_adult = input() == "true"

can_ride = (height >= 120 and age >= 8) or (height >= 110 and with_adult)
print(f"Can ride: {can_ride}")
```

#### 1 - Sleep In on the Weekend
Days are numbered from 1 (Monday) to 7 (Sunday). You sleep in when the day is 6 or 7 and no alarm is set.

Read the day number and whether an alarm is set (true or false). Print whether it is the weekend, then whether you sleep in. For 6 and true:

Weekend: True
Sleep in: False
Print only these lines, with no input prompts.

```
day = int(input())
alarm = input() == "true"

weekend = day >= 6
sleep_in = weekend and not alarm
print(f"Weekend: {weekend}")
print(f"Sleep in: {sleep_in}")

```

### September

#### 30 - Vaccine Eligibility Checker
Create a function named vaccine_eligibility that receives age, has_allergies, and previous_reactions as its parameters.

The function should determine whether a patient is eligible for a vaccine based on their age and medical history. This challenge simulates a scenario where a nurse at a local clinic needs to assess patient eligibility for vaccination.

Use conditional statements and logical operators to implement the following eligibility criteria:
Patients under 12 years old are not eligible for the vaccine.
Patients 12 years and older are eligible, but with different recommendations based on their medical history:
If they have allergies or previous adverse reactions to vaccines, they should consult with a doctor first.
If they have no allergies and no previous reactions, they can proceed with the vaccine.

Parameters:
age (int): The patient's age in years.
has_allergies (bool): Whether the patient has any known allergies (True if they have allergies, False otherwise).
previous_reactions (bool): Whether the patient has had previous adverse reactions to vaccines (True if they have had reactions, False otherwise).
The function should return a string indicating whether the patient is eligible for the vaccine and any precautions or recommendations.

Ensure your implementation uses if-else statements and logical operators efficiently to determine the appropriate output based on the input conditions.



#### 29 - Library Access Control System
Write a function process_library_access that takes member_level, current_checkouts, book_available and returns a boolean indicating checkout approval.

The function processes library member access by incrementing checkout counters based on membership type and validating multiple conditions for book checkout eligibility.

Logic:
Increment current_checkouts by 1 if member_level is "premium" or by 2 if "standard"
Check if updated checkout count doesn't exceed limits: premium (10 books), standard (5 books), basic (3 books)
Approve checkout only if book is available AND checkout limit not exceeded

Conditions:
Premium members: increment by 1, limit 10 books
Standard members: increment by 2, limit 5 books
Basic members: no increment, limit 3 books
Book must be available for any approval

Parameters:
member_level (str): Member type ("premium", "standard", or "basic")
current_checkouts (int): Current number of books checked out
book_available (bool): Whether the requested book is available
Returns: Boolean indicating if checkout is approved. Format: True or False

#### 28 - Family Reunion RSVP Checker
Write a function check_reunion_attendance that takes name, is_available, rsvp_confirmed and returns a personalized message string.

The function checks if a family member can attend the reunion on the 28th and creates an appropriate message based on their availability and RSVP status.

Conditions:
If both available AND RSVP confirmed: return confirmation message
If not available OR RSVP not confirmed: return regret message

Parameters:
name (str): Family member's name
is_available (bool): Whether they're available on the 28th
rsvp_confirmed (bool): Whether they confirmed their RSVP
Returns: Personalized message string. Format: "Hi [name], we're excited to see you at the family reunion on the 28th!" or "Hi [name], we're sorry you can't make it to the family reunion on the 28th."

```
def check_reunion_attendance(name, is_available, rsvp_confirmed):
    if is_available and rsvp_confirmed:
        return f"Hi {name}, we're excited to see you at the family reunion on the 28th!"
    else:
        return f"Hi {name}, we're sorry you can't make it to the family reunion on the 28th."
```

#### 27 - Check Three Readings in Order

```
a = int(input())
b = int(input())
c = int(input())
if a <= b and b <= c:
    print("ORDERED")
else:
    print("UNORDERED")

```

#### 26 - Repeat an Input Message on Separate Line
Read a count on the first line and a message on the second. Print the message on exactly that many output lines. The count is from 1 to 20. The message contains 1-60 ASCII letters, digits or spaces, without leading or trailing space. Preserve the message exactly.

End each output line with a newline. Print only the requested output, with no input prompts.
```
count = int(input())
message = input()
i = 0
while i < count:
    print(message)
    i += 1
```

#### 25 - Detect a Value Outside a Window
Read a value, a lower limit and an upper limit on separate lines. Print OUTSIDE if the value is below the lower limit or above the upper limit. Otherwise print INSIDE. The endpoints are inside. All inputs are from -1000 to 1000, and the lower limit does not exceed the upper limit.

End each output line with a newline. Print only the requested output, with no input prompts.
```
value = int(input())
lower = int(input())
upper = int(input())
if value < lower or value > upper:
    print("OUTSIDE")
else:
    print("INSIDE")
```

#### 24 - Pirate Captain's Hull Repair
Create a function named repair_pirate_ship that receives wood_planks, nails, and damage_size as its parameters.

The function should determine if the pirate captain has enough materials to repair the ship's hull.

To repair the ship, the captain needs:

At least 5 wood planks for every 1 unit of damage
At least 2 nails for every 1 wood plank used
Use basic logical operators and variable assignments to check if the captain has sufficient materials.

Parameters:

wood_planks (int): The number of wood planks available
nails (int): The number of nails available
damage_size (int): The size of the damage to the hull
The function returns a boolean value: True if the captain has enough materials to repair the ship, False otherwise.

#### 23 - Deliver Two Lines in Reverse Order
Read two lines of text. Print the second line first and the first line second, on separate output lines. Each input line contains 1-60 ASCII letters, digits or spaces and has no leading or trailing space. Preserve internal spaces and letter case.

End each output line with a newline. Print only the requested output, with no input prompts.

```
first = input()
second = input()
print(second)
print(first)
```

#### 22 - Show a Balance After Each Update
Read a starting balance, a deposit and a withdrawal on separate lines. Print the balance after adding the deposit. Then subtract the withdrawal from that updated balance and print the final balance on the next line. All three inputs are from 0 to 1000. A negative final balance is allowed.

End each output line with a newline. Print only the requested output, with no input prompts.
```
balance = int(input())
deposit = int(input())
withdrawal = int(input())
balance += deposit
print(balance)
balance -= withdrawal
print(balance)
```

#### 21 - Exchange Two Stored Numbers
Read two integers on separate lines. Exchange their values and print the resulting first value followed by the resulting second value, separated by one space. Each input is from -1000 to 1000. For inputs 4 and 9, print 9 4.

End each output line with a newline. Print only the requested output, with no input prompts.

```
a = int(input())
b = int(input())
saved = a
a = b
b = saved
print(a, b)
```

#### 20 - Describe the Order of Two Numbers
Read two integers on separate lines. Print LESS, EQUAL or GREATER to describe the first number compared with the second. Both inputs are from -10000 to 10000.

End each output line with a newline. Print only the requested output, with no input prompts.
```
a = int(input())
b = int(input())
if a < b:
    print("LESS")
else:
    if a == b:
        print("EQUAL")
    else:
        print("GREATER")

```

#### 19 - Print a Two-Line Parcel Label
Read an item name on the first line and an integer quantity on the second. Print Item: followed by the name, then Quantity: followed by the quantity on the next line. Each colon is followed by one space. The name contains 1-60 ASCII letters and internal spaces. Quantity is from 0 to 1000.

End each output line with a newline. Print only the requested output, with no input prompts.
```
name = input()
quantity = int(input())
print("Item:", name)
print("Quantity:", quantity)

```

#### 18 - Compare Two Groupings of an Expression
Read integers a, b and c on separate lines. Print a + b * c on the first output line and (a + b) * c on the second. Each input is from 0 to 100.

End each output line with a newline. Print only the requested output, with no input prompts.
```
a = int(input())
b = int(input())
c = int(input())
print(a + b * c)
print((a + b) * c)
```

#### 17 - Loyalty Program Validator

Check if the username is valid (3-15 characters, letters/numbers/underscores only, can't start with a number), verify the balance is a valid decimal number, and calculate the estimated wait time (5 minutes per customer ahead in queue). Print "Valid" or "Invalid" for each check, followed by the wait time in minutes.

#### 16 - Romantic Picnic Cost Calculator
Write a function calculate_picnic_cost that takes sandwich_price, drink_price, dessert_price, flower_price and returns a formatted romantic message with the total cost.

The function calculates the total cost of all picnic items and creates a romantic summary message.

Parameters:
sandwich_price (float): Price of sandwiches
drink_price (float): Price of drinks
dessert_price (float): Price of desserts
flower_price (float): Price of flowers
Returns: A formatted string with basket contents and total cost. Format: "Our romantic picnic basket contains sandwiches, drinks, desserts, and flowers for $X.XX total"


#### 15 - Opening Night Guest Count & Final Sales
Create a program that reads a sentence from the guest list and counts how many words start with a vowel (a, e, i, o, u - case insensitive). Then read a list of ticket prices (one per line) (one per line until the end of input) (one per line) and calculate the sum of the last two prices.

Print the vowel count on the first line and the sum of the last two prices on the second line.

#### 14 - Counting Notes and Buying Cornice
Create a program that reads a renovation note and counts how many words are in it. Then, read your budget and the price per cornice piece, and calculate how many complete pieces you can afford to buy.

Print the word count first, then the number of pieces you can purchase (remember: only whole pieces!).

#### 13 - Aquarium Management System
Create a program that manages three different calculations for the damselfish aquarium exhibit. Your program should read a calculation type (1, 2, or 3) and then perform the corresponding operation:

Type 1 - Penalty Calculator: Read a violation count and calculate the penalty. Start with a base of 50, add 25 per violation, then add 10% of that subtotal for each violation beyond the first. Print the penalty rounded down.

Type 2 - Arrangement Counter: Read three space-separated numbers: n (total specimens), r (specimens to arrange), and P (a prime number). Calculate how many ways to arrange r specimens from n total, then print the result modulo P. This is nPr mod P, where nPr = n!/(n-r)!.

Type 3 - Twin Prime Finder: Read a number N and find all twin prime pairs up to N. Twin primes are pairs like (3,5) or (11,13) that differ by exactly 2. Print each pair on a separate line as "p1 p2".

#### 12 - Assign Moving Crew by Building Type
Write a function assign_crew that takes building_description, unit_number and returns a formatted crew assignment message.

The function checks if "adobe" appears anywhere in the building description and assigns the appropriate moving crew type ("Specialized" if "adobe" is present, otherwise "Standard").

Parameters:
building_description (str): Description of the building
unit_number (int): The apartment unit number
Returns: Crew assignment message. Format: Unit [unit_number]: [crew_type] crew assigned

#### 11 - Family Reunion Name Tags
Write a function create_name_tag that takes first_name, last_name and returns a formatted name tag string.

The function creates a name tag for family reunion guests with proper formatting for easy identification.

Parameters:
first_name (str): The guest's first name
last_name (str): The guest's last name
Returns: A formatted name tag string. Format: Hello, my name is [LAST NAME], [first name]

```
def create_name_tag(first_name, last_name):
    return f"Hello, my name is {last_name.upper()}, {first_name.lower()}"
```

#### 10 - Mountain Trail Recommendation
Write a function recommend_trail that takes hiker_name, experience_years and returns a personalized trail recommendation message.

The function determines the appropriate trail based on hiking experience and creates a customized message for the hiker.

Conditions:
Less than 2 years experience: recommend "Beginner Trail"
2 or more years experience: recommend "Advanced Trail"

Parameters:
hiker_name (str): The hiker's name
experience_years (int): Years of hiking experience
Returns: A personalized recommendation message. Format: Hello [name]! Based on your [years] years of experience, we recommend the [trail type] for your mountain adventure.
```
def recommend_trail(hiker_name, experience_years):
    if experience_years < 2:
        trail_type = "Beginner Trail"
    else:
        trail_type = "Advanced Trail"
    
    return f"Hello {hiker_name}! Based on your {experience_years} years of experience, we recommend the {trail_type} for your mountain adventure."
```
#### 9 - Plant Growth Report Generator
Create a function named create_plant_report that receives plant_name and height as its parameters.

As a botanist in a university laboratory, you need to create a simple plant growth report for your lab records. Your task is to combine the plant's name and its current height into a formatted string.

Parameters:
plant_name (str): The name of the plant being studied.
height (int): The current height of the plant in centimeters.
The function should return a string that combines the plant name and height into a formatted report message. The message should be in the following format: "The [plant_name] plant has grown to [height] cm tall."
```
def create_plant_report(plant_name, height):
    return f"The {plant_name} plant has grown to {height} cm tall."
```

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
