import random

passwords = {}

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-"
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

def store_password():
    a = input("Do you want to generate a password? (yes/no): ")
    if a.lower() == "yes":
        password = generate_password()
    elif a.lower() == "no" :
        password = input("Enter your password :")
        if password == "":
            print("Password cannot be empty. Please try again.")
            return
        if len(password) < 12:
            print("Password must be at least 12 characters long. Please try again.")
            return
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    usecase = input("use case of the password (eg. email, social media, etc.): ")
    passwords[usecase] = password
    print(f"Password for {usecase} stored successfully.")
    with open("passwords.txt", "a") as f:
        f.write(f"\n{usecase}: {password}\n")

def retrieve_password():
    usecase = input("Enter the use case of the password you want to retrieve :")
    if usecase in passwords :
        print(f"\nPassword for {usecase}: {passwords[usecase]}")
    else:
        print("\nNo password found for this use case.")

def update_password():
    usecase = input("Enter the use case of the password you want to update :")
    if usecase in passwords :
        new_pass = input("Enter the new password :")
        passwords[usecase] = new_pass
        with open("passwords.txt", "w") as f:
            for key, value in passwords.items():
                f.write(f"{key}: {value}\n")
    else :
        print("\nNo password found for this use case.")

def delete_password():
    usecase = input("Enter the use case of the password you want to delete :")
    if usecase in passwords :
        del passwords[usecase]
        with open("passwords.txt", "w") as f:
            for key, value in passwords.items():
                f.write(f"{key}: {value}\n")
    else :
        print("\nNo password found for this use case.")

def view_passwords():
    with open("passwords.txt", "r") as f:
        content = f.read()
        if content:
            print("Stored passwords:")
            with open("passwords.txt", "r") as f:
                print(f"\n{f.read()}")
        else:
            print("\nNo passwords stored.")

def clear_all_passwords():
    passwords.clear()
    with open("passwords.txt", "w") as f:
        f.write("")
    print("\nAll passwords cleared.")

if __name__ == "__main__":
    while True:
        print("\n=====Password Manager=====")
        print("\n1. Store a password")
        print("2. Retrieve a password")
        print("3. Update a password")
        print("4. Delete a password")
        print("5. View all passwords")
        print("6. Clear all passwords")
        print("7. Exit")
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            store_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            view_passwords()
        elif choice == "6":
            clear_all_passwords()
        elif choice == "7":
            print("Exiting the program.")
            break





