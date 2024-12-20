'''
DealService
    + create_deal
    + get_deal 
    + is_valid
    + update_deal
    + delate_deal
'''

from ..models.deal import Deal
from datetime import datetime

class DealService:
    def __init__(self):
        self.deals = []

    def create_deal(self, deal_id, item_id, discount, unit_limit, start_time, duration_hours):
        deal = Deal(deal_id, item_id, discount, unit_limit, start_time, duration_hours)
        self.deals.append(deal)
        print(f"Deal #{deal_id} created")
        return deal


    def get_deal(self, deal_id):
        for deal in self.deals:
            if deal.deal_id == deal_id:
                return deal
        return None
        
    def is_valid_deal(self,deal_id):
        for deal in self.deals:
            if deal.deal_id == deal_id and deal.end_time < datetime.now():
                print("Deal Expired")
                return False
        
        return True
                
    
    def update_deal(self, deal_id, new_discount=None, new_unit_limit=None, new_start_time=None, new_end_time=None):
        deal = self.get_deal(deal_id)
        if deal:
            if new_discount:
                deal.discount = new_discount
            if new_unit_limit:
                deal.unit_limit = new_unit_limit
            if new_start_time:
                deal.start_time = new_start_time
            if new_end_time:
                deal.end_time = new_end_time
            return deal
        return None

    def delete_deal(self, deal_id):
        for deal in self.deals:
            if deal.deal_id == deal_id:
                deal.remove(deal)
        
                

    
    
        
        
        
    
    
        
    