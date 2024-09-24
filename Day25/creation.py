import pandas
import csv

data_dict = {
    "student": ["mahadev", "Akash", "Shashi"],
    "scores": [76, 56, 65],
    "usn":[1456,8901,7865]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
