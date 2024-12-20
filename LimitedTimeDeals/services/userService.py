'''
UserService
    + create_user
    + get_user
    + purchase_item
    + get_purchased_items
    + get_purchased_deals
    + print_user
    
'''
from ..models.user import User


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f"User '{name}' created")
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def purchase_item(self, user_id, item_id, deal_id, quantity):
       
        if quantity != 1:
            print("Error: Can only purchase one item per deal.")
            return False

        user = self.get_user(user_id)
        if user:
            if item_id in user.items_purchased:
                print(f"Deal #{deal_id} already claimed by '{user.name}'!")
                return False
            else:
                user.items_purchased[item_id] = {"deal_id": deal_id, "quantity": quantity}
                print(f"Deal #{deal_id} claimed by '{user.name}'")
                return True
        return False



    def get_purchased_items(self, user_id):
        user = self.get_user(user_id)
        if user:
            return user.items_purchased
        return None

    def get_purchased_deals(self, user_id, item_id):
        user = self.get_user(user_id)
        if user and item_id in user.items_purchased:
            return user.items_purchased[item_id]
    
        return 0

    def print_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            print(f"User {user_id}: {user.name}", end = " | ")
            for item_id, item_info in user.items_purchased.items():
                print(f"Item ID: {item_id}, Deal ID: {item_info['deal_id']}, Quantity: {item_info['quantity']}")
        else:
            print(f"User {user_id} not found")
