import time

seconds = int(input("Enter countdown time in seconds: "))

for i in range(seconds, 0, -1):
    print(f"\rTime left: {i} sec", end="")
    time.sleep(1)

print("\nTime's up! ⏰")