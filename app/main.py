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
    average_mark: int | float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(groups_list, groups)
        for student in groups_list:
            return len(student.students)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as info_about_students:
        pickle.dump(students_list, info_about_students)
        return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_file:
        ready_to_reed = pickle.load(groups_file)
        specialty = set()
        for group in ready_to_reed:
            specialty.add(group.specialty.name)
        return specialty


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_info:
        result = pickle.load(students_info)
        return result
