from user.encryption import encrypt_password, decrypt_password

file_name = "user/passwords.txt"


def store_password():

    website = input("Enter Website Name: ")
    password = input("Enter Password: ")

    encrypted = encrypt_password(password)

    with open(file_name, "a") as file:
        file.write(f"{website}|{encrypted}\n")

    print("Password Stored Successfully!")


def view_password():

    website = input("Enter Website Name: ")

    try:
        with open(file_name, "r") as file:

            found = False

            for line in file:

                site, encrypted = line.strip().split("|")

                if site.lower() == website.lower():

                    print("\nWebsite :", site)
                    print("Password:", decrypt_password(encrypted))
                    found = True
                    break

            if not found:
                print("Password Not Found.")

    except FileNotFoundError:
        print("No Passwords Stored Yet.")