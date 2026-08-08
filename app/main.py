import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: int | float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as open_file:
        pickle.dump(groups, open_file)
    if groups:
        list_students = [len(group.students) for group in groups]
        return max(list_students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as open_file:
        pickle.dump(students, open_file)
    return len(students)


def read_groups_information() -> set[Specialty]:
    with open("groups.pickle", "rb") as open_file:
        groups = pickle.load(open_file)
    group = {g.specialty.name for g in groups}
    return group


def read_students_information() -> list:
    with open("students.pickle", "rb") as open_file:
        students = pickle.load(open_file)
    student_list = [student for student in students]
    return student_list
