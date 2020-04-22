def remove_key(my_dict,key):
    my_dict.pop(key,None)

def remove_key_del(my_dict,key):
    try:
       del my_dict[key]
    except KeyError:
        pass

if __name__ == '__main__':
    fruits = {
        1:'apple',
        2:'grape',
        3:'orange'
    }
    remove_key(fruits,2)
    remove_key_del(fruits,2)
    print(fruits)

