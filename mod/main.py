grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    
    formatted_list = []

    for index, (name, grade) in enumerate(students.items(), start=1):
        formatted = f"{index: >4}|{name: <10}| {grade: ^5}| {grades.get(grade, 0): ^5}"
        formatted_list.append(formatted)
      

    return formatted_list
    
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)



