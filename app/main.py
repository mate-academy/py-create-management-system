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
    birth_date: datetime.today()
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as new_file:
        pickle.dump(groups, new_file)
    if not groups:
        return 0
    num_of_students = []
    for group in groups:
        num_of_students.append(len(group.students))

    max_num_of_students = max(num_of_students)

    return max_num_of_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as new_file:

        pickle.dump(students, new_file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as new_file:
        groups = pickle.load(new_file)

    specialties = []
    for group in groups:
        specialties.append(group.specialty.name)

    all_specialties = set(specialties)

    return all_specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as new_file:
        list_of_all_student = pickle.load(new_file)

    return list_of_all_student
