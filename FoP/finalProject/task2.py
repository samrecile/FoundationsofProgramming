def total_price(list):
    '''takes in numbers such as 0, 5, 3.0 and would return 8'''
    total = 0
    for x in list:
        total += int(x)
    return total


lists = [5, 2, 1, 7.0]
x = total_price(lists)
print(x)
