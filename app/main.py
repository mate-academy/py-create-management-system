from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List

# -----------------------------
# Dataclass Definitions
# -----------------------------


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]

# -----------------------------
# Pickle-Based Functions
# -----------------------------


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    # Return the max number of students in any group
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    # Extract unique specialty names
    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
