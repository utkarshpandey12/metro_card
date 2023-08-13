


from abc import ABC, abstractmethod


class MetroStationAccount(ABC):

    @abstractmethod
    def credit_amount_to_station_account(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_stations_account_summary_data(self,*args,**kwargs):
        raise NotImplementedError