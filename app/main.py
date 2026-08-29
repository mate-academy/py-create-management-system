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
    """
    Writes inputted information about the Lyceum groups
    to the file 'groups.pickle'. Returns the max number
    of students among all groups.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    """
    Writes student information to 'students.pickle'.
    Returns the total number of students.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    """
    Reads data from 'groups.pickle' and returns a list
    of unique specialty names.
    """
    try:
        with open("groups.pickle", "rb") as f:
            groups: list[Group] = pickle.load(f)

        specialties = {group.specialty.name for group in groups}
        return list(specialties)
    except (FileNotFoundError, EOFError):
        return []


def read_students_information() -> list[Student]:
    """
    Reads data from 'students.pickle' and returns
    a list of Student instances.
    """
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []
