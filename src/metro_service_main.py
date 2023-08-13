
class MetroService():

    """
    Metro Service class whose methods will be called in main file
    BALANCE CMD executes -> create_metro_card_user() method
    CHECK IN CMD executes -> checkin_service() method
    """

    def __init__(self,metro_card_user_service,metro_station_account_service):
        self.metro_card_user_service = metro_card_user_service
        self.metro_station_accounts_service = metro_station_account_service
        
        
    def create_metro_card_user(self,card_id,initial_card_balance):
        """
        Creates a new MetroCardUser with card_id and initial balance
        Other details set as None for the user ex- type,last_travelled_from,count_of travel
        """
        self.metro_card_user_service.add_new_card_user(card_id=card_id,initial_card_balance=initial_card_balance)
        
    def checkin_service(self,card_id,travelling_from,passenger_type):
        """
        Calculates fare, discount and updates users checkin details
        Credits amount collected and discount amount to MetroStations
        """
        (fare_amount_payable,discount_amount) = self.get_fare_by_passenger_type(passenger_type=passenger_type,is_valid_return_journey= self.metro_card_user_service.is_valid_return_journey(card_id=card_id,travelling_from=travelling_from))
        amount_deducted = self.metro_card_user_service.checkin_metro_card_user(card_id=card_id,fare_amount=fare_amount_payable,travelling_from=travelling_from,passenger_type=passenger_type)
        self.metro_station_accounts_service.credit_amount_to_station_account(station_name=travelling_from,fare_amount=amount_deducted,discount_amount=discount_amount,passenger_type=passenger_type)
        
    
    def get_stations_accounts_summary(self):
        return self.metro_station_accounts_service.get_stations_account_summary_data()
        
    
    def get_fare_by_passenger_type(self,passenger_type,is_valid_return_journey):
        """
        Return a tuple of payable amount and discount amount if applicable as per rate card and passenger type 
        """
        if not is_valid_return_journey:
            return (200,0) if passenger_type=='ADULT' else ((100,0) if passenger_type=='SENIOR_CITIZEN' else (50,0))
        else:
            return (100,100) if passenger_type=='ADULT' else ((50,50) if passenger_type=='SENIOR_CITIZEN' else (25,25))
