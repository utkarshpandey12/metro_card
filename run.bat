@echo off

pip install -r requirements.txt
python3 -m geektrust sample_input\input1.txt
python3 -m geektrust sample_input\input2.txt


cd tests
python3 -m test_metro_station_account
