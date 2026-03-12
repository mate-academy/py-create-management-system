from dataclasses import dataclass
from datetime import date
from typing import Any
import pickle


GROUPS_FILE = "groups.pickle"
STUDENTS_FILE = "students.pickle"


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def _write_pickle(filename: str, data: Any) -> None:
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def _read_pickle(filename: str) -> Any:
    with open(filename, "rb") as f:
        return pickle.load(f)


def write_groups_information(groups: list[Group]) -> int:
    with open(GROUPS_FILE, "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    if not groups:
        return 0
    return max(len(g.students) for g in groups)


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_FILE, "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()
    try:
        with open(GROUPS_FILE, "rb") as f:
            while True:
                try:
                    group: Group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return list(specialties)


def read_students_information() -> list[Student]:
    students: list[Student] = []
    try:
        with open(STUDENTS_FILE, "rb") as f:
            while True:
                try:
                    students.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return students
