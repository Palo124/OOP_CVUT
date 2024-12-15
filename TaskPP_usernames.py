def create_usernames(data):

    students = data["students"]
    activeCounterTrue = 0

    for i in range(len(data["active"])):
        if (data["active"][i]) == True:
            activeCounterTrue += 1

    UsernameStored = [None] * len(data["students"])

    for i in range(len(students)):
        Name, Surename = students[i].split()
        username = (Surename[:5]+Name[:3]).lower()
        if (data["active"][i]) == True:
            UsernameStored[i] = username

    firstNumber = len(UsernameStored)

    duplicateCounter = [1] * len(UsernameStored)

    for i in range(firstNumber):
        for j in range(len(UsernameStored)):
            if UsernameStored[i] == UsernameStored[j] and j != i:
                duplicateCounter[i] = duplicateCounter[i] + 1
                UsernameStored[j] = f'{UsernameStored[j][:7]}{duplicateCounter[i]}'

    usernames = [None] * activeCounterTrue
    final_students = [None] * activeCounterTrue
    final_active = [None] * activeCounterTrue

    index = 0

    for i in range(len(UsernameStored)):
        if UsernameStored[i] != None:
            final_students[index] = students[i]
            final_active[index] = True
            usernames[index] = UsernameStored[i]
            index += 1

    print(final_students)
    print(usernames)
    print(final_active)

    transformed_data = {
        "students": final_students,
        "active": final_active,
        "usernames": usernames
    }
    
    return transformed_data

#testing
data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
    "active":[True, False, True, True]
} 

# The assert to check if the function works as expected
assert create_usernames(data) == {
    "students":["Adam Levine", "John Deere", "John Deere"],
    "active":[True, True, True],
    "usernames":["levinada", "deerejoh", "deerejo2"]
}
