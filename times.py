# Time and Date
import time
t = time.strftime("%Z\n%H:%M:%S %p\n%j Days\n%D %h\n%A %B")
print(t)

hour = int(time.strftime("%H"))
if(hour>4 and hour<=12):
    print("Good Morning Raju !")
elif(hour>12 and hour<=16):
    print("Good Afternoon Raju !")
if(hour>16 and hour<=19):
    print("Good Evening !")
else:
    (hour>19 and hour<=4)
    print("Good Night Raju !")
