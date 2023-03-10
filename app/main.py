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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    number_of_students = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            number_of_students.append(len(group.students))

    return max(number_of_students, default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                specialties.add(pickle.load(file).specialty.name)
            except EOFError:
                break

    return specialties


def read_students_information() -> List[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
