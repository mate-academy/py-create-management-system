from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: datetime.year
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    else:
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            specialties = {group.specialty.name for group in groups}
            return list(specialties)
    except EOFError:
        return []


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        try:
            file_list = pickle.load(f)

            for student in file_list:
                students.append(student)
        except EOFError:
            pass
    return students
