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
    Writes groups info to 'groups.pickle'
    and returns the maximum number of
    students among all groups.
    """
    with open("groups.pickle", "wb") as file_writer:
        pickle.dump(groups, file_writer)

    if not groups:
        return 0

    max_students_count = 0
    for group in groups:
        students_count = len(group.students)
        if students_count > max_students_count:
            max_students_count = students_count

    return max_students_count


def write_students_information(students: List[Student]) -> int:
    """
    Writes all students to 'students.pickle'
    and returns number of students.
    """
    with open("students.pickle", "wb") as file_writer:
        pickle.dump(students, file_writer)

    return len(students)


def read_groups_information() -> List[str]:
    """
    Reads groups from 'groups.pickle'
    and returns unique specialty names
    (without repetition).
    """
    with open("groups.pickle", "rb") as file_reader:
        groups: List[Group] = pickle.load(file_reader)

    specialty_names_set: Set[str] = set()
    for group in groups:
        specialty_names_set.add(group.specialty.name)

    return list(specialty_names_set)


def read_students_information() -> List[Student]:
    """
    Reads students from 'students.pickle'
    and returns list of Student instances.
    """
    with open("students.pickle", "rb") as file_reader:
        students: List[Student] = pickle.load(file_reader)

    return students
