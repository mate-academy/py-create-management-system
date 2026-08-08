from dataclasses import dataclass
import datetime
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
    students: list[Student]


def write_groups_information(list_group: list[Group]) -> int:
    len_students = [len(group.students) for group in list_group]
    max_group = max(len_students) if len_students else 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_group, file)
    return max_group


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        list_group = pickle.load(file)
    list_group = [group.specialty.name for group in list_group]
    return set(list_group)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_student = pickle.load(file)
    return list_student
