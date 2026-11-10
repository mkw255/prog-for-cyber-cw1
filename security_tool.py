# this is for user username and password
USERNAME = "student"
PASSWORD = "student"
GUESS_PASSWORD = "demo123"

# This tool checks user logins, counts password errors
MAX_LOGIN_ATTEMPTS = 3
MAX_GUESS_ATTEMPTS = 5
EVENT_COUNT = 10

def login():
    " return true if the user logs in within the attempt limimt"
    for attempt in range(1, MAX_LOGIN_ATTEMPTS + 1):
        entered_username = input("enter your username")
        entered_password = input("enter your password") 

        if entered_username == USERNAME and entered_password == PASSWORD:
            print("login successfull")
            return True
        
        print(f"login failed ({attempt}/{MAX_LOGIN_ATTEMPTS})")
    
    print("account frozen for 24 hours")
    return False

def count_security_event():
    " count correct and incorrect password entries"
    incorrect_count = 0
    
    for attempt in range(1,EVENT_COUNT + 1):
        entered_password = input(f"enter password ({attempt}/{EVENT_COUNT}) ")

        if entered_password != PASSWORD: 
            incorrect_count += 1
    
    correct_count = EVENT_COUNT - incorrect_count
    incorrect_percentage = incorrect_count / EVENT_COUNT * 100

    print(f"correct entires: {correct_count}")
    print(f"incorrect entires{incorrect_count}")
    print(f"Incorrect percentage: {incorrect_percentage:.0f}%")

    # an alert will only happen if more than half of the entiers are incorrect.
    if incorrect_percentage > 50:
        print("alert, more than 50% percent of your password you enterd are incorrect.")


def simulate_password_guessing():
    "let the user manually enter a dummy password "
    for attempt in range(1, MAX_GUESS_ATTEMPTS + 1):
        guess = input (f"Enter your guess ({attempt}/{MAX_GUESS_ATTEMPTS}): ")

        
        if guess == GUESS_PASSWORD:
            print(f"correct password guessed in {attempt} attempts.")
            return
        
        print("incorrect guess")

    print("max guesses reached")


def main():
    # the menu will open when you entered the correct startup login

    if not login():
        return 
    
    while True:
        print("\nSecurity Tool Menu")
        print("1- Security Event Counter")
        print("2- Brute-Force Simulation")
        print("3- Login Authentication")
        print("4- Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            count_security_event()
        elif choice == "2":
            simulate_password_guessing()
        elif choice == "3":
            login()
        elif choice == "4":
            print("Thank you for using the security tool")
            break
        else:
            print("Invalid option. Enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

    
