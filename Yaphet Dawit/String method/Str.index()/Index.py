D = "It's beautiful morning"

# Finding the index of a substring
index_beautiful = D.index("beautiful")    # Should return 4
index_morning = D.index("morning")   # Should return 14
index_not_found = D.index("today")     # Raises ValueError 

# To Print the results
print(f"Index of 'beautiful': {index_beautiful}")    # Output: 4
print(f"Index of 'morning: {index_morning}")   # Output: 14

