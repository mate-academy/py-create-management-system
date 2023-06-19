import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


@dataclass
class Student:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: datetime,
                 average_mark: str,
                 has_scholarship: str,
                 phone_number: str,
                 address: str
                 ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address


@dataclass
class Group:
    def __init__(self,
                 specialty: Specialty,
                 course: str,
                 students: List[Student]
                 ) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = 0
    for group in groups:
        students = len(group.students)
        if max_students < students:
            max_students += students
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialities = set()
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    for group in groups:
        if group.specialty.name not in specialities:
            specialities.add(group.specialty.name)
    return list(specialities)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
