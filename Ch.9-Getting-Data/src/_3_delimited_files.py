#1) "Deltimied Files" -> Many pieces of info per line // either seperated by "tab" or "comma"
            # What happens when the fields have commmas or tabs in the data??
                ## ANSWER: using the "csv" module in python

    # Ex: tab-delimted file of stock prices
            # 6/20/2014      AAPL       90.91
            # 6/20/2014      MSFT       41.68
            # 6/20/2014      FB         64.5
            # 6/19/2024      AAPL       91.86
            # 6/19/2024      MSFT       41.51
            # 6/19/2024      FB         64.34

def process(date: str, symbol: str, closing_price: float) -> None:
    # Imaginge that this function actually does something.
    assert closing_price > 0.0

# processing them with: ...
import csv
with open('tab_delimited_stock_prices.txt') as f:
    tab_reader = csv.reader(f, delimeter='\t')            # read file f, delimit between tabs
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)


#-----------------------------------------------------------------------------------------------
#2) Dealing with headers in the data
        # Option A: Skip the row w/ initial call to 'reader.next'
        #      or
        # Option B: get each row as a "dict" (w/ headers as keys) by using "csv.DictReader"

# Write a file
with open('colon_delimited_stock_prices.txt', 'w') as f:
    f.write("""date:symbol:closing_price
            6/20/2014:AAPL:90.91
            6/20/2014:MSFT:41.68
            6/20/2014:FB:64.5
            """)

with open('colon_delimited_stock_prices.txt') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    for dict_row in colon_reader:
        date = dict_row['date']
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        process(date, symbol, closing_price)


#-----------------------------------------------------------------------------------------------
#3) Even w/o headers, using the 'DictReader' by passing in keys as a "fieldnames" parameter
todays_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5 }

with open('comma_delimited_stock_prices.txt', 'w') as f:
    csv_writer = csv.writer(f, delimeter=',')
    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])

    # csv.writer will do the correct thing even if your fields have commas in them
    # Bad example:

results = [["test1", "success", "Monday"],
           ["test2", "success, kind of", "Tuesday"],
           ["test3", "failure, kind of", "Wednesday"],
           ["test4", "failure, utter", "Thursday"]]

# don't do this!
with open('bad_csv.txt', 'w') as f:
    for row in results:
        f.write(",".join(map(str, row))) # might have too many commas in it!
        f.write("\n")                    # row might have newlines as well!