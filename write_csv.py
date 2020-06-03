import csv

class Items(object):

    def __init__(self, id, name, category):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__index = -1

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

if __name__ == '__main__':
    filename = 'items.csv'
    items = [Items(100, 'iPhone 10', 'Mobiles'), Items(200, 'Lenovo', 'Laptops')
        , Items(300, 'Java in Action', 'Books'), Items(400, 'Python', 'Books')]
    try:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for item in items:
                writer.writerow([item.id, item.name, item.category])
    except BaseException as e:
        print('BaseException:', filename)
    else:
        print('Data has been loaded successfully !')