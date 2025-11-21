import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups_list:
            max_students = max(max_students, len(group.students))
            pickle.dump(group, file)
    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students_list:
            pickle.dump(student, file)
    return len(students_list)


def read_groups_information() -> list:
    specialties = []
    groups = []
    read = True
    with open("groups.pickle", "rb") as file:
        try:
            while read:
                groups.append(pickle.load(file))
        except EOFError:
            read = False
    for group in groups:
        specialties.append(group.specialty.name)
    return list(set(specialties))


def read_students_information() -> list:
    students = []
    read = True
    with open("students.pickle", "rb") as file:
        try:
            while read:
                students.append(pickle.load(file))
        except EOFError:
            read = False
    return students
