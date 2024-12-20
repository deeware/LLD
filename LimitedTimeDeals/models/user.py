'''
User 
    - ID 
    - name
    - items_purchased 
'''

class User:
    _next_id = 1

    def __init__(self, name):
        self._id = User._next_id
        User._next_id += 1
        self._name = name
        self._items_purchased = {}  # stores key:value :: itemID:[dealID]

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def items_purchased(self):
        return self._items_purchased

    def __str__(self):
        return f"User {self._id}: {self._name}"

        
        