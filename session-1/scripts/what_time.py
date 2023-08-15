# Import from the datetime module to manipulate dates and times
from datetime import datetime

# Store the current time in the `time` variable 
time = datetime.now()

# The original representation is not that pretty to the human eye
# You can uncomment the line below to check it
# print(time)

# Store the time in a specific format (hour-minute-second)
pretty_now = time.strftime("%H:%M:%S")

# Print the value of our prettyfied time
print(pretty_now)