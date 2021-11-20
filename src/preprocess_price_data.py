import re

# open file "../data/raw/price.csv" and remove all multiple spcaes
file = open("../data/raw/price.csv","r")
file1 = open("../data/raw/price1.csv","w")
lines = []
for line in file:
    # remove multiple spaces in line using re
    line = re.sub(r'\s+', ' ', line)
    if line[-1] == " ":
        line = line[:-1]
    line = line.split(" ")    
    print(line)
    player = " ".join(line[0:-2])
    price = " ".join(line[-2:])
    line = player + "," + price + "\n"
    file1.write(line)

file.close()
file1.close()
