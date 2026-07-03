import time
price_cache = {
    "RELIANCE": 2850,
    "TCS": 3605,
    "INFY": 1490,
    "HDFCBANK": 1720
}

ticker = input("Enter stock ticker: ").upper()
start_time = time.time()
if ticker in price_cache:
    print("Latest price: ", price_cache[ticker])
else:
    print("Ticker not available.")

end_time = time.time()
print("Total Time Taken: ", end_time - start_time)