import psycopg2
import json
import datetime
import numpy as np


def calc_insert():
    try:
        # PostgreSQL Connection
        connection = psycopg2.connect(user="postgres",
                                      password="123456",
                                      host="localhost",
                                      port="5432",
                                      database="btc_price_variation")
        cursor = connection.cursor()
        # Variables
        ls_po = []  # Price Open
        ls_ph = []  # Price High
        ls_pl = []  # Price Low
        ls_pc = []  # Price Close
        datetimeFormat = '%Y-%m-%d %H:%M:%S'
        sum_min = 0

        # Read file
        with open('cf.json') as my_file:
            data = json.load(my_file)
            for fields in data:
                try:
                    # Query for inserting all data
                    postgres_insert_query = """INSERT INTO btc_price (time_period_start,time_period_end,time_open,time_close
                    ,price_open,price_high,price_low,price_close,volume_traded,trades_count)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    record_to_insert = (
                        fields['time_period_start'], fields['time_period_end'], fields['time_open'],
                        fields['time_close'], fields['price_open'], fields['price_high'],
                        fields['price_low'], fields['price_close'], fields['volume_traded'], fields['trades_count'])
                    print(record_to_insert)
                    # Insert rows
                    cursor.execute(postgres_insert_query, record_to_insert)
                    connection.commit()
                    count = cursor.rowcount
                    print(count, "Record inserted successfully into btc_price table")
                except (Exception, psycopg2.Error) as error:
                    print("Failed to insert record into btc_price table", error)
                    continue

                # Calculate and store daily price volatility
                date1 = fields['time_period_end'].replace('T', ' ').split('.')[0]
                date2 = fields['time_period_start'].replace('T', ' ').split('.')[0]
                diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2,
                                                                                                      datetimeFormat)
                ls_po.append(fields['price_open'])
                ls_ph.append(fields['price_high'])
                ls_pl.append(fields['price_low'])
                ls_pc.append(fields['price_close'])
                minutes = str(diff).split(':')[1]
                sum_min += int(minutes)
                if sum_min == 1440:
                    std_po = round(np.std(ls_po), 3)
                    std_ph = round(np.std(ls_ph), 3)
                    std_pl = round(np.std(ls_pl), 3)
                    std_pc = round(np.std(ls_pc), 3)
                    try:
                        # Query for inserting calculated data
                        postgres_insert_std = """INSERT INTO daily_price_volatility 
                        (daily_time,std_price_open,std_price_high,std_price_low,std_price_close) 
                        VALUES (%s,%s,%s,%s,%s)"""
                        record_to_insert_std = (
                        fields['time_period_start'].split('T')[0], std_po, std_ph, std_pl, std_pc)
                        print(record_to_insert_std)
                        # Insert rows
                        cursor.execute(postgres_insert_std, record_to_insert_std)
                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record inserted successfully into daily_price_volatility table")
                        # Clear variables for new daily values
                        sum_min = 0
                        ls_po.clear()
                        ls_ph.clear()
                        ls_pl.clear()
                        ls_pc.clear()
                    except (Exception, psycopg2.Error) as error:
                        print("Failed to insert record into daily_price_volatility table", error)
                        continue
    except (Exception, psycopg2.Error) as error:
        print("Connection error", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    calc_insert()
