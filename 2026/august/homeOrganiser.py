# Read number of room-item pairs
n = int(input())

# Build inventory dictionary
inventory = {}
for _ in range(n):
    line = input().split()
    room = line[0]
    item = line[1]
    inventory[item] = room

# Read number of queries
q = int(input())

# Answer queries
for _ in range(q):
    item = input()
    if item in inventory:
        print(inventory[item])
    else:
        print("not found")

# Read weight, activity level, and goal
weight = int(input())
activity = input()
goal = input()

# Calculate base calories
base = weight * 15

# Adjust for activity level
if activity == "sedentary":
    calories = base
elif activity == "moderate":
    calories = base * 1.20
elif activity == "active":
    calories = base * 1.40

# Adjust for goal
if goal == "lose":
    calories -= 500
elif goal == "gain":
    calories += 500

# Print calories as integer
print(int(calories))

# Read number of furniture pieces
f = int(input())

# Process each furniture piece
for _ in range(f):
    dimensions = list(map(int, input().split()))
    room_max = list(map(int, input().split()))
    
    # Clip each dimension to room maximum
    clipped = []
    for i in range(len(dimensions)):
        if dimensions[i] > room_max[i]:
            clipped.append(room_max[i])
        else:
            clipped.append(dimensions[i])
    
    # Print clipped dimensions
    print(' '.join(map(str, clipped)))