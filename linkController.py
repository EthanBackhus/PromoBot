import os
import ast


def openLinks():
    with open('linkList.txt', 'r') as file:
        listLinks = file.readlines()

    ## Remove the extensions from the filenames
    websiteList = [os.path.splitext(x)[0] for x in listLinks] 
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



openLinks()