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
    phone_number: int
    address: int


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_groups_info:
        pickle.dump(groups, pickle_groups_info)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students_info:
        pickle.dump(students, pickle_students_info)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_groups_info:
        groups = pickle.load(pickle_groups_info)
    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_students_info:
        students = pickle.load(pickle_students_info)
    return students
