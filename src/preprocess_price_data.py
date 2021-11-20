import re

# open file "../data/raw/price.csv" and remove all multiple spcaes
file = open("../data/raw/price.csv","r")
file2 = open("../data/raw/price1.csv","r")
file1 = open("../data/processed/price.csv","w")
lines = []
file1.write("Player,Price,Role\n")
for line in file:
    # remove multiple spaces in line using re
    line = re.sub(r'\s+', ' ', line)
    if line[-1] == " ":
        line = line[:-1]
    line = line.split(" ")    
    # print(line)
    player = " ".join(line[0:-2])
    price = float(line[-2])
    if "lakh" in line[-1]:
        price = price/100
    price = round(price,2)
    line = player + "," + str(price)
    lines.append(line)
roles = [role for role in file2]

# print(roles)
batsman = 0
bowler = 0
allrounder = 0

for line,role in zip(lines,roles):
    if 'Batsman' in role:
        line = line + ",Batsman\n"
        batsman += 1
    elif 'Bowler' in role:
        line = line + ",Bowler\n"
        bowler += 1
    elif 'All Rounder' in role:
        line = line + ",All Rounder\n"
        allrounder += 1
    file1.write(line)  

file.close()
file1.close()

if __name__ == "__main__":
    print("Batsman: ",batsman)
    print("Bowler: ",bowler)
    print("All Rounder: ",allrounder)
