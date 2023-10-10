from __future__ import annotations

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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group: list[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        pickle.dump(group, file)

    spis = []
    for i in group:
        if i.students:
            spis.append(len(i.students))
        else:
            return 0
    if spis:
        return max(spis)


def write_students_information(student: list[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(student, file)

    return len(student)


def read_groups_information() -> list | set:

    specialty_name = []

    with open("groups.pickle", "rb") as file:
        data = pickle.load(file)
        for i in data:
            if i.specialty:
                specialty_name.append(i.specialty.name)

        if specialty_name:
            return set(specialty_name)
        else:
            return []


def read_students_information() -> list:
    students_list = []

    with open("students.pickle", "rb") as file:
        data = pickle.load(file)
        for i in data:
            students_list.append(i)

    return students_list
