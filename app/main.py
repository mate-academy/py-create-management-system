import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        max_number_of_students = 0
        for group in groups:
            if len(group.students) > max_number_of_students:
                max_number_of_students = len(group.students)

        return max_number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    result = []

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    for group in groups:
        if group.specialty.name not in result:
            result.append(group.specialty.name)

    return sorted(result)


def read_students_information() -> list[Student]:
    result = []

    with open("students.pickle", "rb") as file:
        for student in pickle.load(file):
            result.append(student)

    return result
