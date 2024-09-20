import time

# Display the current time and date information
t = time.strftime("%Z\n%I:%M:%S %p\n%j Days\n%d-%m-%Y %b\n%A %B")
print(t)

# Get the current hour as an integer in 24-hour format
hour = int(time.strftime("%H"))

# Adjust the greeting based on the current time
if 4 < hour <= 12:
    print("Good Morning Raju!")
elif 12 < hour <= 15:
    print("Good Afternoon Raju!")
elif 15 < hour <= 18:
    print("Good Evening!")
elif 19 <= hour or hour <= 4:  # Night condition: either after 7 PM or before 5 AM
    print("Good Night Raju!")
