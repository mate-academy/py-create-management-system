import dataclasses
from datetime import datetime
import pickle
from typing import List


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
    course: str
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups:
        max_count_of_stud = 0
        for student in group_list:
            pickle.dump(student, pickle_groups)
            if len(student.students) > max_count_of_stud:
                max_count_of_stud = len(student.students)
        return max_count_of_stud


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_stud:
        for student in student_list:
            pickle.dump(student, pickle_stud)
    return len(student_list)


def read_groups_information() -> set:
    list_of_speciality = []
    with open("groups.pickle", "rb") as pickle_groups:
        while True:
            try:
                group = pickle.load(pickle_groups)
                list_of_speciality.append(group.specialty.name)
            except EOFError:
                break
    return set(list_of_speciality)


def read_students_information() -> list:
    stud_list = []
    with open("students.pickle", "rb") as pickle_groups:
        while True:
            try:
                student = pickle.load(pickle_groups)
                stud_list.append(student)
            except EOFError:
                break
    return stud_list
