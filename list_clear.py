if __name__ == '__main__':
    fruits = ['Apple','Banana','Gua','Pineapple','Mango']

    # Before clearing the list
    print(fruits)

    #Method 1
    fruits.clear()
    # After clearing the list
    print(fruits)

    #Method 2
    del fruits[:]
    # After clearing the list
    print(fruits)

    #Method 3
    fruits *=0
    # After clearing the list
    print(fruits)

