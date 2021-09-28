import csv

def get_listing_type_count(filename):
    with open(filename, 'r') as csv_file:
        filedata = csv.reader(csv_file)

        next(filedata)

        listing_types = {}

        for line in filedata:
            if line[3] not in listing_types.keys():
                listing_types.update({line[3]:1})
            else:
                listing_types[line[3]] += 1
        return(dict(listing_types))
        
get_listing_type_count('nola.csv')
