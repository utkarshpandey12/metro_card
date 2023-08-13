# Pre-requisites
* Python 3.x
* Pip

# Introductions
* This repository contains solutions to the geektrust metrocard problem
* Read more about the problem statement and requirements at https://www.geektrust.com/challenge/metro-card

# How to run the code

```
cd metro_card
python3 -m venv env ( create virtual environment ) (Unix/MacOs) or py -m venv env (Windows)
source env/bin/activate (activate virtual environment) (Unix/MacOs) or .\env\Scripts\activate (Windows)
```

 # Running the code for first input sample txt file
```
python3 -m geektrust sample_input/input1.txt
```

#  Running the code for second input sample txt file
```
python3 -m geektrust sample_input/input2.txt
```

#  Run your own test cases
Edit the input1/input2.txt file with your sample test cases 
and run using above commands depending on sample input txt file chosen


# How to execute the unit tests
```
cd tests
python3 -m test_metro_card_user 
python3 -m test_metro_station_accounts
```

Alternatively you can add these two commands in run.sh (Unix/MacOs) or run.bat (Windows) and execute it.

# run.sh/run.bat content for executing test cases
```
pip install -r requirements.txt
cd tests
python3 -m test_metro_station_account
python3 -m test_metro_card_user
```


# execute run.sh/run.bat using
```
bash run.sh (Unix/MacOs)
```


# Help

You can refer our help documents [here](https://help.geektrust.com)
You can read build instructions [here](https://github.com/geektrust/coding-problem-artefacts/tree/master/Python)
Reach Out to me @ email - u13051995p@gmail.com