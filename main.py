from modules import gmailSPAMMER
from modules import hotmailSPAMMER
from modules import yahooSPAMMER

def main():
    print("What email service do you want to use?")
    print("1. Gmail")
    print("2. Yahoo")
    print("3. Hotmail")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You chose Gmail")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        gmail = gmailSPAMMER.Gmail(username, password)
        to = input("To: ")
        content = input("Content: ")

        count = 0
        i = int(input("How many times do you want to send this email? "))
        while count < i:
            gmail.send(to, content)
            count += 1

        gmail.send(to, content)
        print("Email sent!")

    elif choice == 2:
        print("You chose Yahoo")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        yahoo = yahooSPAMMER.Yahoo(username, password)
        to = input("To: ")
        content = input("Content: ")

        count = 0
        i = int(input("How many times do you want to send this email? "))
        while count < i:
            yahoo.send(to, content)
            count += 1

        yahoo.send(to, content)
        print("Email sent!")

    elif choice == 3:
        print("You chose Hotmail")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        hotmail = hotmailSPAMMER.Hotmail(username, password)
        to = input("To: ")
        content = input("Content: ")

        count = 0
        i = int(input("How many times do you want to send this email? "))
        while count < i:
            hotmail.send(to, content)
            count += 1

        hotmail.send(to, content)
        print("Email sent!")

    else:
        print("Invalid choice!")

main()