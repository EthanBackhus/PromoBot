import requests
import re
import multiprocessing as mp
import time

tradigitalLink = "https://tradigitalir.com/disclaimer-tmg/"
pattern = r'\((NASDAQ|NYSE|OTC):\s*([A-Za-z]{2,4})\)'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0", "Accept-Language": "en-US"}
queue = None

def scrapeTradigitalProces():
    while True:
        res = scrapeTradigital()
        queue.put(res)
        time.sleep(30)


def scrapeTradigital():
    pattern = r'\((NASDAQ|NYSE|OTC):\s*([A-Za-z]{2,4})\)'

    html_content = requests.get(url=tradigitalLink, headers=headers)
    matches = re.findall(pattern, html_content)

    existingWords = set()
    with open('tradigitalList.txt', 'r') as file:
        existingWords = {line.strip() for line in file}

    with open('tradigitalList.txt', 'r') as file:
        for match in matches:
            word = match[1]
            if word not in existingWords:
                file.write(word + '\n')

                # CALL THE PROMO METHOD
                return word




if __name__ == '__main__':
    # Create a multiprocessing queue
    queue = mp.Queue()

    # Start the search query process
    tradigitalProcess = mp.Process(target=scrapeTradigitalProces, args=(queue,))
    tradigitalProcess.start()
    tradigitalProcess.join()
