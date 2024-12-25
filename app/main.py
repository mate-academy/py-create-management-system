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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: object
    course: datetime.year
    students: list[Student]

# def write_groups_information(groups: list[Group]) -> int:
#     with open("groups.pickle", "wb") as group_file:
#         group_count = 0
#         for group in groups:
#             pickle.dump(group, group_file)
#             if len(group.students) > group_count:
#                 group_count = len(group.students)
#     return group_count
#
#
# def write_students_information(students: list[Student]) -> int:
#     with open("students.pickle", "wb") as students_file:
#         number_of_students = 0
#         for student in students:
#             number_of_students += 1
#             pickle.dump(student, students_file)
#     return number_of_students
#
#
# def read_groups_information() -> set:
#     groups = []
#     with open("groups.pickle", "rb") as file:
#         data_group = pickle.load(file)
#         for group in data_group:
#             if group.specialty.name not in groups:
#                 groups.append(group.specialty.name)
#     return set(groups)
#
#
# def read_students_information() -> list[Student]:
#     with open("students.pickle", "rb") as file:
#         data_students = pickle.load(file)
#     return data_students

def write_groups_information(list_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_groups, file)
    if not list_groups:
        return 0
    return max(len(group.students) for group in list_groups)


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)

    return len(list_students)


def read_groups_information() -> set:
    groups = []
    with open("groups.pickle", "rb") as file:
        data_group = pickle.load(file)
        for group in data_group:
            if group.specialty.name not in groups:
                groups.append(group.specialty.name)
    return groups


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        data_students = pickle.load(file)
    return data_students
