import dataclasses
import pickle
from datetime import datetime


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
    course: datetime
    students: list[Student]


def write_groups_information(group: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(group, groups)
        count_students = max((len(inst.students) for inst in group), default=0)
    return count_students


def write_students_information(student: list[Student]) -> int:
    students_count = len(student)
    with open("students.pickle", "wb") as file_students:
        pickle.dump(student, file_students)
    return students_count


def read_groups_information() -> list[str]:
    list_names = []
    with open("groups.pickle", "rb") as groups_file:
        names = pickle.load(groups_file)
        for name in names:
            if name.specialty.name not in list_names:
                list_names.append(name.specialty.name)
    return list_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as groups_students:
        student = pickle.load(groups_students)
    return student
