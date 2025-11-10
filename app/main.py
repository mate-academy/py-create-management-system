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


def write_groups_information(groups: List[Group]) -> int:
    """
    Write list of groups to 'groups.pickle' and
    return max number of students.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max(
        (len(group.students) for group in groups),
        default=0,
    )
    return max_students


def write_students_information(students: List[Student]) -> int:
    """
    Write list of students to 'students.pickle'
    and return number of students.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> List[str]:
    """Read groups and return unique specialty names."""
    with open("groups.pickle", "rb") as file:
        groups: List[Group] = pickle.load(file)

    specialties = {
        group.specialty.name
        for group in groups
    }
    return list(specialties)


def read_students_information() -> List[Student]:
    """Read students from file and return list of Student instances."""
    with open("students.pickle", "rb") as file:
        students: List[Student] = pickle.load(file)
    return students
