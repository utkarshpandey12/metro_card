import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 



from src.services.metro_card_user import MetroCardUserService
import unittest

class TestMetroCardUserService(unittest.TestCase):

    CurrentTestCaseResult = None

    def setUp(self):
        self.metro_card_user_service = MetroCardUserService()
        # Add a card user initially for testing test data
        self.metro_card_users = self.metro_card_user_service.add_new_card_user(card_id=2,initial_card_balance=100)
    
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

    def test_add_new_card_user(self):
        self.assertDictEqual(self.metro_card_users[2],{'bal':100,'type':None,'last_travelled_from':None,'travel_count':0})

    def test_get_card_balance_by_card_id(self):
        self.assertEqual(self.metro_card_users[2]['bal'],self.metro_card_user_service.get_card_balance_by_card_id(card_id=2))

    def test_deduct_money_from_card(self):
        initial_balance = self.metro_card_users[2]['bal']
        self.metro_card_user_service.deduct_money_from_card(card_id=2,amount=50)
        self.assertLess(self.metro_card_user_service.get_card_balance_by_card_id(card_id=2),initial_balance)

    def test_checkin_metro_card_user(self):
        self.metro_card_user_service.checkin_metro_card_user(card_id=2,fare_amount=50,travelling_from='AIRPORT',passenger_type='ADULT')
        self.assertIsNotNone(self.metro_card_users[2]['last_travelled_from'])
        self.assertGreater(self.metro_card_users[2]['travel_count'],0)

    

    
    
        
if __name__=='__main__':
	unittest.main()

