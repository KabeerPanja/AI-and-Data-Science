correct_password = "python"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Successful!")
        break
    else:
        print("Wrong password, try again")
