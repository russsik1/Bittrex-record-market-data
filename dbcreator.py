import requests
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tables_DB():

    d = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries').json()['result']
	
    with psycopg2.connect(dbname='dbname', user='username', host='localhost', password='password') as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        c = conn.cursor()
        c.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        table_names = [x[0].upper() for x in c.fetchall()]
        for market in d:
            if market['MarketName'].replace('-', '_') not in table_names:
                c.execute('CREATE TABLE ' + market['MarketName'].replace('-', '_') +
                          ' (id serial primary key,'
                          'bid numeric,'
                          'ask numeric,'
                          'last numeric,'
                          'high numeric,'
                          'low numeric,'
                          'volume numeric,'
                          'basevolume numeric,'
                          'timestamp numeric,'
                          'timerecord integer);')


create_tables_DB()
