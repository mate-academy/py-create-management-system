import dataclasses
from datetime import date
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
    birth_date: date
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
    max_count = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            max_count = max(max_count, len(group.students))
    return max_count


def write_students_information(students: List[Student]) -> int:
    if students is None:
        students = []
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    specialities = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialities.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No groups.pickle")
    return list(specialities)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        try:
            students = pickle.load(f)
        except EOFError:
            students = []
    return students
