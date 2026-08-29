import dataclasses
import pickle
from datetime import datetime
from typing import List


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


# ------------------ Functions ------------------ #

def write_groups_information(groups: List[Group]) -> int:
    """Writes group information to groups.pickle and
    returns the maximum number of students in any group"""
    with open("groups.pickle", "wb") as outfile:
        pickle.dump(groups, outfile)

    max_students = max(
        (len(group.students) for group in groups),
        default=0
    )
    return max_students


def write_students_information(students: List[Student]) -> int:
    """Writes students information to students.pickle and
    returns the number of students"""
    with open("students.pickle", "wb") as outfile:
        pickle.dump(students, outfile)
    return len(students)


def read_groups_information() -> List[str]:
    """Reads groups.pickle and returns all specialties' names
    without repetition"""
    with open("groups.pickle", "rb") as infile:
        groups = pickle.load(infile)
    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> List[Student]:
    """Reads students.pickle and returns the list of Student
    instances"""
    with open("students.pickle", "rb") as infile:
        students = pickle.load(infile)
    return students
