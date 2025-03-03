def intinput(message: str, range_stop, range_start=1):

    """Forces user to enter a valid number within a specified range."""
    while True:
        try:
            answer = int(input(message))  # Get user input
            if range_start <= answer <= range_stop:
                return str(answer)  # Return the valid integer
            else:
                print(f"Invalid input, please enter a number between {range_start} and {range_stop}.")
        except ValueError:
            print("Please enter a valid number.")