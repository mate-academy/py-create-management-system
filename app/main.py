import dataclasses
import pickle
from typing import List
from datetime import date


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(grups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_name:
        pickle.dump(grups, file_name)
    students = []
    for student in grups:
        for man in student.students:
            if man not in students:
                students.append(man)
    return len(students)


def write_students_information(studets: list) -> int:
    with open("students.pickle", "wb") as file_name:
        pickle.dump(studets, file_name)
    return len(studets)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as new_file:
        grups = pickle.load(new_file)
        specialty = []
        for grup in grups:
            specialty.append(grup.specialty.name)
        spec = []
        for i in specialty:
            if i in spec:
                break
            else:
                spec.append(i)
    return spec


def read_students_information() -> list:
    with open("students.pickle", "rb") as new_file:
        students = pickle.load(new_file)
        new_student = []
        for student in students:
            new_student.append(student)
    return new_student
