import statistics

#first input
price = input('Please enter listing price:')

#list to store the prices
list_of_prices = []

#while loop to collect prices until 'quit'
while price != 'quit':
    list_of_prices.append(int(price))
    price = input('Please enter listing price')


#finds median and displays if valid
if list_of_prices:
    median = statistics.median(list_of_prices)
    print('Median daily listing price is ' + str(int(median)) + ' USD')
else:
    print('Prices not entered, median unavailable')
