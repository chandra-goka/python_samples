from operator import attrgetter
class Item():
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def __repr__(self):
        return '({},{},{})'.format(self.id,self.name,self.price)

item1 = Item(100,"Mobile",25000)
item2 = Item(200,"Books",17000)
item3 = Item(300,"Pens",12000)
item4 = Item(400,"Laptops",75000)

items = [item1,item2,item3,item4]

#Using custom method
def item_sort(item):
    return item.price
sorted_items = sorted(items,key=item_sort,reverse=True)
print(sorted_items)

#Using lambda
sorted_items2 = sorted(items,key=lambda item:item.name)
print(sorted_items2)

#Using operator module
sorted_items3 = sorted(items,key=attrgetter("id"))
print(sorted_items3)




