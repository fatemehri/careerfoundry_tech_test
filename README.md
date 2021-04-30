## Description of my design decision:
```
Source file: I collected and saved all information about the BTC price variation for the year 2020.

Database: I choose PostgreSQL database for storing the data. My reason for this selection was if it is necessary to collect 
data from tables in the future, we will make relation between them, as well as this, PostgerSQL has many advantages to working 
with JSON format. I created two tables, `btc_price` and `daily_price_volatility`. The `btc_price` table includes all data related 
to BTC price variation and `daily_price_volatility` table includes processed data. 

Process: For processing, I separated all the prices related to one certain day and I calculated price volatility with std function 
from NumPy python library. With all data in `daily_price_volatility` table we realize the daily price volatility in year 2020.
```

## Structure of project folders:
```
    Deliverable1
    ├── btc_price_variation.py
    ├── cf.json
    ├── README.md
    └── requirements.txt
    
    Deliverable2
    └── proposal.pdf
 ```

## Installation packages:
```
pip install -r Deliverable1/requirements.txt
Or
pip3 install -r Deliverable1/requirements.txt
```

## Run the project:
```
Linux: python3 Deliverable1/btc_price_variation.py
Windows: python Deliverable1/btc_price_variation.py
```
