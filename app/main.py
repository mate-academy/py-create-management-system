import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


@dataclasses.dataclass
class Specialty:
    """Class representing a specialty."""
    name: str
    number: int


@dataclasses.dataclass
class Student:
    """Class representing a student."""
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    """Class representing a group of students."""
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    """
    Write group data to 'groups.pickle' and return the max number of students.
    """
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    """
    Write student data to 'students.pickle' and return the number of students.
    """
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> Set[str]:
    """
    Read groups from 'groups.pickle' and return unique specialty names.
    """
    specialties: Set[str] = set()
    try:
        with open("groups.pickle", "rb") as groups_file:
            while True:
                try:
                    group: Group = pickle.load(groups_file)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return specialties


def read_students_information() -> List[Student]:
    """
    Read students from 'students.pickle' and return list of Student instances.
    """
    students: List[Student] = []
    try:
        with open("students.pickle", "rb") as students_file:
            while True:
                try:
                    student: Student = pickle.load(students_file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return students
