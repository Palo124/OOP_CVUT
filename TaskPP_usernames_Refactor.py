def create_usernames(data: dict) -> dict:
    """
    Generates unique usernames for active students.

    Args:
        data (dict): A dictionary containing 'students' (list of names) and 'active' (list of booleans).

    Returns:
        dict: Data with 'students', 'active', and 'usernames'.
    """
    students = data["students"]
    active_flags = data["active"]

    # Count active students
    active_count = sum(active_flags)

    # Generate initial usernames based on name and surname
    def generate_username(full_name):
        first_name, last_name = full_name.split()
        return (last_name[:5] + first_name[:3]).lower()

    initial_usernames = [
        generate_username(student) if active else None
        for student, active in zip(students, active_flags)
    ]

    # Dealing with duplicates by counter
    username_counts = {}
    for i, username in enumerate(initial_usernames):
        if username is None:
            continue

        if username in username_counts:
            username_counts[username] += 1
            initial_usernames[i] = f"{username[:7]}{username_counts[username]}"
        else:
            username_counts[username] = 1

    # Filter active students and corresponding usernames
    active_students = []
    active_usernames = []
    for student, username, active in zip(students, initial_usernames, active_flags):
        if active:
            active_students.append(student)
            active_usernames.append(username)

    # Creation of transformed data
    transformed_data = {
        "students": active_students,
        "active": [True] * active_count,
        "usernames": active_usernames,
    }

    return transformed_data

# Testing
if __name__ == "__main__":
    data = {
        "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere"],
        "active": [True, False, True, True],
    }

    # Checking if the script works properly
    assert create_usernames(data) == {
        "students": ["Adam Levine", "John Deere", "John Deere"],
        "active": [True, True, True],
        "usernames": ["levinada", "deerejoh", "deerejo2"],
    }
