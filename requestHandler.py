import requests
import time
import numpy as np
import os
import certifi

#os.environ['REQUESTS_CA_BUNDLE'] = 'cacert.pem'

#print(certifi.where)
#print(certifi.contents)
def send_request():
    url = "https://www.disclaimer.topstocktips.com/cr"
    secretUrl = "https://www.secretstockalerts.com/at"
    url2 = 'https://stackoverflow.com/questions/33148312/how-to-fake-the-object-initiation-using-fakeiteasy'
    response = requests.get(url, verify = './ca.pem')
    #response = requests.get(url, verify= 'c:\users\h510341\appdata\roaming\python\python310\site-packages')

    if response.status_code == 200:
        print("200")
    elif response.status_code == 404:
        print("404")
    else:
        print("Unsuccessful")
    #print(response.content)



send_request()