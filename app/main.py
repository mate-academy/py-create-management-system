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
    course: str
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as groups_data:
        pickle.dump(groups_list, groups_data)

    for group in groups_list:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_data:
        pickle.dump(students_list, students_data)

    return len(students_list)


def read_groups_information(file_name: str = "groups.pickle") -> list[str]:
    all_specialties = list()

    with open(file_name, "rb") as groups_data:
        all_groups = pickle.load(groups_data)

    for group in all_groups:
        if group.specialty.name not in all_specialties:
            all_specialties.append(group.specialty.name)

    return all_specialties


def read_students_information(
        file_name: str = "students.pickle"
) -> list[Student]:
    with open(file_name, "rb") as students_data:
        students = pickle.load(students_data)

    return students
