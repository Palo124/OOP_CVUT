from TaskPP_usernames_Refactor import create_usernames

data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
    "active": [True, False, True, True],
}
result = create_usernames(data)
print(result)