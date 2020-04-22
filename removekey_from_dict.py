def remove_key(my_dict,key):
    my_dict.pop(key, None)

if __name__ == '__main__':
    fruits = {
        1:'apple',
        2:'grape',
        3:'orange'
    }
    remove_key(fruits,2)
    print(fruits)

