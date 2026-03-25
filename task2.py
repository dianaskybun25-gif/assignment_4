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
    ov = []
    for student in students_list:
        current_student = student
        av = 0
        for val in current_student["scores"].values():
            if not val >= passing_score:
                break
            else:
                av = av + val
        av = av / len(current_student["scores"])
        if av != 0:
            ov.append(av)
    return ov

get_successful_students(students_math_results)

print(get_successful_students(students_math_results))