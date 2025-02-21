import dataclasses
import pickle
# from datetime import datetime
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


def write_groups_information(groups: List[Group]) -> int:
    if not all(isinstance(group, Group) for group in groups):
        raise TypeError("All elements in groups should be of type Group")

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    if not all(isinstance(student, Student) for student in students):
        raise TypeError("All elements in students should be of type Student")

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> str:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
