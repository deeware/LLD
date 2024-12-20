Assumptions :
    1. Handling at scale is out of scope. Therefore, storing data in-memory.
    2. Deal IDs provided are unique.
    3. User IDs provided are unique.
    4. The quantity of deals is a positive integer.
    5. The price of deals is a positive value.
    6. A user can claim a deal only once.
    7. Deals end at the specified end time and cannot be claimed after that.

LLD Design :
    
Models:
    User 
        - ID 
        - name
        - items_purchased 
    
    Item 
        - ID
        - name 
        - units
        - price
    
    Deal 
        - deal_id 
        - item_id 
        - discount
        - unit_limit
        - start_time
        - duration_hours
        - end_time
    
Services :
    UserService
        + create_user
        + get_user
        + purchase_item
        + get_purchased_items
        + get_purchased_deals
        + print_user
    
    ItemService
        + create_item
        + get_item
        + update_item_price
        + delete_item
        + update_units
    
    DealService
        + create_deal
        + get_deal 
        + is_valid
        + update_deal
        + delate_deal
        
Driver : 
    main 
    
        