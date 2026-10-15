from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    if not groups:
        return 0

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                group = pickle.load(file)
                specialty_names.add(group.specialty.name)
    except EOFError:
        pass
    return list(specialty_names)


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                student = pickle.load(file)
                students.append(student)
    except EOFError:
        pass
    return students
