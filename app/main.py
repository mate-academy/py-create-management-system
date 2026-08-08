import dataclasses
import pickle
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list) -> int:
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students


def write_students_information(students: List[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return num_students


def read_groups_information() -> List[str]:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        for group in groups:
            specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
