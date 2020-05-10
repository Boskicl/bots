import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import getpass


class Stock:
    def __init__(self,url):
        self.url        = url
        self.database   = 'stock'

    def sqlsend(self,user,password):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database = self.database,
                                         user = user,
                                         password = password)
            mySql_insert_query = """INSERT INTO stock(stock_name,time,price) 
                           VALUES('teslatoo','9:12:10','2150') """

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into stock table")
            cursor.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into stock table {}".format(error))
        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")

    def sqlquery(self,user,password):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database = self.database,
                                         user = user,
                                         password = password)

            sql_select_Query = "select * from stock"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Total number of rows in stock is: ", cursor.rowcount)

            print("\nPrinting each stock record")
            for row in records:
                print("stock_name = ", row[0], )
                print("time = ", row[1])
                print("price  = ", row[2])

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")

    def priceTrack(self):
        url = self.url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #print(soup.prettify())
        price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span')
        return price
    
   #def 
if __name__ == '__main__':

    usr = str(input('What is your SQL username? (case sensitive): '))
    paswrd = getpass.getpass(prompt='What is your SQL password (case sensitive): ', stream=None)
    stock = Stock('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch')
    #stock.sqlsend(usr,paswrd)
    stock.sqlquery(usr,paswrd)
    quit()

    #i = 0
    #p = stock.priceTrack()
    #data = {}
    #while i < 5:
    #    data['price'] = p.text
    #    #data.append(p.text)
    #    i += 1
    #with open('out.json', "w") as writeJ:
    #    json.dump(data,writeJ)
    #stock = Stock('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch')
    #p = stock.priceTrack()
    #print(p)