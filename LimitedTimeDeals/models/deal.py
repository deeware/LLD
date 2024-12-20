'''
Deal 
    - deal_id 
    - item_id 
    - discount
    - unit_limit
    - start_time
    - duration_hours
    - end_time
'''
import datetime

class Deal:
    def __init__(self, deal_id, item_id, discount, unit_limit, start_time, duration_hours):
        self.deal_id = deal_id
        self.item_id = item_id
        self.discount = discount
        self.unit_limit = unit_limit
        self.start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        self.duration_hours = duration_hours
        self.end_time = self.calculate_end_time()

    def calculate_end_time(self):
        end_time = self.start_time + datetime.timedelta(hours=self.duration_hours)
        return end_time

    def is_active(self):
        import datetime
        current_time = datetime.datetime.now()
        return self.start_time <= current_time <= self.end_time


    def has_units_available(self, units_requested):
        return units_requested <= self.unit_limit

    def __str__(self):
        return f"Deal {self.deal_id}: Item {self.item_id}, Discount {self.discount}%, Unit Limit {self.unit_limit}, Start Time {self.start_time}, End Time {self.end_time}"
