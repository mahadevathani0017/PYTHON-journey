import random

names = ['Mahadev', 'Sagar', 'Rahul', 'Suresh', 'Deepa', 'Shashi', 'Kartik', 'Nikhil']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
# loop through dict

passed_student = {student: score for (student, score) in student_scores.items() if score <= 60}
print(passed_student)
