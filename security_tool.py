# security tools

# here you can see the username and password and how it done
password = "code12"

user = input("Username: ")
password = input("Password: ")

if user == "student" and password == password:

    choice = ""

    # this show the user the menu
    while choice != "4":

        print("\n1. Security Event Counter")
        print("2. Brute Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Enter choice: ")

# 1. security counter- this counts the correct and incorrect attemtps, an alert will happen if 50 or percent is incorrect 
        if choice == "1":

            correct = 0
            wrong = 0

            for i in range(10):
                p = input("Enter password: ")

                if p == password:
                    correct += 1
                else:
                    wrong += 1

            print("Correct:", correct)
            print("Wrong:", wrong)

            percent = wrong * 100 / 10

            print("Wrong percentage:", percent, "%")

    # this will show if you get 50% are wrong
            if percent > 50:
                print("ALERT")

#2. Brute force- this allows the user to guess the password but you have a limited amount of attemps
        elif choice == "2":

            secret = "python"
            attempts = 0
            
            # the user is allowed to have 5 attempts 
            while attempts < 5:

                guess = input("Guess password: ")
                attempts += 1

                if guess == secret:
                    print("Correct")
                    break
                else:
                    print("Wrong")

            if attempts == 5:
                print("nax attempts reached")

# 3. login authentication- This will make sure that you know the username and password and if you dont you will be frozen from the acount
        elif choice == "3":

            failed = 0

# this part allows you 3 attempts to login

            while failed < 3:

                u = input("Username: ")
                p = input("Password: ")

                if u == "student" and p == password:
                    print("Login Successful")
                    break
                else:
                    failed += 1
                    print("Login Failed")

            if failed == 3:
                print("Account frozen for 24 hours")

#4. exit the menu
        elif choice == "4":
            print("Thank you for using the security tool")

else:
    print("Invalid Login")

    
