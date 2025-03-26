import os


def main():
    clear_console()
    print("Hello, User.")
    user_name = str(input("What is your name?"))
    print(f"Nice to meet you, {user_name}")
    user_num = int(input("Pick a number!  Any number: "))
    if user_num == 0:
        print("Yes, zero is technically an EVEN number, it is nothing.  Stop playing...")    
    elif user_num % 2 == 0:
        print("You have choosen an EVEN number!")
    else:
        print("You have choosen an ODD number!")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()