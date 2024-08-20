import pickle
from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    max_students = 0

    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
            pickle.dump(group, file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    students_count = 0

    with open("students.pickle", "wb") as file:
        for student in students:
            students_count += 1
            pickle.dump(student, file)

    return students_count


def read_groups_information() -> list:
    specalities_set = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specalities_set.add(group.specialty.name)
            except EOFError:
                break

    return list(specalities_set)


def read_students_information() -> list:
    students = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
    return students
