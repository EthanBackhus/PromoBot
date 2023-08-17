import multiprocessing as mp
import time
import pandas as pd
import datetime
import requests

startTime = datetime.time(hour=5, minute=45)
endTime = datetime.time(hour=22, minute=0)
link = ''
listExcelSheets = ['disclaimer.topstocktipsAA.xlsx','secretstockalerts.xlsx']
dataFrameStockTips = pd.read_excel(listExcelSheets[0], sheet_name='Sheet1')
dataFrameSecretStockAlerts = pd.read_excel(listExcelSheets[1], sheet_name='Sheet1')
listKnownHits = 'listKnownHits.txt'
query = None



def search_query_process(queue):
    while True:
        response, link = perform_search_query()
        
        if response == 200:
            print("adding message to the queue")
            newStr = 'NEW PROMO ALERT!! ' + link 
            queue.put(newStr)
            
            
        time.sleep(5)
        



def perform_search_query():
    index = 0
    while True:
        if(index == 676):
            index = 0

        linkStockTips = dataFrameStockTips.iloc[index,0]
        responseStockTips = requests.get(linkStockTips)
        
        if(responseStockTips.status_code == 200):
            if(stringInFile(linkStockTips) == False):
                writeToFile(linkStockTips)
                return responseStockTips.status_code, linkStockTips
        else:
            pass

        index += 1

    
    


def writeToFile(text):
    with open(listKnownHits, 'a+') as file:
        file.seek(0)
        content = file.read()
        if text not in content:
            file.write('\n' + text)


def stringInFile(text):
    with open(listKnownHits, 'r') as file:
        content = file.read()
        if text in content:
            return True
        else:
            return False
        

def find_ticker(html_content, twoletterTicker):
    pattern = r'content='    



if __name__ == '__main__':
    # Create a multiprocessing queue
    queue = mp.Queue()

    # Start the search query process
    search_query_proc = mp.Process(target=search_query_process, args=(queue,))
    search_query_proc.start()

    search_query_proc.join()