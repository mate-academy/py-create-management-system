import dataclasses
from datetime import datetime
import pickle


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list


def write_groups_information(groups_base: list[Group]) -> int:
    with open("groups.pickle", "wb") as out_info:
        pickle.dump(groups_base, out_info)

    if groups_base:
        return max(len(group.students) for group in groups_base)


def write_students_information(students_base: list[Student]) -> int:
    with open("students.pickle", "wb") as out_info:
        pickle.dump(students_base, out_info)

    return len(students_base)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as in_info:
        upd_groups_base = pickle.load(in_info)
        speciality_list = []
        for group in upd_groups_base:
            if group.specialty.name not in speciality_list:
                speciality_list.append(group.specialty.name)

    return speciality_list


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as in_info:
        upd_students_base = pickle.load(in_info)

    return upd_students_base
