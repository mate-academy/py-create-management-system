import pickle
from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    list_of_instances = []

    for group in groups:
        list_of_instances.extend(group.students)
    for student in list_of_instances:
        if list_of_instances.count(student) > 1:
            list_of_instances.remove(student)

    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)

    return len(list_of_instances)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)

    cashed_students = deepcopy(students)

    for student in cashed_students:
        if cashed_students.count(student) > 1:
            cashed_students.remove(student)
    return len(cashed_students)


def read_groups_information() -> List[Group]:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
