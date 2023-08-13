import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 



from src.services.metro_station_account import MetroStationAccountsService
import unittest

        

class TestMetroStationAccountsService(unittest.TestCase):

    CurrentTestCaseResult = None

    def setUp(self):
        self.metro_station_account_service = MetroStationAccountsService()
        
    
    @classmethod
    def setResult(cls, total_test_cases, errors_test_cases, failures_test_cases, skipped_test_cases):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            total_test_cases, errors_test_cases, failures_test_cases, skipped_test_cases

    def tearDown(self):
        total_test_cases = self.CurrentTestCaseResult.testsRun
        errors_test_cases = self.CurrentTestCaseResult.errors
        failures_test_cases = self.CurrentTestCaseResult.failures
        skipped_test_cases = self.CurrentTestCaseResult.skipped
        self.setResult(total_test_cases, errors_test_cases, failures_test_cases, skipped_test_cases)

    def run(self, result=None):
        self.CurrentTestCaseResult = result 
        unittest.TestCase.run(self, result)
    
    @classmethod
    def tearDownClass(cls):
        print("\nTotal number of test cases: " + str(cls.amount))
        print("error test cases: " + str(len(cls.errors)))
        print("failure test cases: " + str(len(cls.failures)))
        print("success test cases: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
        print("skipped test cases: " + str(len(cls.skipped)))

    
    def test_create_station_account_summary(self):
        self.metro_station_account_service.create_station_account_summary(station_name='AIRPORT')
        self.assertEqual(len(self.metro_station_account_service.station_account_summary['AIRPORT']),5)

    def test_credit_amount_to_station_account(self):

        self.metro_station_account_service.credit_amount_to_station_account(station_name='AIRPORT',fare_amount=100,discount_amount=100,passenger_type='ADULT')
        self.assertGreater(self.metro_station_account_service.station_account_summary['AIRPORT']['amt_collected'],0)
        self.assertGreater(self.metro_station_account_service.station_account_summary['AIRPORT']['ADULT'],0)


    def test_get_stations_account_summary_data(self):
        
        station_account_summary = self.metro_station_account_service.get_stations_account_summary_data()
        self.assertDictEqual(station_account_summary,{'AIRPORT':{'amt_collected': 100, 'discount_offered_amt': 100, 'SENIOR_CITIZEN': 0, 'ADULT': 1, 'KID': 0, 'top3': [('ADULT', 1)]}})
        


    
    
        
if __name__=='__main__':
	unittest.main()
