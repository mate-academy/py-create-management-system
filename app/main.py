import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        result = pickle.load(groups_file)
    return {
        group.specialty.name
        for group in result
    }


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_file:
        result = pickle.load(students_file)
        print(type(result))
    return result
