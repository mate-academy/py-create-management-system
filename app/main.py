import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


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
    Writes group information to 'groups.pickle' and returns
    the maximum number of students in any group.

    Args:
        groups (List[Group]): List of Group instances.

    Returns:
        int: Maximum number of students from all groups,
        or 0 if no groups exist.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:  # Check if the groups list is empty
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    """
    Writes student information to 'students.pickle' and returns
    the number of students written.

    Args:
        students (List[Student]): List of Student instances.

    Returns:
        int: Number of students written to the file.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> Set[str]:
    """
    Reads group information from 'groups.pickle' and
    returns unique specialties' names.

    Returns:
        Set[str]: A set of unique specialty names.
    """
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return {group.specialty.name for group in groups}


def read_students_information() -> List[Student]:
    """
    Reads student information from 'students.pickle' and
    returns a list of Student instances.

    Returns:
        List[Student]: A list of Student instances.
    """
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
