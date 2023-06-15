import openpyxl

workbookName = 'disclaimer.topstocktipsAA.xlsx'
workbook = openpyxl.load_workbook(workbookName)
worksheet = workbook['Sheet1']
link = "https://www.secretstockalerts.com/$"
link2 = 'https://www.disclaimer.topstocktips.com/$'


async def populate_worksheet():
    stuckInLoop = True
    while(stuckInLoop):
        enterNewLink = input("Do you want to enter a new link? (Y/N):")
        if(enterNewLink.ToLower() == 'y'):
            ##TODO: create logic for true loop

            loop2 = True
            while(loop2):
                enterTwoOrThreeLetters = input("Would you like 2 letters (AA-ZZ) or 3 letters (AAA-ZZZ)? (2/3):")
                if(enterTwoOrThreeLetters == '2'):
                    ##do something

                    populateExcelLinksAA(worksheet)

                    loop2 = False
                elif(enterTwoOrThreeLetters == '3'):
                    ##do something
                    loop2 = False
                else:
                    print("Your answer is not recognized. Please enter 2 for AA-ZZ and 3 for AAA-ZZZ: ")
                    enterTwoOrThreeLetters = input("Would you like 2 letters (AA-ZZ) or 3 letters (AAA-ZZZ)? (2/3):")

            stuckInLoop = False
        elif(enterNewLink.ToLower() == 'n'):
            ##TODO: create logic for false loop
            stuckInLoop = False
        else:
            print("Your answer is not recognized. Please enter Y for yes and N for no: ")
            enterNewLink = input("Do you want to enter a new link? (Y/N):")



## might need to change this to a variable
#def save_worksheet(workbook):
#    workbook.save('Links.xlsx')





def populateExcelLinksAA(worksheet, link):
    link = 'https://www.disclaimer.topstocktips.com/$'
    index = 2
    for i in range(ord('A'), ord('Z')+1):
        for j in range(ord('A'), ord('Z')+1):
                sequence = (chr(i) + chr(j))
                sequenceLower = sequence.lower()
                new_link = link.replace('$', sequenceLower)
                worksheetIndex = 'A' + str(index)
                worksheet[worksheetIndex] = new_link
                index += 1



def populateExcelLinksAAA(worksheet, link):
    index = 2
    for i in range(ord('A'), ord('Z')+1):
        for j in range(ord('A'), ord('Z')+1):
            for k in range(ord('A'), ord('Z')+1):
                sequence = (chr(i) + chr(j) + chr(k))
                sequenceLower = sequence.lower()
                new_link = link.replace('$', sequenceLower)
                worksheetIndex = 'A' + str(index)
                worksheet[worksheetIndex] = new_link
                index += 1



print(f"workbook is: {workbook} ,worksheet is: {worksheet}, link is: {link2}")
populateExcelLinksAA(worksheet, link2)
#populateExcelLinksAAA(worksheet, link)

#populate_worksheet()
workbook.save(workbookName)