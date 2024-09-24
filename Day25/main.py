# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "Temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
data_dict = data.to_dict()
# print(data_dict)
print(data)
temp_list = data["Temp"].to_list()
n = len(temp_list)
print(n)
print(sum(temp_list) / n)
print(data["Temp"].mode())
print(data["Temp"].max())
print(data["Temp"].min())
print(data["Temp"].median())
print(data["Temp"][1])
print(data.Temp)
print(data[data.day == 'Monday'])
print(data[data.Temp == max(data.Temp)])
print(data["Rain" == data.Condition])
monday_data = data[data.day == "Monday"]
print(((monday_data.Temp) * (9 / 5)) + 32, "F")
