import dataclasses
from datetime import datetime
import pickle


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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_list, f)
    if len(groups_list) == 0:
        return 0
    return max([len(group.students) for group in groups_list])


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups_data = pickle.load(f)
    specialities = [
        group.specialty.name for group in groups_data
    ]
    unique_list = []
    for item in specialities:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        groups_data = pickle.load(f)
    return list(groups_data)
