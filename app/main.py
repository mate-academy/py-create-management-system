import pickle
from builtins import int
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
            students_in_group = len(group.students)
            if students_in_group > max_students:
                max_students = students_in_group
    return max_students


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)
    return len(student_list)


def read_groups_information() -> list[str]:
    groups = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                one_group = pickle.load(pickle_file)
            except EOFError:
                break
            group_name = one_group.specialty
            spec_name = group_name.name
            if spec_name not in groups:
                groups.append(spec_name)
    return groups


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                one_student = pickle.load(pickle_file)
            except EOFError:
                break
            if one_student not in students:
                students.append(one_student)
    return students
