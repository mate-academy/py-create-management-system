import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date : datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    """
    This function writes all inputted information about the
    Lyceum groups to the file named "groups.pickle".
    The input is a list of the Group class instances.
    :return:
    This function returns the maximum number of students from all the groups.
    """
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: list[Student]) -> int:
    """
    This function writes information about students
    to the "students.pickle" file.
    You should store all the students in one file.
    The input is a list of the Student class instances.
    :return:
    This function returns the number of students.
    """
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    """
    This function reads data from the "groups.pickle" file.
    :return:
    It returns all group's specialties' names without repetition.
    """
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
    except (EOFError, ValueError):
        pass
    return list(specialties)


def read_students_information() -> list[Student]:
    """
    This function reads data from the "students.pickle" file.
    :return:
    It returns a list of all the Student class instances.
    """
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                student = pickle.load(file)
                students.append(student)
    except EOFError:
        pass
    return students
