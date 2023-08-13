from sys import argv
from src.metro_service_main import MetroService


def main():
    
    """
    Sample code to read inputs from the file
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    metro_service = MetroService()
    for line in Lines:
        command_string = line.split(' ')
        if 'BALANCE' in line:
            metro_service.create_metro_card_user(card_id=command_string[1],initial_card_balance=int(command_string[2]))

        elif 'CHECK_IN' in line:

            metro_service.checkin_service(card_id=command_string[1],travelling_from=command_string[3],passenger_type=command_string[2])

        elif line == 'PRINT_SUMMARY':
            data = metro_service.get_stations_accounts_summary()
            for stations,station_account_summary in data.items():
                print(f'TOTAL_COLLECTION {stations} {station_account_summary["amt_collected"]} {station_account_summary["discount_offered_amt"]}')
                print('PASSENGER_TYPE_SUMMARY')
                for items in station_account_summary['top3']:
                    print(f'{items[0]} {items[1]}')            
            

    
    
    
    
if __name__ == "__main__":
    main()