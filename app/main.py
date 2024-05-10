from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: [Student]


def write_groups_information(groups: [Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    amount_of_students = [0]
    for group in groups:
        amount_of_students.append(len(group.students))
    return max(amount_of_students)


def write_students_information(students: [Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information(pickle_file: str = "groups.pickle") -> list:
    with open(pickle_file, "rb") as f:
        groups = pickle.load(f)
        list_of_specialty = []
    for group in groups:
        list_of_specialty.append(group.specialty.name)
    return list(set(list_of_specialty))


def read_students_information(pickle_file: str = "students.pickle") -> str:
    with open(pickle_file, "rb") as f:
        students = pickle.load(f)
    return students
