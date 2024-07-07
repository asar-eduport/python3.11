import time


def print_numbers(range_number=5):
    for i in range(1, range_number + 1):
        print(f" print at : {i}")
        time.sleep(.1)



print_numbers()