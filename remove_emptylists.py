if __name__ == '__main__':
    fruits_list = [[], 'apple',[], [], [], [], 'grapes', [], 'banana']
    print("Before filtering")
    print(fruits_list)
    print("After filtering")
    fruits_list = list(filter(None,fruits_list))
    print(fruits_list)

    print("After filtering with list comprehension")
    fruits_list = [fruit for fruit in fruits_list if fruit != []]
    print(fruits_list)

