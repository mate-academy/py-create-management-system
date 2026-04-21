import dataclasses
import pickle
from datetime import datetime


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
    course: int | datetime
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in group_list:
            pickle.dump(group, f)
    return max(
        len(group.students) for group in group_list
    ) if group_list else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students_list:
            pickle.dump(student, f)
    return len(students_list)


def read_groups_information() -> list[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return list(specialties)


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
