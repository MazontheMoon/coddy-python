# Read the prices line and split into a list
prices = input().split()

# Read the phone number
phone = input()

# Calculate product of first two prices
first_price = int(prices[0])
second_price = int(prices[1])
product = first_price * second_price

# Print the product
print(product)

# Check if phone number is valid (XXX-XXX-XXXX format)
# Valid format: exactly 12 characters, dashes at positions 3 and 7
if len(phone) == 12 and phone[3] == '-' and phone[7] == '-':
    # Check if all other characters are digits
    parts = phone.split('-')
    if len(parts) == 3 and len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")