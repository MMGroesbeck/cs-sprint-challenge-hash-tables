# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    pathtable = {}
    for file in files:
        end = file.split("/")[-1]
        if end in pathtable:
            pathtable[end].append(file)
        else:
            pathtable[end] = [file]
    result = []
    for query in queries:
        if query in pathtable:
            result.extend(pathtable[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
