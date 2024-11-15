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
    
def buildGroups(students, groupCount):
    groupSize = len(students)//groupCount
    results = []
    while (len(students)) > 0:
        counter = 0
        results.append([])
        for i in range(groupSize):
            randomNumber = random.randint(0,(len(students)-1))
            results[counter].append(students[randomNumber])
            students.pop(randomNumber)

        counter += 1
    return results


def main():
    rawStudentNames = input("please enter all student names, separate names with a comma\n")
    students = rawStudentNames.split(",")
    groupCount = inputInt("please enter the desired number of groups, students will be evenly divided among the given groups ")
    results = buildGroups(students, groupCount)
    print("groups: ")
    for i in range (len(results)):
        print("group ", (i+1), "\n", results[i],"\n")

if __name__ == "__main__":
    main()
