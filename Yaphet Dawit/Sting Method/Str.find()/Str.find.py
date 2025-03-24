
YY = "I don't have a pc"

# Finding the index 
index_pc = YY.find("pc")    # Should return 15
index_have = YY.find("have")  # Should return 8
index_not_found = YY.find("toshiba") # Should return -1

# If we want to print 
print(f"Index of 'pc': {index_pc}")      # Output: 15
print(f"Index of 'have': {index_have}")     # Output: 8
print(f"Index of 'toshiba: {index_not_found}") # Output: -1
