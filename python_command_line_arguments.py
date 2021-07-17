import sys

def summation():
    sum_cla = 0
    # loop over all command line arguments
    for i in sys.argv[1:]:
        sum_cla = sum_cla + int(i)
    # printing the results
    print("No. of command line arguments are: ",len(sys.argv[1:]))
    print("Sum of command line arguments is:",sum_cla)
    return

if __name__ == "__main__":
    summation()
