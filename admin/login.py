import hashlib
import os
import sys

# Parent folder ko Python path me add karega
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from user.encryption import decrypt_password

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

found = False

try:
    with open("admin/users.txt", "r") as file:

        for line in file:
            user, saved_hash = line.strip().split(",")

            if username == user and hashed_password == saved_hash:
                found = True
                break

except FileNotFoundError:
    print("No Admin Registered!")
    exit()

if found:

    print("\nLogin Successful!")

    while True:

        print("\n===== ADMIN DASHBOARD =====")
        print("1. View All Stored Passwords")
        print("2. Decrypt Password")
        print("3. Delete Password")
        print("4. Total Passwords Stored")
        print("5. Logout")

        choice = input("Enter Choice: ")

        # ================= VIEW ALL PASSWORDS =================

        if choice == "1":

            try:

                with open("user/passwords.txt", "r") as file:

                    print("\n===== STORED PASSWORDS =====")

                    for line in file:

                        website, encrypted = line.strip().split("|")

                        print("Website :", website)
                        print("Encrypted Password :", encrypted)
                        print()

            except FileNotFoundError:
                print("No Passwords Stored Yet.")

        # ================= DECRYPT PASSWORD =================

        elif choice == "2":

            website = input("Enter Website Name: ")

            try:

                found = False

                with open("user/passwords.txt", "r") as file:

                    for line in file:

                        site, encrypted = line.strip().split("|")

                        if site.lower() == website.lower():

                            print("\nWebsite :", site)
                            print("Decrypted Password :", decrypt_password(encrypted))

                            found = True
                            break

                if not found:
                    print("Website Not Found!")

            except FileNotFoundError:
                print("No Passwords Stored Yet.")

        # ================= DELETE PASSWORD =================

        elif choice == "3":

            website = input("Enter Website Name to Delete: ")

            try:

                found = False

                with open("user/passwords.txt", "r") as file:
                    lines = file.readlines()

                with open("user/passwords.txt", "w") as file:

                    for line in lines:

                        site, encrypted = line.strip().split("|")

                        if site.lower() != website.lower():
                            file.write(line)
                        else:
                            found = True

                if found:
                    print("Password Deleted Successfully!")
                else:
                    print("Website Not Found!")

            except FileNotFoundError:
                print("No Passwords Stored Yet.")

        # ================= TOTAL PASSWORDS =================

        elif choice == "4":


            try:

                with open("user/passwords.txt", "r") as file:
                    total = len(file.readlines())

                print("Total Passwords Stored :", total)

            except FileNotFoundError:
                print("Total Passwords Stored : 0")

        # ================= LOGOUT =================

        elif choice == "5":

            print("Logged Out Successfully!")
            break

        else:
            print("Invalid Choice")

else:
    print("Invalid Username or Password!")