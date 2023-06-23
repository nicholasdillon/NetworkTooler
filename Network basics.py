import os

def display_kubernetes_menu():
    print("No options available for Kubernetes")

def display_menu():
    print("1. Kubernetes")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Run Python script")
    print("5. Quit")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

while True:
    display_menu()
    user_choice = get_user_choice()
    if user_choice == "1":
        while True:
            display_kubernetes_menu()
            kubernetes_choice = get_user_choice()
            if kubernetes_choice == "1":
                # Placeholder for future option
                print("Option 1 selected in Kubernetes submenu")
            elif kubernetes_choice == "2":
                # Placeholder for future option
                print("Option 2 selected in Kubernetes submenu")
            elif kubernetes_choice == "3":
                # Placeholder for future option
                print("Option 3 selected in Kubernetes submenu")
            elif kubernetes_choice == "4":
                # Placeholder for future option
                print("Option 4 selected in Kubernetes submenu")
            elif kubernetes_choice == "5":
                # Back to main menu
                break
            else:
                print("Invalid choice. Please try again.")
    elif user_choice == "2":
        # Code for option 2 goes here
        print("You selected Option 2")
    elif user_choice == "3":
        # Code for option 3 goes here
        print("You selected Option 3")
    elif user_choice == "4":
        # Run Python script
        script_path = input("Enter the path to the Python script: ")
        try:
            os.system('python3 ' + script_path)
        except Exception as e:
            print("Error executing Python script: ", e)
    elif user_choice == "5":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")
