import csv

x = open('/home/abhay/Major Project/Datasets/kddcup.testdata.unlabeled', 'r',
         encoding='windows-1251')
i = 0
lines = list()
for l in x:
    words = l.split(",")
    lines.append(words)
    i = i+1

with open('/home/abhay/Major Project/Datasets/unlabeled.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
