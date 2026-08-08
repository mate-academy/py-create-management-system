import dataclasses

from datetime import date

from typing import List

import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    if not groups:
        return 0

    max_students = (len(group.students) for group in groups)
    return max(max_students)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as all_students:
        pickle.dump(students_list, all_students)

    return len(students_list)


def read_groups_information() -> list:
    specialities = set()

    with open("groups.pickle", "rb") as source_file:
        groups = pickle.load(source_file)

        for group in groups:
            specialities.add(group.specialty.name)

    return list(specialities)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as source_file:
        students = pickle.load(source_file)

    return [student for student in students]
