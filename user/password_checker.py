from user.password_rules import show_rules
from user.suggestions import show_suggestions
show_rules()
# Password Strength Checker

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

# Check every character
for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

    elif ch in special_characters:
        has_special = True
        
print("\n------ Password Report ------")
print("Password Length :", len(password))
print("Uppercase       :", has_upper)
print("Lowercase       :", has_lower)
print("Number          :", has_digit)
print("Special Char    :", has_special)

score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1
show_suggestions(password, has_upper, has_lower, has_digit, has_special)
print("\nScore :", score, "/5")

if score == 5:
    print("Password Strength : STRONG")

elif score >= 3:
    print("Password Strength : MEDIUM")

else:
    print("Password Strength : WEAK")