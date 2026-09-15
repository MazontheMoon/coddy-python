# Read the sentence from the guest list
sentence = input()

# Read all ticket prices (we don't know how many there will be)
prices = []
try:
    while True:
        price = input()
        prices.append(float(price))
except EOFError:
    pass

# Count words that start with a vowel
words = sentence.split()
vowels = "aeiouAEIOU"
vowel_count = 0

for word in words:
    if word and word[0] in vowels:
        vowel_count += 1

# Calculate sum of last two prices
sum_last_two = prices[-2] + prices[-1]

# Print results
print(vowel_count)
print(sum_last_two)