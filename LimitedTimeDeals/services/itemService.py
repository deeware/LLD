'''
ItemService
    + create_item
    + get_item
    + update_item_price
    + delete_item
    + update_units
'''
from ..models.item import Item

class ItemService:
    def __init__(self):
        #store list of items
        self.items = []

    def create_item(self, name, units, price):
        item = Item(name, units, price)
        self.items.append(item)
        return item

    def get_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update_item_price(self, item, new_price):
        item.price = new_price
        return item

    def delete_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]

    def update_units(self, item_id, units_sold):
        item = self.get_item(item_id)
        if item:
            if units_sold < 0:
                raise ValueError("Units sold cannot be negative")
            if units_sold > item.units:
                raise ValueError("Insufficient units available")
            item.units -= units_sold
        
        return item
