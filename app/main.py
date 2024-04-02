from __future__ import annotations

import dataclasses
import pickle


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
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_list, file)
    student_count = [len(group.students) for group in group_list]
    return max(student_count) if student_count else 0


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student_list, file)
    return len(student_list) if student_list else 0


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialities = [group.specialty.name for group in groups]
    return set(specialities)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
