Name1 = input("Enter your name: ")
Password1 = input("Enter your password: ")

Name2 = "python"
Password2 = "rules"
tries = 0

while Name1 != Name2 or Password1 != Password2:
    print("Incorrect name or password. Please try again.")
    Name1 = input("Enter your name: ")
    Password1 = input("Enter your password: ")
    tries += 1
    if tries == 5:
        print("Too many failed attempts. Access denied.")
        break
else:
    print("Welcome, " + Name1 + "! You have successfully logged in.")