import time
prices = list(range(1, 100000001))
start_time = time.time()
maximum_price = max(prices)
end_time = time.time()

print("Maximum price: ", maximum_price)
print("Execution time:", end_time - start_time)