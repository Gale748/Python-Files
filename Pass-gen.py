import string
import random

def generate_password(length):
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (16-32): "))
            if length >= 16 and length <= 32:
                break
            else:
                print("Invalid input. Length must be between 16 and 32.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    password = generate_password(length)
    print("Your new password is:", password)

if __name__ == "__main__":
    main()