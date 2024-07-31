import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: str


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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    # return max(len(group.students) for group in groups) if groups else 0

        students_list = []
    if groups:
        for group in groups:
            students_list.append(len(group.students))
        max_number = max(students_list)
    else:
        max_number = 0
    return max_number


def write_students_information(students: list[Group]) -> int:
    with open("students.pickle", "wb") as file_2:
        pickle.dump(students, file_2)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_3:
        st_list = pickle.load(file_3)
    # return list(set(student.specialty.name for student in st_list))
    # will be a list
    empty = []
    for student in st_list:
        empty.append(student.specialty.name)
    return set(empty)
# def read_groups_information() -> list[Specialty]:
#     with open("groups.pickle", "rb") as file_3:
#         groups = pickle.load(file_3)
#     specialities = []
#     for group in groups:
#         if group.specialty.name in specialities:
#             continue
#         specialities.append(group.specialty.name)
#     return specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_4:
        students = pickle.load(file_4)
    return students
