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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    result = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            result.append(len(group.students))
    if result:
        return max(result)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)

def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        for group in groups:
            result.append(group.specialty.name)
    return list(set(result))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
