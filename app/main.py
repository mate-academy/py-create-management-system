from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import pickle


# Data Classes

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
    students: List[Student] = field(default_factory=list)


# Pickle Functions
def write_groups_information(groups: List[Group]) -> int:
    """
    Writes all inputted groups to 'groups.pickle' using pickle.
    Returns the maximum number of students in any group.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def write_students_information(students: List[Student]) -> int:
    """
    Writes all students to 'students.pickle' using pickle.
    Returns the total number of students.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[str]:
    """
    Reads groups from 'groups.pickle' and returns a list of
    specialties' names without repetition.
    """
    with open("groups.pickle", "rb") as f:
        groups: List[Group] = pickle.load(f)

    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> List[Student]:
    """
    Reads all students from 'students.pickle' and returns
    them as a list of Student instances.
    """
    with open("students.pickle", "rb") as f:
        students: List[Student] = pickle.load(f)

    return students
