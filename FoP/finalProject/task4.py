import statistics

# takes file as input and opens it
file = input('Enter filename: ')
fileopen = open(file, 'r')

#opens file
pricefile = fileopen.readlines()

#list to store the prices
list_of_prices = []

#for loop to collect prices
for price in pricefile:
    list_of_prices.append(int(price))

#returns number of listings
def num_of_listings(list):
    listings = len(list)
    return listings

# function to determine total price of all listings
def total_price(list):
    '''takes in numbers such as 0, 5, 3.0 and would return 8'''
    total = 0
    for value in list:
        total += int(value)
    return total

#function that finds median
def median_price(list):
    #new list to filter out empty values
    new_list = []
    #for loop that appedns to new_list
    for value in list:
        if type(value) == int or type(value) == float:
            new_list.append(value)
    median = statistics.median(new_list)
    return median

#function that uses median_price to find monthly host income
def median_monthly_host_income(list):
    #formula for monthly host income
    income = median_price(list) * 30
    return income

#function calls
print('Total number of listings: ' + str(num_of_listings(list_of_prices)))
print('Total daily price of listings is ' + str(int(total_price(list_of_prices))) + ' USD')
print('Median daily listing price is ' + str(int(median_price(list_of_prices))) + ' USD')
print('Median monthly host income is ' + str(int(median_monthly_host_income(list_of_prices))) + ' USD')
