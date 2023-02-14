import dataclasses
import pickle
from datetime import datetime
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)

    numbers_student = []
    for group in groups:
        for student in group.students:
            if student not in numbers_student:
                numbers_student.append(student)
    return len(numbers_student)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)

    numbers_student = 0
    for _ in students:
        numbers_student += 1
    return numbers_student


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)

    name_all_specialties = [group.specialty.name for group in groups]
    return set(name_all_specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)

    return students
