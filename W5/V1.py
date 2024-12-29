while True:
    input_string = input("Enter a number or 'q' to quit: ")
    if input_string == 'q':
        print("goodbye")
        break
    
    if input_string.isdigit():
        number = int(input_string)
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
