#finds average price per neighborhood
import csv

filename = input()

# creates a dicionary of neighborhoods and their total prices
def neighborhood_prices_dict(filename):
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        #skips first line of headings
        next(filedata)

        # initializes dictionary to store neighborhoods and totals
        neighborhood_prices = {}

        # iterates through filedata and adds key to neighborhood_prices along with price
        for line in filedata:
            if line[7] not in neighborhood_prices.keys():
                neighborhood_prices.update({line[7]:int(float(line[13]))})
            # if key already in listing_types adds price to value
            else:
                neighborhood_prices[line[7]] += int(float(line[13]))
        return(dict(neighborhood_prices))

# creates a dicitonary of neighborhoods and their total number of rentals
def neighborhood_total_rental(filename):
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        #skips first line of headings
        next(filedata)

        #initalizes dictionary to store neighborhoods and totals
        neighborhoods = {}

        # iterates through filedata and increments neighborhoods
        for line in filedata:
            #if neighborhood not in neighborhoods adds it with 1 as value
            if line[7] not in neighborhoods.keys():
                neighborhoods.update({line[7]:1})
            else:
                neighborhoods[line[7]] += 1
        return(dict(neighborhoods))

#stores dictionary of neighborhood total prices
neighborhood_price_totals = neighborhood_prices_dict(filename)
neighborhood_rental_totals = neighborhood_total_rental(filename)

# takes the two dicitonaries created above to calculate the average price for each neighborhood
def average_hood_price(price_totals, rental_totals):
    # initializes a new dicitonary to hold the averages of all the neighborhoods
    price_totals_list = []
    rental_totals_list = []
    neighborhoods = []
    final_averages = []
    final_dict = {}
    for neighborhood in price_totals.keys():
        neighborhoods.append(neighborhood)
    for pricetotal in price_totals.values():
        price_totals_list.append(pricetotal)
    for rentaltotal in rental_totals.values():
        rental_totals_list.append(rentaltotal)
    for x in range(len(price_totals_list)):
        average =  int(price_totals_list[x])/int(rental_totals_list[x])
        final_averages.append(average)
    for value in range(len(neighborhoods)):
        final_dict[neighborhoods[value]] =  final_averages[value]

    return final_dict

x = average_hood_price(neighborhood_price_totals, neighborhood_rental_totals)
print(x)
