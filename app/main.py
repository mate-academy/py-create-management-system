from dataclasses import dataclass
from datetime import date
from typing import List
import pickle


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        max_students = 0
    else:
        list_students = []
        for group in groups:
            count_students = len(group.students)
            list_students.append(count_students)
        max_students = max(list_students)

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

        specialty_names = []
        for group in groups:
            specialty_names.append(group.specialty.name)
        unique_specialties = list(set(specialty_names))
    return unique_specialties


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
