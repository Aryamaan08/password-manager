class Password:
    def __init__(self, password):
        self.only_numbers = password.isnumeric()
        self.only_letters = password.isalpha()
        self.alphanumeric = password.isalnum()
        self.password = password
        self.length = len(password)
    
    def strength(self):
        f = open("common_passwords.txt")
        common_passwords = list(f)
        for i in range(len(common_passwords)):
            common_passwords[i] = common_passwords[i][:-1]

        if password in common_passwords:
            return "Weak"
        elif password.length <= 3:
            return "Weak"

        f.close()

        num_count = 0
        special_count = 0

        for char in password.password:
            if password.password.count(char) > 3 and password.length < 8:
                return "Weak"
            if char.isnumeric():
                num_count += 1
            elif not char.isalpha():
                special_count += 1
            
        if special_count > 1 and password.length >= 8:
            return "Strong"

        if num_count > 3 and password.length >= 8:
            return "Strong"
        
        if password.length > 13 and not password.isnumeric():
            return "Strong"
        elif password.length > 20:
            return "Strong"

        return "Weak"
    
    def improve(self):
        if self.only_letters:
            return "Add numbers and symbols!"
        elif self.only_numbers:
            return "Add letters and symbols!"
        elif self.alphanumeric:
            return "Add symbols!"
        elif self.length < 8:
            return "Make a bigger password!"
        else:
            return "This is a good password!"

if __name__ == "__main__":
    p = input("Enter password: ")
    password = Password(p)
    print(password.strength())
    print(password.improve())
