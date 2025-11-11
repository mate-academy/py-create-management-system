import dataclasses
import pickle
from datetime import datetime


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
    """Class representing a student group."""
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    """
    Write all groups information to 'groups.pickle' file.
    Returns the maximum number of students from all groups.
    """
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(students: list) -> int:
    """
    Write all students information to 'students.pickle' file.
    Returns the number of students.
    """
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    """
    Read data from 'groups.pickle' file.
    Returns all group's specialties' names without repetition.
    """
    specialties = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
            except EOFError:
                break

    return list(specialties)


def read_students_information() -> list:
    """
    Read data from 'students.pickle' file.
    Returns a list of all Student class instances.
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
