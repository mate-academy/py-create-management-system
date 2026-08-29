from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List, Set


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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    # Handle the case where groups is empty
    if not groups:
        return 0

    # Find the maximum number of students in any group
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    # Return the number of students written to the file
    return len(students)


def read_groups_information() -> Set[str]:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        # Load all group instances and collect specialty names
        groups = pickle.load(file)
        for group in groups:
            specialties.add(group.specialty.name)
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        # Load all student instances from the file
        students = pickle.load(file)
    return students
