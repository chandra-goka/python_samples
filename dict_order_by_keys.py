import collections
if __name__ == '__main__':
    data = {1: 'one', 3: 'three', 4: 'four', 2: 'two'}
    print("Before sort")
    print(data)
    orderd_dict = collections.OrderedDict(sorted(data.items()))
    print("After sort")
    print(orderd_dict)

    data = {'one': 1, 'three': 3, 'two': 3, 'four': 4}
    print("Before sort")
    print(data)
    orderd_dict = collections.OrderedDict(sorted(data.items()))
    print("After sort")
    print(orderd_dict)

    data = {'one': 1, 'two': 2, 'three': 3, 'two': 2}
    print("Before sort")
    print(data)
    orderd_dict = collections.OrderedDict(sorted(data.items()))
    print("After sort")
    print(orderd_dict)

    data = {'one': 1, 'three': 3, 'two': 3, 'four': 4}
    print("Before sort")
    print(data)
    orderd_dict = collections.OrderedDict(sorted(data.items(), key=lambda t: len(t[0])))
    print("After sorting by key length")
    print(orderd_dict)