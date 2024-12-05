from datetime import datetime
import time

def inputInt(prompt):
    success = False
    while (not success):
        num = input(prompt)
        try:
            num = int(num)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return num

def main():
    timer = inputInt("Please enter time in seconds ")
#todo change timer so it uses the seconds from date time rather than sleep
#this will make it more accurate
    usefultime = datetime.now()
    savedtime = (usefultime.second*1000000) +usefultime.microsecond
    firstRun = True
    while timer > 0:
        ct = datetime.now()
        currenttime = (ct.second*1000000)+ct.microsecond
        if firstRun:
            print(timer, end='\r')
            timer -= 1
            firstRun = False
        if currenttime >= savedtime + 1000000:
            if timer >1:
                print(timer, end='\r')
                timer -= 1
                usefultime = datetime.now()
                savedtime = (usefultime.second *1000000) + usefultime.microsecond
            else:
                print(timer)
                timer -= 1
                time.sleep(1)
        else:
            pass
        
    print("Timer has expired")

if __name__ == "__main__":
    main()
