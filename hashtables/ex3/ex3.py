def intersection(arrays):
    """
    YOUR CODE HERE
    """
    tables = [{ v:i for i,v in enumerate(array)} for array in arrays]
    result = []
    for num in arrays[0]:
        found = True
        for table in tables:
            if num not in table:
                found = False
        if found:
            result.append(num)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
