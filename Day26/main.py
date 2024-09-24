# name = "Mahadev"
# new_list = [letter for letter in name]
# print(new_list)

#
# lst = [34, 56, 78]
# new_lst = [pow(item, 2) for item in lst]
# print(new_lst)

# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# range_list = [num*2 for num in range(1, 5) if num % 2 == 0]
# print(range_list)
# name = ['Mahadev', 'Sagar', 'Rahul', 'Suresh', 'Deepa', 'Shashi', 'Kartik', 'Nikhil']
# new_names = [letter for letter in name if len(letter) != 5]
# print(new_names)
names = ['Mahadev', 'Sagar', 'Rahul', 'Suresh', 'Deepa', 'Shashi', 'Kartik', 'Nikhil']
upper_names = [letter.upper() for letter in names if len(letter) <= 5]
print(upper_names)
