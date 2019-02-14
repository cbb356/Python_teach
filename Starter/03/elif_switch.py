print("""Menu:
1. File
2. View
3. Exit
""")

choice = input("Enter you choice:")

if choice == "1":
    print("You have selected 'File' menu")
elif choice == "2":
    print("You have selected 'View' menu")
elif choice == "3":
    print("Stopping")
else:
    print("Incorrect choice")
