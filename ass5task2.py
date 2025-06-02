
def slice_and_reverse():
    numbers = list(range(1, 11))

    first_five = numbers[:5]

    reversed_list = first_five[::-1]

    print("First 10 elements:", numbers)
    print("First 5 elements:", first_five)
    print("Reversed list:", reversed_list)

slice_and_reverse()
