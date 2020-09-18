import json
import random

def create_password(length=20):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ`1234567890-=[]\;',./~!@#$%^&*()_+\{\}|:\"<>?"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    return password

def get_passwords(website=None):
    f = open("passwords.json")
    passwords = json.load(f)
    f.close()
    if website == None:
        return passwords
    try:
        return passwords[website]
    except:
        return None

def save_password(website, password):
    f = open("passwords.json")
    passwords = json.load(f)
    passwords[website] = password
    f = open("passwords.json", "w")
    json.dump(passwords, f)

def determine_strength(password):
    f = open("common_passwords.txt")
    common_passwords = list(f)
    for i in range(len(common_passwords)):
        common_passwords[i] = common_passwords[i][:-1]

    if password in common_passwords:
        return "Weak"
    elif len(password) <= 3:
        return "Weak"

    f.close()

    num_count = 0
    special_count = 0

    for char in password:
        if password.count(char) > 3 and len(password) < 8:
            return "Weak"
        if char.isnumeric():
            num_count += 1
        elif not char.isalpha():
            special_count += 1
        
    if special_count > 3 and len(password) >= 8:
        return "Strong"

    if num_count > 3 and len(password) >= 8:
        return "Strong"
    
    if len(password) > 13 and not password.isnumeric():
        return "Strong"
    elif len(password) > 20:
        return "Strong"

    return "Weak"
    


while True:
    action = input("What do you want to do? G to get a password, C to create a password, S to save a password, D to determine strength of password or Q to quit. ")
    if action.upper() == "G":
        website = input("\nEnter website (optional): ")
        if website == "":
            passwords = get_passwords()
            print("\n", end="")
            for website in passwords:
                print(f"Website: {website}\nPassword: {passwords[website]}\n")
        else:
            password = get_passwords(website)
            if password == None:
                print("\nInvalid Website!")
            else:
                print(f"\nWebsite: {website}\nPassword: {password}")
    elif action.upper() == "C":
        length = input("\nEnter length (optional): ")
        if length == "":
            print(create_password())
        else:
            try:
                print(create_password(int(length)))
            except:
                print("Invalid input!")
    elif action.upper() == "S":
        website = input("\nEnter website: ")
        password = input("\nEnter password (optional): ")
        if password == "":
            save_password(website, create_password())
        else:
            save_password(website, password)
    elif action.upper() == "D":
        password = input("\nEnter password: ")
        print(determine_strength(password))
    elif action.upper() == "Q":
        break
    else:
        print("Invalid Action!")
    print("\n\n")
