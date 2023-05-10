
def stringInFile(text, filename):
    with open(filename, 'r') as file:
        content = file.read()
        if text in content:
            return True
        else:
            return False




print(stringInFile('https://www.disclaimer.topstocktips.com/ce', 'listKnownHits.txt'))