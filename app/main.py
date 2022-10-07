import dataclasses
from datetime import date
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    lenght_list = [len(group.students) for group in groups]
    result = 0
    if len(lenght_list) > 0:
        result = max(lenght_list)
    return result


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    filename = "groups.pickle"
    with open(filename, "rb") as file:
        groups = pickle.load(file)
    print("groupsssss", groups)
    return set([group.specialty.name for group in groups])


def read_students_information() -> list:
    filename = "students.pickle"
    with open(filename, "rb") as file:
        students = pickle.load(file)
    return students
