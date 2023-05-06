import os
import ast
import asyncio

async def openExcelLinks():
    with open('excelList.txt', 'r') as file:
        listExcelLinks = file.readlines()

    ## Remove the extensions from the filenames
    websiteList = [os.path.splitext(x)[0] for x in listExcelLinks] 
    print(websiteList)  
#
    ## give control to function that will modify list
#
    ### return control and convert list back to string
#
    #linkListStr = str(linkList)
#
    #with open('linkList.txt', 'w') as file:
    #    file.write(linkListStr)



async def openLinkList():
    with open('linkList.txt', 'r') as file:
        listLinks = [line.strip() for line in file.readlines()]

    print(listLinks[0])


asyncio.run(openLinkList())