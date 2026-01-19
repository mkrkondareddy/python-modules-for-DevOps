import pdb

def calculate_total(prices):
    total = 0
    
    for price in prices:
        # pdb.set_trace()
        total = total + int(price)
    return total


items = [100, 200, "300", 400]

total_price = calculate_total(items)
print("Total price:", total_price)
