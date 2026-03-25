students_math_results = [
{"name": "Олександр", "scores": {"Calculus": 85,
"Algebra": 90, "Discrete Math": 78}},
{"name": "Марія", "scores": {"Calculus": 65, "Algebra":
55, "Discrete Math": 70}},
{"name": "Іван", "scores": {"Calculus": 92, "Algebra": 88,
"Discrete Math": 95}},
{"name": "Анна", "scores": {"Calculus": 45, "Algebra": 60,
"Discrete Math": 50}}
]


def get_successful_students(students_list, passing_score=60):
    succ_students = {}

    for student in students_list:
        s = []
        for val in student["scores"].values():
            s.append(val)
        if min(s) < passing_score:
            continue
        else:
            av = round(sum(s)/len(s), 2)
            succ_students[student["name"]] = av
    return succ_students

get_successful_students(students_math_results)

print(get_successful_students(students_math_results))