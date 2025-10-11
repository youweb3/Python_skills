# D_datetime_example.py
# Demonstrates how to use Python's built-in datetime module'

import datetime

# 1. Get current date and time
current_datetime = datetime.datetime.now()
print("Current Date & Time:", current_datetime)

# 2. Get only date and only time
print("Current Date:", current_datetime.date())
print("Current Time:", current_datetime.time())

# 3. Format date and time
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date & Time:", formatted_date)

# 4. Create a specific date
custom_date = datetime.datetime(2025, 1, 1, 12, 30, 0)
print("Custom Date:", custom_date)

# 5. Calculate difference between dates
difference = custom_date - current_datetime
print("Time left until custom date:", difference)

# 6. Add or subtract time using timedelta
added_days = current_datetime + datetime.timedelta(days=7)
print("Date after 7 days:", added_days)

subtracted_hours = current_datetime - datetime.timedelta(hours=5)
print("Date and time 5 hours ago:", subtracted_hours)