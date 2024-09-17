import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = time.strftime("%H")
print(timestamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)

import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Raju!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Raju!")
elif(hour>=17 and hour<0):
    print("Good Night Raju!")

# Time and Date
import time
t = time.strftime("%Z\n%H:%M:%S %p\n%j Days\n%D %h\n%A %B")
print(t)