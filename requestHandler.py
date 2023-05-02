import requests


def send_request():
    url = "https://www.disclaimer.topstocktips.com/cr"
    secretUrl = "https://www.secretstockalerts.com/at"
    response = requests.get(url)

    if response.status_code == 200:
        print("200")
    elif response.status_code == 404:
        print("404")
    else:
        print("Unsuccessful")
    #print(response.content)



#populateExcelLinksAA(worksheet, link)
#populateExcelLinksAAA(worksheet, link)

#populate_worksheet()
send_request()