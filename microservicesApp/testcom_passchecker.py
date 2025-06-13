with open("commonpassword.txt", "r") as f:
    password = f.read().splitlines()

user_input = input('please enter your password: ')

if user_input in password:
    print("your password is common")
else:
    print("your password is not common")
