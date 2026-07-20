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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    count_of_students = 0
    for group in groups:
        if len(group.students) > count_of_students:
            count_of_students = len(group.students)
    return count_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        list_of_specialties = set()
        while True:
            try:
                group = pickle.load(f)
                list_of_specialties.add(group.specialty.name)
            except EOFError:
                break
    return list_of_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        list_of_students = []
        while True:
            try:
                list_of_students.append(pickle.load(students_file))
            except EOFError:
                break
    return list_of_students
