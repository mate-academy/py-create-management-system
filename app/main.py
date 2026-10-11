import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


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
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> Set[str]:
    specialty_names = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group: Group = pickle.load(file)
                specialty_names.add(group.specialty.name)
            except EOFError:
                break

    return specialty_names


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student: Student = pickle.load(file)
                students.append(student)
            except EOFError:
                break

    return students
