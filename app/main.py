from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    student_numbers = [0]
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            student_numbers.append(len(group.students))
        pickle.dump(groups, groups_file)
    return max(student_numbers)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> List[str]:
    specialties = set()
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
        for group in groups:
            specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
    return students
