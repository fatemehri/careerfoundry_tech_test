## Description of my design decision:
```
Source file: I collected and saved all information from the linked that you mentioned about the BTC price variation for the year 2020.

Database: I choose PostgreSQL database for storing the data. My reason for this selection was if it would be necessary to collect 
data from tables in the future, we can make relation between them. I created two tables, `btc_price` and `daily_price_volatility`. 
The `btc_price` table is for all data related to BTC price variation and `daily_price_volatility` table is for processed data. 

Process: For processing, I separated all the prices related to one certain day and
calculated price volatility with std function from NumPy python library. With all data in `daily_price_volatility` table we can find out 
The daily price volatility in `price_open`, `price_high`, `price_low` and `price_close` parameters in year 2020.
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
