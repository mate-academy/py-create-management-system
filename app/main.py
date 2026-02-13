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


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
    students_count = []
    for group in group_list:
        students_count.append(len(group.students))
    if students_count:
        return max(students_count)
    else:
        return 0


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file)
    return len(student_list)


def read_groups_information() -> list:
    names = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                gr = pickle.load(pickle_file)
                if gr.specialty.name not in names:
                    names.append(gr.specialty.name)
            except EOFError:
                break
    return names


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                stud = pickle.load(pickle_file)
                students.append(stud)
            except EOFError:
                break
    return students
