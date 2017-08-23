def age_in_seconds():
    user_input = input("Enter your age in seconds: ")
    seconds = int(user_input) * 365 * 24 * 60 * 60

    print("Your age in seconds is {}s").format(seconds)

def age_in_years():
    user_input = input("Enter your age in years: ")
    years = int(user_input) / 60 / 60 / 24 / 365

    print("Your age in years is {} years").format(years)



def main():
    ans = raw_input("Type y or s To calculate age in years or seconds: ")
    if ans =="y":
        age_in_seconds()
    elif ans == "s":
        age_in_years()
    else:
        print "Enter a valid option! "

if __name__ == "__main__":
    main()