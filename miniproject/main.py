import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"])
countGray = 0
countBlack = 0
countCinnamon = 0

data_list = data["Primary Fur Color"].to_list()
print(data_list)
for item in data_list:
    if item == "Gray":
        countGray += 1
    elif item == "Black":
        countBlack += 1
    else:
        countCinnamon += 1

data_dict = {
    "Colours": ["Gray", "Black", "Cinnamon"],
    "Counts": [countGray, countBlack, countCinnamon],

}
data_update = pandas.DataFrame(data_dict)

data_update.to_csv("sqirrel_count.csv")
