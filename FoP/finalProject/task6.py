import statistics
import csv

# takes file as input and opens it
file = input('Enter filename: ')


#returns number of listings
def num_of_listings(filename):
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        # skips first line
        next(filedata)

        # total to keep track of how many listings
        total = 0

        #for loop to iterate through and increment total
        for line in filedata:
            total +=1
        return total


# function to determine total price of all listings
def total_price(filename):
    '''takes in numbers such as 0, 5, 3.0 and would return 8'''
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        # skips first line
        next(filedata)

        #total to add price values to
        total = 0

        # for loop to append values
        for line in filedata:
            total += int(float(line[13]))
        return total

#function that finds median of csv file
def median_price(filename):
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        # skips first line
        next(filedata)

        #new list to append price values to
        list = []

        # for loop to append values
        for line in filedata:
            list.append(int(float(line[13])))

        median = statistics.median(list)
        return median

# from task 5 iterates over a csv file and creates a dictionary
def get_listing_type_count(filename):
    #opens file
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        #skips first line of headings
        next(filedata)
        # initializes dictionary
        listing_types = {}

        # iterates through filedata and adds key to listing_types
        for line in filedata:
            if line[3] not in listing_types.keys():
                listing_types.update({line[3]:1})
            # if key already in listing_types adds 1 to value
            else:
                listing_types[line[3]] += 1
        return(dict(listing_types))

#creates dictionary with file content
roomtypes = get_listing_type_count(file)
# integer number of each type of room
shared_rooms = int(roomtypes['Shared room'])
entire_homes = int(roomtypes['Entire home/apt'])
private_rooms = int(roomtypes['Private room'])

#calculations for each type as a percent of total
shared_room_perc = int(shared_rooms/num_of_listings(file)*100)
entire_homes_perc = int(entire_homes/num_of_listings(file)*100)
private_rooms_perc = int(private_rooms/num_of_listings(file)*100)

print('Total number of listings: ' + str(num_of_listings(file)))
print('Total daily price of listings is ' + str(int(total_price(file))) + ' USD')
print('Median daily listing price is ' + str(int(median_price(file))) + ' USD')
print(str(shared_room_perc) + ' percent listings are Shared room')
print(str(entire_homes_perc) + ' percent listings are Entire home/apt')
print(str(private_rooms_perc) + ' percent listings are Private room')
