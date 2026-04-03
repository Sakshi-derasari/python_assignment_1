from data import *
def login():
    while True:
        username = input ("enter username: ").strip()

        if username =="":
            print("username canot be empty!")
            continue

        role = input("Eneter role (user/staff): ").strip().lower()
        if role not in ["user", "staff"]:
            print("Invalid role! choose 'user' or 'staff'")
            continue

        user_data = {
            "username": username,
            "role": role
        }

        users.append(user_data)

        print(f"Welcome, {username}! Role: {role}")
        return user_data
