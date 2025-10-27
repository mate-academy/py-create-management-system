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
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> Set[str]:
    specialties: Set[str] = set()
    try:
        with open("groups.pickle", "rb") as groups_file:
            while True:
                try:
                    group: Group = pickle.load(groups_file)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return set()
    return specialties


def read_students_information() -> List[Student]:
    students: List[Student] = []
    try:
        with open("students.pickle", "rb") as students_file:
            while True:
                try:
                    student: Student = pickle.load(students_file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
