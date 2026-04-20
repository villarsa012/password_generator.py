import random
import string

# =========================
# PASSWORD GENERATOR
# =========================

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def menu():
    print("\n===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter password length (or 0 to exit): "))

            if length == 0:
                print("Goodbye!")
                break

            if length < 4:
                print("Use at least 4 characters for security.\n")
                continue

            password = generate_password(length)
            print(f"\nGenerated Password: {password}\n")

        except ValueError:
            print("Please enter a valid number.\n")


# RUN PROGRAM
menu()