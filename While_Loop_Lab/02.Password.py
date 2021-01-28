username = input()
correct_password = input()

while True:
    password = input()
    if password == correct_password:
        print(f"Welcome {username}!")
        break