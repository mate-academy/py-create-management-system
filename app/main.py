import dataclasses
from datetime import date
import pickle
import os


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:

    with open("groups.pickle", "wb") as group_file:
        if group_list:
            pickle.dump(group_list, group_file)
            return max([len(group.students) for group in group_list])


def write_students_information(students_list: list[Student]) -> int:

    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
        return len(students_list)


def read_groups_information() -> set:

    with open("groups.pickle", "rb") as group_file:
        if os.path.getsize("groups.pickle") == 0:
            return set()
        return set([group.specialty.name for group in pickle.load(group_file)])


def read_students_information() -> list:

    with open("students.pickle", "rb") as students_file:
        return [student for student in pickle.load(students_file)]
