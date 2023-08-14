import pickle
import os
from typing import List
import dataclasses


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        return 0  # Return 0 when the groups list is empty

    max_students = max(len(group.students) for group in groups)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    specialties = set()
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            for group in groups:
                specialties.add(group.specialty.name)
        return list(specialties)
    else:
        return []


def read_students_information() -> List[Student]:
    if os.path.exists("students.pickle"):
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
        return students
    else:
        return []
