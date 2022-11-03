import csv

csvRows = []
table = {}
indexToColumnName = []

# reading file
with open("lab_11_data.csv") as f:
    x = csv.reader(f)
    for row in x:
        csvRows.append(row)

# removing last 6 columns
csvRows = list(map(lambda x : x[:-6], csvRows))

# dropping rows
columns = csvRows[0]
filteredRows = list(filter(lambda x : float(x[6]) >= -3, csvRows[1:]))

# Computing averages
openHighLow = list(map(lambda x : list(map(lambda y : float(y.replace(",", "")), x[1:4])), filteredRows))
Open = list(map(lambda x : x[0], openHighLow))
High = list(map(lambda x : x[1], openHighLow))
Low = list(map(lambda x : x[2], openHighLow))
average = [str(sum(Open) / len(Open)), str(sum(High) / len(High)), str(sum(Low) / len(Low))]
    
with open("avg_output.txt", "w") as f:
    f.write("\n".join(average))

    
# (iv)
def filterStocks(c):
    filteredStocks = list(filter(lambda x : x[0][0] == c, filteredRows))
    filteredStocks = list(map(lambda x : " ".join(x), filteredStocks))
    filteredStocks = "\n".join(filteredStocks)
    with open("stock_output.txt", "w") as f:
        f.write(filteredStocks)

# (v)
filterStocks("A")