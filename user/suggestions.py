def show_suggestions(password, has_upper, has_lower, has_digit, has_special):

    print("\nSuggestions:")

    if len(password) < 8:
        print("- Increase password length to at least 8 characters.")

    if not has_upper:
        print("- Add at least one uppercase letter.")

    if not has_lower:
        print("- Add at least one lowercase letter.")

    if not has_digit:
        print("- Add at least one number.")

    if not has_special:
        print("- Add at least one special character.")

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("- Excellent! Your password follows all the rules.")