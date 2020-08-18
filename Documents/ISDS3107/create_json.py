import json

student_scores = {'name': 'Scrappy Doo', 'scores': [90, 88, 92]}
with open("scrappy_scores.json", "w") as file:
    json.dump(student_scores, file)
