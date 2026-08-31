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


groups_file_name = "groups.pickle"
students_file_name = "students.pickle"


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open(groups_file_name, "wb") as groups_file:
        pickle.dump(list_of_groups, groups_file)
    if list_of_groups:
        return max(len(group.students) for group in list_of_groups)
    return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open(students_file_name, "wb") as students_file:
        pickle.dump(list_of_students, students_file)
    return len(list_of_students)


def read_groups_information() -> set[str]:
    with open(groups_file_name, "rb") as groups_file:
        groups_list = pickle.load(groups_file)
    return set(group.specialty.name for group in groups_list)


def read_students_information() -> list[Student]:
    with open(students_file_name, "rb") as students_file:
        return pickle.load(students_file)
