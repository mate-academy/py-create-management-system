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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    group_number_list = [0]
    for group in groups:
        try:
            group_number_list.append(len(group.students))
        except ValueError:
            group_number_list.append(0)
    return max(group_number_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        content = pickle.load(file)
    return set(item.specialty.name for item in content)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        content = pickle.load(file)
    return content
