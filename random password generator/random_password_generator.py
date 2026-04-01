import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""
    password = []
    if use_lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if use_upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        return None
    
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

def main():
    try:
        length = int(input("Enter password length:"))
        if length < 4:
            print("password length sould be at least 4.")
            return
    except ValueError:
        print("please enter a valid niumber.")
        return
    
    print("\nSelect character types (y/n):")
    use_lower = input("include lowercase letters?(y/n):").lower() =='y'
    use_upper = input("include uppercase letters?(y/n):").lower() =='y'
    use_digits = input("inculde numbers?(y/n):").lower() =='y'
    use_symbols = input("include symbols?(y/n):").lower() =='y'

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)

    if password:
        print("\nGenerated password:",password)
    else:
        print("Error:you must select at least one character type.")

if __name__ == "__main__":
    main()