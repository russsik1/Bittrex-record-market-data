# Bittrex-record-market-data
Use this script to record market data from Bittrex to db

Use this script on your web server to collect bittrex.com market data to db.

Bittrex.com API is very simple to use. This script use method "https://bittrex.com/api/v1.1/public/getmarketsummaries", which allow to get last, high, low, bid, ask price, volume, base valume, timestamp information for all markets on exchange. By default the data is recorded per minute.If table of market does not exist in db, there is method that creates new market table in db. It doesn't matter what db you use, however using postgresql (psycopg2) could let you read and write data at the same time.

Don't forget to change db configurations on your own. If it's hard for you use sqlite3, its very comfortable to keep all data in single file.

Have a good trade.
