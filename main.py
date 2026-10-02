from user.password_store import store_password, view_password
from user.password_generator import generate_password
import os

while True:

    print("\n===== PASSWORD SECURITY SYSTEM =====")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = input("Enter Choice: ")

    # ================= USER PANEL =================

    if choice == "1":

        while True:

            print("\n===== USER PANEL =====")
            print("1. Password Strength Checker")
            print("2. Store Password")
            print("3. View Password")
            print("4. Password Generator")
            print("5. Back")

            user_choice = input("Enter Choice: ")

            if user_choice == "1":
                os.system("python user/password_checker.py")

            elif user_choice == "2":
                store_password()

            elif user_choice == "3":
                view_password()

            elif user_choice == "4":
                generate_password()

            elif user_choice == "5":
                break

            else:
                print("Invalid Choice")

    # ================= ADMIN PANEL =================

    elif choice == "2":

        while True:

            print("\n===== ADMIN PANEL =====")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            admin_choice = input("Enter Choice: ")

            if admin_choice == "1":
                os.system("python admin/register.py")

            elif admin_choice == "2":
                os.system("python admin/login.py")

            elif admin_choice == "3":
                break

            else:
                print("Invalid Choice")

    # ================= EXIT =================

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")