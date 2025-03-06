import time

mytime = int(input("Enter the time in Seconds:"))

for x in range(0, mytime ):
    seconds = x % 60
    minuts = int(x/60) % 60
    hour = int(x/3600)
    print(f"{hour:02}:{minuts:02}:{seconds:02}")
    time.sleep(1)

print("TIME OVER !!!!!!!!!")