def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max((len(group.students) for group in groups), default=0)

def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)

def read_groups_information() -> List[str]:
    groups = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                groups.append(pickle.load(f))
            except EOFError:
                break
    return list(set(group.specialty.name for group in groups))

def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                students.append(pickle.load(f))
            except EOFError:
                break
    return students
