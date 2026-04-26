# Infinite loop
while True:
    user_input = input("Enter something (type 'exit' to stop): ")

    # Check if user wants to exit
    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    # Otherwise, print the input
    print("You entered:", user_input)