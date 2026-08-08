import dataclasses

import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(group_info: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for student in group_info:
            pickle.dump(student, pickle_file)

    if group_info:
        max_students = max(len(group.students) for group in group_info)
    else:
        max_students = 0

    return max_students


def write_students_information(student_info: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_info:
            pickle.dump(student, pickle_file)

    return len(student_info)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                groups = pickle.load(file)
                specialties.add(groups.specialty.name)
            except EOFError:
                break
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
    return students
