import dataclasses
from datetime import datetime
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    maximal_students = 0

    for group in groups:
        if len(group.students) > maximal_students:
            maximal_students = len(group.students)

    with open("groups.pickle", "wb") as pickle_groups:
        pickle.dump(groups, pickle_groups)

    return maximal_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        pickle.dump(students, pickle_students)

    return len(students)


def read_groups_information() -> set:
    all_specialties = []

    with open("groups.pickle", "rb") as pickle_groups:
        groups = pickle.load(pickle_groups)

        for group in groups:
            all_specialties.append(group.specialty.name)

    return set(all_specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_students:
        all_students = pickle.load(pickle_students)

    return all_students
