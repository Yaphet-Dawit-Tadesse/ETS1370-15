text = "tea milk coffee"

# Split text into a list
words = text.split()

print(words)  # Output: ['tea', 'milk', 'coffee']


or we can specify a custom delimiter

text = "tea,milk,coffee"

# Split using comma
words = text.split(",")

print(words)  # Output: ['tea', 'milk', 'coffee']
