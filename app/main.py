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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as data:
        pickle.dump(groups, data)
        result = []
        if len(groups) > 0:
            result = max([len(group.students) for group in groups])
    return result


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as data:
        groups = pickle.load(data)
        result = []
        for group in groups:
            if group.specialty.name not in result:
                result.append(group.specialty.name)
    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as data:
        pickle.dump(students, data)
    result = len(students)
    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as data:
        students = pickle.load(data)
        result = [student for student in students]
    return result
