from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    num_students = [len(group.students) for group in groups]
    if len(num_students) > 0:
        return max(num_students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "b+r") as file:
        groups = pickle.load(file)
    for group in groups:
        if group.specialty.name not in result:
            result.append(group.specialty.name)
    return result


def read_students_information() -> list:
    with open("students.pickle", "b+r") as file:
        students = pickle.load(file)
    return students
