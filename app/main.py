import dataclasses
import pickle
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(in_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in in_info:
            pickle.dump(group, file)
    x = [len(count.students) for count in in_info]
    return max(x) if len(x) > 0 else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    specialties = set()

    with open("groups.pickle", "rb") as file:
        try:
            while True:
                specialties.add(pickle.load(file).specialty.name)
        except EOFError:
            return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
