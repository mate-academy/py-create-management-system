from typing import List, Set
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
    students: List[Student]


def write_groups_information(groups_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)
    max_students = max(len(group.students) for group in groups_list)
    return max_students


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)
    return len(students_list)


def read_groups_information() -> Set[str]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            for group in pickle.load(file):
                specialties.add(group.specialty.name)
    except FileNotFoundError:
        print("File 'groups.pickle' not found.")
    return specialties


def read_students_information() -> List[Student]:
    students_list = []
    try:
        with open("students.pickle", "rb") as file:
            students_list = pickle.load(file)
    except FileNotFoundError:
        print("File 'students.pickle' not found.")
    return students_list
