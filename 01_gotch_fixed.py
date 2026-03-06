def student(name, age, result = None):
    if result is None:
        result = []
    return {'name' : name, 'age' : age, 'result' : result}

def marks_add(student, marks):
    student['result'].append(marks)
    return student

if __name__ == "__main__":
    ram = student('ram', 45)
    shyam = student('shyam', 46)

    print(f"ram details: {ram}" )
    print(f"shyam details: {shyam}" )


    ram_marks = marks_add(ram, 90)
    print(f"ram details and marks: {ram_marks}" )
    shyam_marks = marks_add(shyam, 99)
    print(f"shyam details and marks: {shyam_marks}" )

    print(f"id of ram's result: {id(ram['result'])}")
    print(f"id of shyam's result: {id(shyam['result'])}")

    ram_marks = marks_add(ram, 80)
    print(f"ram details and marks: {ram_marks}" )
    shyam_marks = marks_add(shyam, 89)
    print(f"shyam details and marks: {shyam_marks}" )

    print(f"id of ram's result: {id(ram['result'])}")
    print(f"id of shyam's result: {id(shyam['result'])}")

