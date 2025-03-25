text = "today is my birth day"

# Checking
starts_with_today = text.startswith("Today")      # Should return True
starts_with_birthday = text.startswith("birthday")   # Should return False
starts_with_today_upper = text.startswith("today")  # Should return False (case-sensitive)

# To Print
print(f"Starts with 'Today': {starts_with_today}")          # Output: True
print(f"Starts with 'birthday': {starts_with_birthday}")      # Output: False
print(f"Starts with 'today': {starts_with_today_upper}")    # Output: False
