import csv

data = [
    "Firstname,Lastname".split(","),
    "Sachin,Tendulkar".split(","),
    "Virat,Kohli".split(","),
    "MS,Dhoni".split(","),
    "Yuvraj,Singh".split(",")
]

with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)