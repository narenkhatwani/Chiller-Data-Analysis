import csv
reader = csv.reader(open("sample.csv"))
reader1 = csv.reader(open("sample1.csv"))
f = open("combined.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()