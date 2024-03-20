# write your code here
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(academy_groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(academy_groups, f)
        for academy_group in academy_groups:
            max_students = max(max_students, len(academy_group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        academy_groups = pickle.load(f)
        for academy_group in academy_groups:
            specialties.add(academy_group.specialty.name)
    return specialties


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
