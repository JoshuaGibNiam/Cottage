def intinput(message: str, range_stop, range_start=1):
    """Forces user to enter a valid number."""
    answer = input(message)
    while True:
        try:
            answer = int(answer)
            while not answer in list(range(range_start, range_stop+1)):
                answer = input(f"Invalid input, try again: {message}: ")
            return answer
        except ValueError:
            print("Please enter a valid number.")
