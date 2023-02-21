from datetime import datetime
from typing import List
import dataclasses
import pickle


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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        students_list = []
        groups_list = []
        for group in groups:
            groups_list.append(group)
            for student in group.students:
                if student not in students_list:
                    students_list.append(student)
        pickle.dump(groups_list, groups_file)
    return len(students_list)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        students_list = [student for student in students]
        pickle.dump(students_list, students_file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
        specialties = [group.specialty.name for group in groups]
    return set(specialties)


def read_students_information() -> set:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
