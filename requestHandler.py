import requests
import time
import numpy as np
import os
import certifi

#os.environ['REQUESTS_CA_BUNDLE'] = 'cacert.pem'
url1 = 'https://www.disclaimer.topstocktips.com/$'
url2 = 'https://www.secretstockalerts.com/$'

listUrls = ['https://www.disclaimer.topstocktips.com/$','https://www.secretstockalerts.com/$']




def sendRequest():
    counter = 0
    while True:
        url = "https://www.disclaimer.topstocktips.com/cr"
        secretUrl = "https://www.secretstockalerts.com/at"
        response = requests.get(url)
        time.sleep(0.01)
        counter += 1
    
        #resposne2 = requests.get(secretUrl)
        #response = requests.get(url, verify= 'c:\users\h510341\appdata\roaming\python\python310\site-packages')

        if response.status_code == 200:
            print(f'200 Counter={counter}')
        elif response.status_code == 404:
            print("404")
        else:
            print("Unsuccessful")
        #print(response.content)




async def requestHandler(request):
    if(request.status_code == 200):
        
    




#sendRequest()