from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: float | int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_num_of_students = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        for group in groups:
            if max_num_of_students < len(group.students):
                max_num_of_students = len(group.students)

    return max_num_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)
    return len(students)


def read_groups_information() -> list:
    result = set()
    with open("groups.pickle", "rb") as groups_pickle:
        groups = pickle.load(groups_pickle)
        for group in groups:
            result.add(group.specialty.name)
    return list(result)


def read_students_information() -> list:
    result = []
    with open("students.pickle", "rb") as students_pickle:
        result = pickle.load(students_pickle)

    return result
