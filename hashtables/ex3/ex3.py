def intersection(arrays):

    # create dictionary to hold key(num), value(amount)
    items_count = dict()
    # init a result list t append intersections
    result = []

    # iterate over arrays list
    for i, num_list in enumerate(arrays):
        # iterate over individual lists
        for y in num_list:
            # if the item already has a count in the dict. and the index is more than 1, increase the count
            if items_count.get(y) != None and i > 0:
                items_count[y] = items_count[y] + 1
            # if theres no entry with that number in the dict. and the index is 1 (meaning were still in the first array)
            elif items_count.get(y) is None and i == 0:
                # then we set the inital count to 1
                items_count[y] = 1
            else:
                continue

    for num in items_count:
        if items_count[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
