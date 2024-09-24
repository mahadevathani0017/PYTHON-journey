import pandas

student_dict = {
    "student": ["Angela", "james", "Lily"],
    "score": [56, 76, 98]
}
student_data = pandas.DataFrame(student_dict)
print(student_data["student"])
print(type(student_data))
