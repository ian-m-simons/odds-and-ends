import time

timer = int(input("Please enter time "))

while timer > 0:
    print(timer, "\r")
    timer -= 1
    time.sleep(1)
print("Timer has expired")
