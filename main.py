import hashlib
from termcolor import colored

print("\nWellcome to Password to Hash256!")

is_running = True
while is_running:
    try:
        option = int(input("""\nEnter the option:
            1. Encrypt password
            2. Exit
            Choose: """))

        if option == 1:
            password = input("\nEnter a password: ")
            password_utf8 = bytes(password, 'utf8')
            encoded = hashlib.sha256(password_utf8).hexdigest()

            print("\nEncrypted password: ", colored(encoded, "green"))

        elif option == 2:
            is_running = False

        else:
            print("\nThat's not a valid option...")
    except:
        print("\nThat's a number, ha!...")

print("\nThanks for trying!")
