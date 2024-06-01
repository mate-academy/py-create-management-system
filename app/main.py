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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: Student


def write_groups_information(groups: list) -> int:
    max_count_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > max_count_students:
                max_count_students = len(group.students)
        pickle.dump(groups, file)

    return max_count_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    all_specialities = set()
    with open("groups.pickle", "rb") as file:
        groups_data = pickle.load(file)
        for group in groups_data:
            speciality = group.specialty.name
            if speciality:
                all_specialities.add(speciality)
    return list(all_specialities)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students_data = pickle.load(file)
        return students_data
