import os
from ..services import dealService
from ..services.userService import UserService

def main():
    # Create a DealService
    deal_service = dealService.DealService()

    # Create a UserService
    user_service = UserService()
    
    # Read input from file
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),'inputs/input0.txt')
    with open(filename, "r") as file:
        for line in file:
            command = line.strip().split()

            if command[0] == "CREATE_DEAL":
                deal_id = int(command[1])
                item_id = int(command[2])
                discount = int(command[3])
                unit_limit = int(command[4])
                start_time = command[5]+' '+command[6]
                duration_hours = int(command[7])
                deal_service.create_deal(deal_id, item_id, discount, unit_limit, start_time, duration_hours)

            elif command[0] == "CREATE_USER":
                user_id = int(command[1])
                name = command[2]
                user_service.create_user(name)

            elif command[0] == "PURCHASE_ITEM":
                user_id = int(command[1])
                item_id = int(command[2])
                deal_id = int(command[3])
                units = int(command[4])
                if deal_service.is_valid_deal(deal_id):
                    user_service.purchase_item(user_id, item_id, deal_id, units)

            elif command[0] == "PRINT_USER":
                user_id = int(command[1])
                user = user_service.get_user(user_id)
                if user:
                    user_service.print_user(user_id)
                else:
                    print("User not found")
                    

            else:
                print("Invalid command")


if __name__ == "__main__":
    main()
