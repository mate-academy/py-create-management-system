import dataclasses
from datetime import datetime
from typing import List
import pickle


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
    """Writes all group information to 'groups.pickle' and
    returns the maximum number of students in any group.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = max(len(group.students) for group in groups) \
        if groups else 0
    return max_students


def write_students_information(students: List[Student]) -> int:
    """Writes all students information to 'students.pickle' and
    returns the total number of students.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[str]:
    """Reads groups from 'groups.pickle' and returns a list of
    specialties' names without repetition.
    """
    with open("groups.pickle", "rb") as f:
        groups: List[Group] = pickle.load(f)

    specialty_names = list({group.specialty.name for group in groups})
    return specialty_names


def read_students_information() -> List[Student]:
    """Reads students from 'students.pickle' and returns a list
    of all Student instances.
    """
    with open("students.pickle", "rb") as f:
        students: List[Student] = pickle.load(f)

    return students
