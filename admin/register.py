import hashlib

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

with open("admin/users.txt", "a") as file:
    file.write(username + "," + hashed_password + "\n")

print("Registration Successful!")