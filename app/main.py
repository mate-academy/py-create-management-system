import dataclasses
from datetime import datetime
import pickle


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
    with open("groups.pickle", "wb") as load_group_file:
        pickle.dump(groups, load_group_file)
        max_students = 0
        for group in groups:
            num_students = len(group.students)
            if num_students > max_students:
                max_students = num_students

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as load_students_file:
        pickle.dump(students, load_students_file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as read_group_file:
        groups = pickle.load(read_group_file)
        specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as read_students_file:
        students = pickle.load(read_students_file)
    return students
