import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
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
    with open("groups.pickle", "wb") as file:
        if len(groups) == 0:
            return 0
        max_students = len(groups[0].students)

        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_students:
                max_students = len(group.students)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as read_file:
        specialties = {}
        try:
            while True:
                group = pickle.load(read_file)
                specialties[group.specialty.name] = None
        except EOFError:
            pass

    return list(specialties.keys())


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as read_file:
        try:
            while True:
                students.append(pickle.load(read_file))
        except EOFError:
            pass

    return students
