password_in = input("Input the password: ")

for i in range(2):
    if password_in == "Tues1212":
        print("Password accepted")
        break
    else:
        password_in = input("Password rejected\nTry again:")

