'''
Item 
    - ID
    - name 
    - units
    - price
'''

class Item:
    _next_item_id = 1

    def __init__(self, name, units, price):
        self._id = Item._next_item_id
        Item._next_item_id += 1
        self._name = name
        self._units = units
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def units(self):
        return self._units

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"Item {self._id}: {self._name}, Units: {self._units}, Price: {self._price}"

        