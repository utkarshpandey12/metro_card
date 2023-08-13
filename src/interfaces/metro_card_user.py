

from abc import ABC, abstractmethod


class MetroCardUser(ABC):

    @abstractmethod
    def add_new_card_user(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def is_valid_return_journey(self,*args,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def checkin_metro_card_user(self,*args,**kwargs):
        raise NotImplementedError

    

    