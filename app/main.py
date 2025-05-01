from dataclasses import dataclass
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list | Student


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file_groups:
        pickle.dump(groups, pickle_file_groups)
        if groups == []:
            return 0
        else:
            return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file_students:
        pickle.dump(students, pickle_file_students)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file_groups:
        groups = pickle.load(pickle_file_groups)
        return list(set((group.specialty.name) for group in groups))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file_students:
        students = pickle.load(pickle_file_students)
        return list(student for student in students)
