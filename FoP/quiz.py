def isleapyear(year):
    value = False
    if int(year) % 4 == 0:
        value = True
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            value = True

if __name__ == '__main__':
    year = input()
    x = isleapyear(year)
    if x == True:
        print(year + ' is a leap year.')
    else:
        print(year + ' is not a leap year.')
