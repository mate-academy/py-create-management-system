from dataclasses import dataclass
from typing import List
import pickle
import os


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    # Return the maximum number of students from all groups
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    # Return the number of students
    return len(students)


def read_groups_information() -> List[str]:
    if not os.path.exists("groups.pickle"):
        return []

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    # Return all group specialties' names without repetition
    specialties_names = {group.specialty.name for group in groups}
    return list(specialties_names)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    # Return a list of all Student class instances
    return students
