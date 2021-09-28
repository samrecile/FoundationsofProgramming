# takes file as input and opens it
file = input()
fileopen = open(file, 'r')

#opens file
pricefile = fileopen.readlines()

#list to store the prices
list_of_prices = []

#for loop to collect prices
for price in pricefile:
    list_of_prices.append(price)


#variable to take total for calculations
total = 0

#for loop to add to total
for x in list_of_prices:
    total += int(x)


#finds average and displays if valid
if list_of_prices:
    average = int(total / len(list_of_prices))
    print('Average daily listing price is ' + str(average) + ' USD')
else:
    print('Prices not entered, average unavailable')
