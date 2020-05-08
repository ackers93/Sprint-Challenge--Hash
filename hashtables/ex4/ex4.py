def has_negatives(a):

    # init a dict to hold all numbers in `a`
    storage = dict()
    # init list to return matches
    matches = list()

    # iterate over each num in list
    for num in a:
        # if the num as a corresponding number in the dict.
        if storage.get(abs(num)):
            # check if their sum adds to 0
            if (storage.get(abs(num)) + num) == 0:
                # if it does, append to matches list
                matches.append(abs(num))
        else:
            # if no value is found, pass num as new key along with it's value
            storage[abs(num)] = num

    return matches


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
