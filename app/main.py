import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:

    name: str
    number: int


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
    max_students = []

    with open("groups.pickle", "wb") as data_groups:
        pickle.dump(groups, data_groups)

    for group in groups:
        max_students.append(len(group.students))

    if len(max_students) == 0:
        return 0

    return max(max_students)


def write_students_information(student: list[Student]) -> int:

    with open("students.pickle", "wb") as data_student:
        pickle.dump(student, data_student)

    return len(student)


def read_groups_information() -> list:
    speciality_ls = []
    with open("groups.pickle", "rb") as data:
        group_information = pickle.load(data)

    for group in group_information:
        speciality_ls.append(group.specialty.name)
    unique = set(speciality_ls)

    return list(unique)


def read_students_information() -> list:

    with open("students.pickle", "rb") as data_stud:
        stud_inform = pickle.load(data_stud)

    return stud_inform
