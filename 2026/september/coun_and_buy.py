# Read the renovation note
note = input()

# Read the budget and price per piece
budget = int(input())
price_per_piece = int(input())

# Count words in the note
word_count = len(note.split())

# Calculate how many complete pieces can be bought
pieces = budget // price_per_piece

# Print the results
print(word_count)
print(pieces)