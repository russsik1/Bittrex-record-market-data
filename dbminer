import requests
import psycopg2
import time
import datetime
import dateutil.parser
from dbcreator import create_tables_DB


create_tables_DB()


def getData():
    while True:
		
        timerecord = round((time.time()+30)/60)*60
        while time.time() < timerecord:
            time.sleep(1)
        
        d = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').json()['result']

        with psycopg2.connect(dbname='dbname', user='username', host='localhost', password='password') as conn:
            c = conn.cursor()
            for market in d:
                timestamp = datetime.datetime.timestamp(dateutil.parser.parse(market['TimeStamp']))
                c.execute("INSERT INTO %s (bid, ask, last, high, low, volume, basevolume, timestamp, timerecord) "
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(
                              market['MarketName'].replace('-', '_').lower(), market['Bid'],
                              market['Ask'], market['Last'], market['High'], market['Low'],
                              market['Volume'], market['BaseVolume'], timestamp, timerecord))


getData()
