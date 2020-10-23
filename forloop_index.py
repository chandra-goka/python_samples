
if __name__ == '__main__':
    languages = ['python', 'perl', 'groovy', 'java', 'curl', 'javascript']
    for num, name in enumerate(languages):
        print( num, name)

    # index starts from 1
    for num, name in enumerate(languages, start =1):
        print( num, name)

    # count of list items
    for count, name in enumerate(languages, start=1):
        print(name)
    print(f'There were {count} items in the list')