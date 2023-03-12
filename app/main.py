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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    students_number = []
    with open("groups.pickle", "wb") as groups_pickle:
        for group in groups_list:
            pickle.dump(group, groups_pickle)
            students_number.append(len(group.students))
    return max(students_number, default=0)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        for student in students_list:
            pickle.dump(student, students_pickle)
    return len(students_list)


def read_groups_information() -> set:
    speciality = []
    with open("groups.pickle", "rb") as groups_pickle:
        while True:
            try:
                group = pickle.load(groups_pickle)
            except EOFError:
                break
            else:
                speciality.append(group.specialty.name)
    return set(speciality)


def read_students_information() -> list[Student]:
    student_list = []
    with open("students.pickle", "rb") as students_pickle:
        while True:
            try:
                student_list.append(pickle.load(students_pickle))
            except EOFError:
                break
    return student_list
