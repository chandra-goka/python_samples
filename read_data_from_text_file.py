
def read_file():

    with open('D:\\work\\sample.txt', 'r') as f:
        print(f.read())

    with open('D:\\work\\sample.txt') as f:
        for line in f:
            print(line, end='')

    with open('D:\\work\\sample.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    read_file()