from __future__ import annotations

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
    Save the list of groups to 'groups.pickle'.
    Return the maximum number of students among all groups (0 for empty list).
    """
    with open("groups.pickle", "wb") as file_handle:
        pickle.dump(groups, file_handle)

    return max(
        (len(group.students) for group in groups),
        default=0,
    )


def write_students_information(students: List[Student]) -> int:
    """
    Save ALL students (single list) to 'students.pickle'.
    Return the number of students.
    """
    with open("students.pickle", "wb") as file_handle:
        pickle.dump(students, file_handle)
    return len(students)


def read_groups_information() -> List[str]:
    """
    Read 'groups.pickle' and return a list of specialty names without
    duplicates, preserving the order of first appearance.
    """
    with open("groups.pickle", "rb") as file_handle:
        groups: List[Group] = pickle.load(file_handle)

    seen_names: set[str] = set()
    specialty_names: List[str] = []
    for group in groups:
        spec_name = group.specialty.name
        if spec_name not in seen_names:
            seen_names.add(spec_name)
            specialty_names.append(spec_name)
    return specialty_names


def read_students_information() -> List[Student]:
    """
    Read 'students.pickle' and return the list of Student instances.
    """
    with open("students.pickle", "rb") as file_handle:
        students: List[Student] = pickle.load(file_handle)
    return students
