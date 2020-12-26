def threeWayPartition(array, a, b):
    low = 0
    mid = 0
    high = len(array) - 1

    while (mid <= high):
        if (array[mid] < a):  # swap array[mid] with array[low]
            temp = array[mid]
            array[mid] = array[low]
            array[low] = temp
            low += 1
            mid += 1
        elif (array[mid] > b):
            # swap array[mid] with array[high]
            temp = array[mid]
            array[mid] = array[high]
            array[high] = temp
            high -= 1
        else:
            mid += 1
    return array


if __name__ == "__main__":
    print("Enter the array elements seperated by spaces: ")
    str_arr = input().split(' ')
    arr = [int(num) for num in str_arr]
    a, b = [int(x) for x in input("Enter the range [A,B] seperated by spaces (NOTE: A <= B) ").split()]
    arr = threeWayPartition(arr, a, b)
    print("The array after three way partitioning is ", arr)