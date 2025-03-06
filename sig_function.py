def intinput(message: str, range_stop, range_start=1, intstr=1):

    """Forces user to enter a valid number within a specified range.
    int str specifies the type to return: str for 1 and int for 2"""
    while True:
        try:
            answer = int(input(message))  # Get user input
            if range_start <= answer <= range_stop:
                if intstr == 1:
                    return str(answer)
                else:
                    return int(answer)# Return the valid integer
            else:
                print(f"Invalid input, please enter a number between {range_start} and {range_stop}.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    i = intinput("Please enter a number between 1 and 100?", 100,
                 intstr=1)
    print(type(i))