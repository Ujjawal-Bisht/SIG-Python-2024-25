import csv

with open("file1.csv","w", newline="\n") as fp:
    wr = csv.writer(fp)
    wr.writerow(["S.No","Name","Age"])
    wr.writerow([1,"A",20])
    wr.writerow([2,"B",21])
    wr.writerow([3,"C",22])
    wr.writerow([4,"D",23])

with open("file1.csv","r") as fp:
    rd = csv.reader(fp)
    for row in rd:
        print(row)