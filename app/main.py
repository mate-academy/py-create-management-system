from dataclasses import dataclass
from datetime import date
import pickle


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


def write_groups_information(group_list: list[Group]) -> int:
    # if len(group_list) == 0:
    #     return 0

    students_in_group = []

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(group_list, pickle_file)

    for group in group_list:
        students_in_group.append(len(group.students))

    if len(students_in_group) == 0:
        return 0

    return max(students_in_group)


def write_students_information(students_list: list[Student]) -> int:

    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        unique_groups = []
        data = pickle.load(pickle_file)
        for group in data:
            specialty_name = group.specialty.name
            if specialty_name not in unique_groups:
                unique_groups.append(specialty_name)
        return unique_groups


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
