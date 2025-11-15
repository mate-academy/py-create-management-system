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
    students: list[Student]


def write_groups_information(groups_data: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_data, file)

    max_student = 0
    for group in groups_data:
        if len(group.students) > max_student:
            max_student = len(group.students)
    return max_student


def write_students_information(students_data: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_data, file)

    return len(students_data)


def read_groups_information() -> set[Group]:
    with open("groups.pickle", "rb") as file:
        set_of_group = set()
        res = pickle.load(file)
        for el in res:
            set_of_group.add(el.specialty.name)
    return set_of_group


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students_list = []
        student = pickle.load(file)
        students_list.extend(student)
        return students_list
