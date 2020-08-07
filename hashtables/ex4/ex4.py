def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hashtable = { v:i for i,v in enumerate(a)}
    result = [ num for num in a if (num > 0) and ((-1 * num) in hashtable)]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
