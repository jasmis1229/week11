# class Bus(Vehicle):
#     def __init__(self, name, capacity, is_card_only=False):
#         super().__init__(name, capacity)
#         self.buzzer_status = False
#         self.is_card_only = is_card_only


# class PaymentError(Exception):
#     def __str__(self):
#         return 'Payment mismatch'
    
# class Passenger:
#     def __init__(self, is_cash_only=False):
#         self.is_cash_only = is_cash_only

#     def get_on(self, bus: Bus):
#         if self.is_cash_only and bus.is_card_only:
#             raise PaymentError
#         print(f'getting on {bus.name}')
class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, name, capacity, is_card_only=False):
        super().__init__(name, capacity)
        self.buzzer_status = False
        self.is_card_only = is_card_only

class PaymentError(Exception):
    def __str__(self):
        return 'Payment mismatch'
    
class Passenger:
    def __init__(self, is_cash_only=False):
        self.is_cash_only = is_cash_only

    def get_on(self, bus: Bus):
        if self.is_cash_only and bus.is_card_only:
            raise PaymentError
        print(f'getting on {bus.name}')
