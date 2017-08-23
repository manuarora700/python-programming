def age_in_seconds():
    user_input = input("Enter your age: ")
    seconds = user_input * 365 * 24 * 60 * 60

    print("Your age in seconds is {}s").format(seconds)

age_in_seconds()