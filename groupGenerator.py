import random 

def inputInt(prompt):
    success = False
    while (not success):
        groupCount = input(prompt)
        try:
            groupCount = int(groupCount)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return groupCount
    
def buildGroupsByGroupCount(students, groupCount):
    groupSize = len(students)//groupCount
    results = []
    for i in range(groupCount):
        results.append([])
    groupNumber = 0
    while (len(students)) > 0:
        randomNumber = random.randint(0,(len(students)-1))
        results[groupNumber].append(students[randomNumber])
        students.pop(randomNumber)
        if groupNumber == groupCount-1:
            groupNumber = 0
        else:
            groupNumber += 1
        
    return results


def main():
    rawStudentNames = input("please enter all student names, separate names with a comma\n")
    students = rawStudentNames.split(",")
    groupCount = inputInt("please enter the desired number of groups, students will be evenly divided among the given groups ")
    results = buildGroupsByGroupCount(students, groupCount)
    print("groups: ")
    for i in range (len(results)):
        print("group ", (i+1), "\n", results[i],"\n")

if __name__ == "__main__":
    main()
