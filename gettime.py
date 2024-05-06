from datetime import datetime, timedelta

# Define the timezone offset in seconds (19800 corresponds to UTC+5:30)
timezone_offset_seconds = 19800

# Get the current UTC time
utc_time = datetime.utcnow()

# Add the timezone offset to the current UTC time
current_time_with_offset = utc_time + timedelta(seconds=timezone_offset_seconds)

print("Current time with timezone offset:", current_time_with_offset)
