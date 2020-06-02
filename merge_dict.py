
def merge_dict(dic1, dic2):
    copy = dic1.copy()
    copy.update(dic2)
    return copy

def merge_dict2(dic1, dic2):
    return {**dic1, **dic2}

#python 2
def merge_dict3(dic1, dic2):
    return dict(dic1.items() + dic2.items())

def merge_dict4(dic1, dic2):
    return dict(list(dic1.items()) + list(dic2.items()))

if __name__ == '__main__':
    merged = merge_dict({'a': 1, 'b': 2}, {'c': 3})
    print(merged)
    merged = merge_dict2({'a': 1, 'b': 2}, {'c': 3})
    print(merged)
    # merged = merge_dict3({'a': 1, 'b': 2}, {'c': 3})
    # print(merged)
    merged = merge_dict4({'a': 1, 'b': 2}, {'c': 3})
    print(merged)
