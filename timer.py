from datetime import datetime

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
    dt = datetime.now()
    dt = dt.microsecond
    while timer > 0:
        ct = datetime.now()
        ct = ct.microsecond
        if int(ct) >= int(dt) + 1000000:
            print(timer, end='\r')
            timer -= 1
            dt = datetime.now()
            dt = dt.microsecond
        else:
            pass
        
    print("Timer has expired")

if __name__ == "__main__":
    main()
