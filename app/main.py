import dataclasses
import pickle
from datetime import datetime


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    """Write group data to a file.

    Returns the max number of students in any group.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    """Write student data to a file.

    Returns the total number of students.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    """Read groups from a file.

    Returns a list of unique specialty names.
    """
    with open("groups.pickle", "rb") as file:
        groups: list[Group] = pickle.load(file)

    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    """Read and return a list of students from a file."""
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
