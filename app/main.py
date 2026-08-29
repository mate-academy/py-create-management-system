import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    students: list


def write_groups_information(groups: list) -> int:
    """
    Writes all group information to groups.pickle file.
    Returns the maximum number of students from all groups.
    """
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)

    return max_students


def write_students_information(students: list) -> int:
    """
    Writes all student information to students.pickle file.
    Returns the number of students.
    """
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> list:
    """
    Reads data from groups.pickle file.
    Returns all group's specialties' names without repetition.
    """
    specialties = set()

    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return list(specialties)


def read_students_information() -> list:
    """
    Reads data from students.pickle file.
    Returns a list of all Student class instances.
    """
    students = []

    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return students
