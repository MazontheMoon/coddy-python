import re

# Read inputs
username = input()
balance = input()
queue_position = input()

# Validate username (3-15 characters, letters/numbers/underscores only, can't start with a number)
username_valid = False
if len(username) >= 3 and len(username) <= 15:
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', username):
        username_valid = True

# Validate balance (must be a valid decimal number)
balance_valid = False
try:
    balance_float = float(balance)
    balance_valid = True
except ValueError:
    balance_valid = False

# Calculate wait time (5 minutes per customer ahead in queue)
wait_time = int(queue_position) * 5

# Print results
print("Valid" if username_valid else "Invalid")
print("Valid" if balance_valid else "Invalid")
print(wait_time)