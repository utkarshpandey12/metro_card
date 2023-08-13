from ..interfaces.metro_station_account import MetroStationAccount
from collections import Counter


class MetroStationAccountsService(MetroStationAccount):
  station_account_summary = {}

  def create_station_account_summary(self,station_name):
    self.station_account_summary[station_name] = {'amt_collected':0,'discount_offered_amt':0,'SENIOR_CITIZEN':0,'ADULT':0,'KID':0}
    

  def get_station_account_summary_by_station_name(self,station_name):
    try:
      return self.station_account_summary[station_name]
    except KeyError:
      return {}

  def credit_amount_to_station_account(self,station_name,fare_amount,discount_amount,passenger_type):
    if not self.get_station_account_summary_by_station_name(station_name=station_name):
      self.create_station_account_summary(station_name=station_name)
    
    self.station_account_summary[station_name]['amt_collected'] += fare_amount
    self.station_account_summary[station_name]['discount_offered_amt'] += discount_amount
    self.station_account_summary[station_name][passenger_type] += 1

  def get_stations_account_summary_data(self):
    count_summary = {}
    for station,station_data in self.station_account_summary.items():
      for item,data in station_data.items():
        if data!=0 and item in ['SENIOR_CITIZEN','ADULT','KID']:
          count_summary[item] = data
    
      self.station_account_summary[station]['top3'] = Counter(count_summary).most_common(3)

    return self.station_account_summary


          
        
    



