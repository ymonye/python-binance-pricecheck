import json
import datetime
import dateparser
from time import sleep
from binance.client import Client
import sqlite3
import pandas as pd

connection = sqlite3.connect("yonniq.db")
cursor = connection.cursor()

cursor.execute("""DROP TABLE performance;""")

sql_create_table_performance = """
CREATE TABLE performance (
coin VARCHAR(5),
roi_btc_winter VARCHAR(6),
roi_btc_spring VARCHAR(6),
roi_btc_summer VARCHAR(6),
price_btc_low_dec VARCHAR(8),
price_btc_high_jan VARCHAR(8),
price_btc_low_apr VARCHAR(8),
price_btc_high_may VARCHAR(8),
price_btc_low_aug VARCHAR(8),
price_btc_high_aug VARCHAR(8));"""

cursor.execute(sql_create_table_performance)

symbol = [
'ADA', 'ADX', 'AE', 'AGI', 'AION', 'AMB', 'APPC', 'ARDR', 'ARK', 'ARN',
'AST', 'BAT', 'BCC', 'BCD', 'BCN', 'BCPT', 'BLZ', 'BNB', 'BNT', 'BQX',
'BRD', 'BTG', 'BTS', 'CDT', 'CHAT', 'CLOAK', 'CMT', 'CND', 'CVC', 'DASH',
'DENT', 'DGD', 'DLT', 'DNT', 'DOCK', 'EDO', 'ELF', 'ENG', 'ENJ', 'EOS',
'ETC', 'ETH', 'EVX', 'FUEL', 'FUN', 'GAS', 'GNT', 'GRS', 'GTO', 'GVT',
'GXS', 'HC', 'HOT', 'ICN', 'ICX', 'INS', 'IOST', 'IOTA', 'IOTX', 'KEY',
'KMD', 'KNC', 'LEND', 'LINK', 'LOOM', 'LRC', 'LSK', 'LTC', 'LUN', 'MANA',
'MCO', 'MDA', 'MFT', 'MOD', 'MTH', 'MTL', 'NANO', 'NAS', 'NAV', 'NCASH',
'NEBL', 'NEO', 'NPXS', 'NULS', 'NXS', 'OAX', 'OMG', 'ONT', 'OST', 'PHX',
'PIVX', 'POA', 'POE', 'POLY', 'POWR', 'PPT', 'QKC', 'QLC', 'QSP', 'QTUM',
'RCN', 'RDN', 'REP', 'REQ', 'RLC', 'SALT', 'SC', 'SKY', 'SNGLS', 'SNM',
'SNT', 'STEEM', 'STORJ', 'STORM', 'STRAT', 'SUB', 'SYS', 'THETA', 'TNB',
'TNT', 'TRIG', 'TRX', 'VET', 'VIA', 'VIB', 'VIBE', 'WABI', 'WAN', 'WAVES',
'WINGS', 'WPR', 'WTC', 'XEM', 'XLM', 'XMR', 'XRP', 'XVG', 'XZC', 'YOYO',
'ZEC', 'ZEN', 'ZIL', 'ZRX'
]

client = Client("", "")
interval_1d = Client.KLINE_INTERVAL_1DAY
interval_30m = Client.KLINE_INTERVAL_30MINUTE

i = 0
while i < len(symbol):
	start_time = "2017-12-01 EST"
	end_time = "2018-01-31 EST"
	klines = client.get_historical_klines(symbol[i]+'BTC', interval_1d, start_time, end_time)

	max_01 = 0
	min_01 = 9000

	if len(klines) > 0:
                epoch_time = str(klines[0][0])[0: 10]
                first_date = (datetime.datetime.fromtimestamp(float(epoch_time)).strftime('%Y-%m-%d'))

                #if first_date == start_time[0: (len(start_time)-4)]:
                if first_date < "2018-01-01":
                        j = 0
                        while j < len(klines):
                                if (symbol[i] == 'CMT') and (float(klines[j][2]) == .0045):
                                        j += 1
                                elif (symbol[i] == 'DASH') and (float(klines[j][3]) == .000024):
                                        j += 1
                                elif (symbol[i] == 'DASH') and (float(klines[j][3]) == .030003):
                                        j += 1
                                elif (symbol[i] == 'EVX') and (float(klines[j][3]) == .00000183):
                                        j += 1
                                elif (symbol[i] == 'LTC') and (float(klines[j][3]) == .0001):
                                        j += 1
                                elif (symbol[i] == 'LTC') and (float(klines[j][3]) == .0035):
                                        j += 1
                                elif (symbol[i] == 'PPT') and (float(klines[j][2]) == .29):
                                        j += 1
                                elif (symbol[i] == 'TRIG'):
                                        j += 1
                                elif (symbol[i] == 'WABI') and (float(klines[j][2]) == .01):
                                        j += 1
                                elif (symbol[i] == 'XRP') and (float(klines[j][3]) == .00000002):
                                        j += 1
                                elif (symbol[i] == 'ZEC') and (float(klines[j][3]) == .000189):
                                        j += 1
                                else:
                                        if float(klines[j][2]) > max_01 : max_01 = float(klines[j][2])
                                        if float(klines[j][3]) < min_01 : min_01 = float(klines[j][3])
                                        j += 1

	start_time = "2018-03-01 EST"
	end_time = "2018-05-31 EST"
	klines = client.get_historical_klines(symbol[i]+'BTC', interval_1d, start_time, end_time)
	
	max_02 = 0
	min_02 = 9000

	if len(klines) > 0:
                epoch_time = str(klines[0][0])[0: 10]
                first_date = (datetime.datetime.fromtimestamp(float(epoch_time)).strftime('%Y-%m-%d'))
                
                #if first_date == start_time[0: (len(start_time)-4)]:
                if first_date < "2018-05-01":
                        j = 0
                        while j < len(klines):
                                if (symbol[i] == 'BQX') and (float(klines[j][3]) == .00000111):
                                        j += 1
                                if (symbol[i] == 'FUEL') and (float(klines[j][3]) == .00000082):
                                        j += 1
                                if (symbol[i] == 'GRS') and (float(klines[j][2]) == .00048675):
                                        j += 1
                                if (symbol[i] == 'VIA'):
                                        j += 1
                                else:
                                        if float(klines[j][2]) > max_02 : max_02 = float(klines[j][2])
                                        if float(klines[j][3]) < min_02 : min_02 = float(klines[j][3])
                                        j += 1

	start_time = "2018-08-01 EST"
	end_time = "2018-09-09 EST"
	klines = client.get_historical_klines(symbol[i]+'BTC', interval_30m, start_time)
	
	max_03 = 0
	min_03 = 9000

	if len(klines) > 0:
                j = 0
                while j < len(klines):
                        epoch_time = str(klines[j][0])[0: 10]
                        target_date = (datetime.datetime.fromtimestamp(float(epoch_time)).strftime('%Y-%m-%d %H:%M:%S'))

                        if target_date >= "2018-08-13 21:30:00":
                                if (symbol[i] == 'GRS') and (float(klines[j][2]) == .00048675):
                                        j += 1
                                if (symbol[i] == 'POLY') and (float(klines[j][3]) == .0000038):
                                        j += 1
                                else:
                                        if float(klines[j][2]) > max_03 : max_03 = float(klines[j][2])
                                        if float(klines[j][3]) < min_03 : min_03 = float(klines[j][3])
                                        j += 1
                        else: j += 1
    
	if min_01 == 9000:
		min_01 = "-"
		max_01 = "-"
		roi_01 = "-"
	else:
		roi_01 = format((max_01/min_01)-1, '.2f')
		min_01 = format(min_01, '.8f')
		max_01 = format(max_01, '.8f')
	
	if min_02 == 9000:
                min_02 = "-"
                max_02 = "-"
                roi_02 = "-"
	else:
                roi_02 = format((max_02/min_02)-1, '.2f')
                min_02 = format(min_02, '.8f')
                max_02 = format(max_02, '.8f')
	
	if min_03 == 9000:
                min_03 = "-"
                max_03 = "-"
                roi_03 = "-"
	else:
                roi_03 = format((max_03/min_03)-1, '.2f')
                min_03 = format(min_03, '.8f')
                max_03 = format(max_03, '.8f')


	table_data = [ (symbol[i], roi_01, roi_02, roi_03, min_01, max_01, min_02, max_02, min_03, max_03) ]

	for p in table_data:
		sql_command_text = """INSERT INTO performance (coin, roi_btc_winter, roi_btc_spring, roi_btc_summer,
                price_btc_low_dec,price_btc_high_jan, price_btc_low_apr, price_btc_high_may, price_btc_low_aug, price_btc_high_aug)
		VALUES ("{column_01}", "{column_02}", "{column_03}", "{column_04}", "{column_05}",
		"{column_06}", "{column_07}", "{column_08}", "{column_09}", "{column_10}");"""
				
	
	sql_command = sql_command_text.format(column_01=p[0], column_02=p[1], column_03=p[2], column_04=p[3],
	column_05=p[4], column_06=p[5], column_07=p[6], column_08=p[7], column_09=p[8], column_10=p[9])

	cursor.execute(sql_command)

	print(symbol[i] + " -  Winter ROI: " + roi_01 + "%. Spring ROI: " + roi_02 + "%. Summer ROI: " + roi_03 + "%.")
	i += 1

table = pd.read_sql_query("SELECT * from performance", connection)
table.to_csv('performance.csv', index_label='index')

connection.commit()
connection.close()
