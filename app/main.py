import dataclasses
import pickle
import os
from datetime import date
from typing import List, Set


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
    max_students = 0

    try:
        with open("groups.pickle", "wb") as f:
            for group in groups:
                pickle.dump(group, f)
                max_students = max(max_students, len(group.students))
    except IOError:
        pass

    return max_students


def write_students_information(students: List[Student]) -> int:
    try:
        with open("students.pickle", "wb") as f:
            for student in students:
                pickle.dump(student, f)
    except IOError:
        pass

    return len(students)


def read_groups_information() -> Set[str]:
    specialty_names = set()

    if not os.path.exists("groups.pickle"):
        return specialty_names

    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group: Group = pickle.load(f)
                    specialty_names.add(group.specialty.name)
                except EOFError:
                    break
    except IOError:
        pass

    return specialty_names


def read_students_information() -> List[Student]:
    students: List[Student] = []

    if not os.path.exists("students.pickle"):
        return students

    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student: Student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except IOError:
        pass

    return students
