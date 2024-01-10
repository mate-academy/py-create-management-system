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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_num_of_students = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            max_num_of_students = (
                len(group.students)
                if len(group.students) > max_num_of_students
                else max_num_of_students
            )
        return max_num_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        speciality_names = []
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break
            speciality_names.append(group.specialty.name)
    return set(speciality_names)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students_list = []
        while True:
            try:
                student = pickle.load(pickle_file)
            except EOFError:
                break
            students_list.append(student)
    return students_list
