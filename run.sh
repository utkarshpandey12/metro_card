#!/bin/bash


pip install -r requirements.txt

python3 -m geektrust sample_input/input1.txt
python3 -m geektrust sample_input/input2.txt

# To run test cases uncomment this and run the bash script again
#cd tests
#python3 -m test_metro_card_user
#python3 -m test_metro_station_account
