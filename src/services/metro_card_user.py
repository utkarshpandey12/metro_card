from ..interfaces.metro_card_user import MetroCardUser


class MetroCardUserService(MetroCardUser):

    metro_cards_details = {}

    def add_new_card_user(self,card_id,initial_card_balance,user_type=None,last_travelled_from_station=None):
        self.metro_cards_details[card_id] = {'bal':int(initial_card_balance),'type':user_type,'last_travelled_from':last_travelled_from_station,'travel_count':0}
        return self.metro_cards_details

    def get_card_balance_by_card_id(self,card_id):
        return self.metro_cards_details[card_id]['bal']

    def get_card_user_details(self,card_id):
        return self.metro_cards_details[card_id]

    def deduct_money_from_card(self,card_id,amount):
        users_balance = self.get_card_balance_by_card_id(card_id=card_id)
        if users_balance>amount:
            self.metro_cards_details[card_id]['bal'] -= amount
            amount_deducted = amount
        else:
            amount_deducted = amount + int(2*(amount-users_balance)/100)
            self.metro_cards_details[card_id]['bal'] = 0

        return amount_deducted
        
    def update_card_checkin_data(self,card_id,user_type,travelling_from):
        self.metro_cards_details[card_id]['type'] = user_type
        self.metro_cards_details[card_id]['last_travelled_from'] = travelling_from
        self.metro_cards_details[card_id]['travel_count'] += 1
    

    def is_valid_return_journey(self,card_id,travelling_from):
        if self.metro_cards_details[card_id]['last_travelled_from'] is None:
            return False
        if self.metro_cards_details[card_id]['last_travelled_from'] != travelling_from and self.metro_cards_details[card_id]['travel_count'] % 2 !=0:
            return True
        else:
            return False

    def checkin_metro_card_user(self,card_id,fare_amount,travelling_from,passenger_type):
        deducted_amount_from_user = self.deduct_money_from_card(card_id=card_id,amount=fare_amount)
        self.update_card_checkin_data(card_id=card_id,user_type=passenger_type,travelling_from=travelling_from)
        return deducted_amount_from_user