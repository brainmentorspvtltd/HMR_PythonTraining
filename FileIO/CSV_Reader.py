import csv
# import pandas

# d = pandas.read_csv('data.csv')
# print(d)
with open('data.csv') as file:
    reader = csv.reader(file)

    for data in reader:
        print(data)