from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(groups: list[Group]) -> None:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_count_students = max(groups, key=lambda x: len(x.students))
    result = len(max_count_students.students)
    return result


def write_students_information(students: list[Student]) -> list[Student]:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    result_list = []

    for group in groups:
        result_list.append(group.specialty.name)

    result = list(dict.fromkeys(result_list))
    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_file = pickle.load(file)

    return students_file
