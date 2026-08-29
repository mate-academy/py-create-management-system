"""Module for managing student groups and their information."""
from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    """Represents a specialty with a name and number."""
    name: str
    number: int


@dataclass
class Student:
    """Represents a student with personal and academic information."""
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    """Represents a student group with specialty, course, and students."""
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    """
    Write groups information to a pickle file
        and return the largest group size.

    Args:
        groups (list[Group]):
            A list of Group objects to be written to the file.

    Returns:
        int: The size of the largest group, or 0 if there are no groups.
    """
    groups_size = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            groups_size.append(len(group.students))
            pickle.dump(group, file)
    return max(groups_size) if groups_size else 0


def write_students_information(students: list[Student]) -> int:
    """
    Write students information to a pickle file
        and return the number of students.

    Args:
        students (list[Student]):
            A list of Student objects to be written to the file.

    Returns:
        int: The number of students written to the file.
    """
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    """
    Read groups information from a pickle file
        and return list of specialty names.

    Returns:
        list[str]:
            A list of unique specialty names from all groups.
    """
    specialties_set = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties_set.add(group.specialty.name)
            except EOFError:
                break
    return list(specialties_set)


def read_students_information() -> list[Student]:
    """
    Read students information from a pickle file
        and return list of students.

    Returns:
        list[Student]: A list of Student objects read from the file.
    """
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break
    return students
