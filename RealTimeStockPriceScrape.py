"""
1. make this code run for only 10 minutes continuosly
2. make use of stockstats -> the "change" function
"""
from bs4 import BeautifulSoup
import requests
import csv
import time, threading

dataframe = []

#alert function to alert user if change if
#change in CHG crosses 2%
def AlertUserIfChange(CHG_diff,company_name):
    alert="NoAlert"

    if CHG_diff >= 2:
        alert = "%change in CHG rises 2%"
    elif CHG_diff <= -2:
        alert = "%change in CHG lowers 2%"

    #To print the alert in IDE
    if alert != "NoAlert":
        print(company_name," ",alert)
    return alert



#to store the initial %CHG
def initialCHG():

    global dataframe

    #used to exclude first row of table
    headOfTable = 1

    for item in soup.find('table',class_='tbldata14 bdrtpg').find_all('tr'):

        #used to exclude first row of the table which contains column names
        if headOfTable == 1:
            headOfTable = 0
            continue

        #print(item)
        chg = item.find_all('td')[4].text

        #appending the initial CHG values of all companies to check for
        #alert with the current CHG
        sets = []
        sets.append(chg)
        dataframe.append(sets)



#for continuous Scraping
def parseStockPrice():

    csv_file = open('StockScrape.csv','w')
    csv_writer = csv.writer(csv_file)

    #the column names of new_files
    csv_writer.writerow(['Company_Names','Industry','Last Price','Change','Initial_%CHG','Current_%CHG','%change in CHG','Mkt Cap','Alert'])


    #used to exclude first row of table
    headOfTable = 1

    dataframe_index = 0
    for item in soup.find('table',class_='tbldata14 bdrtpg').find_all('tr'):

        #used to exclude first row of the table which contains column names
        if headOfTable == 1:
            headOfTable = 0
            continue

        #print(item)
        company_name = item.find('td').a.b.text
        industry_name = item.find_all('td')[1].a.text
        last_price = item.find_all('td')[2].text
        change = item.find_all('td')[3].text
        current_chg = item.find_all('td')[4].text
        initial_chg = dataframe[dataframe_index][0]
        mkt_cap = item.find_all('td')[5].text
        dataframe_index += 1

        #difference between current CHG and initial CHG(at the start of scraping)
        CHG_diff = float(current_chg) - float(initial_chg)

        #
        alert = AlertUserIfChange(CHG_diff,company_name)

        csv_writer.writerow([company_name, industry_name, last_price, change, initial_chg, current_chg, CHG_diff,mkt_cap,alert])

    csv_file.close()



source = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9').text

soup = BeautifulSoup(source,'lxml')

#used to store initial %chg
initialCHG()

#count the no of times scraping is done
scrapeCount = 0

#used for Refresh Frequency
WAIT_TIME_SECONDS = 10
ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    parseStockPrice()
    scrapeCount += 1
    print("Scraping Count: ",scrapeCount)
