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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_pic:
        pickle.dump(groups, file_pic)

    students_list = []
    for group in groups:
        for student in group.students:
            if student not in students_list:
                students_list.append(student)
    return len(students_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_pic:
        pickle.dump(students, file_pic)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_pic:
        groups = pickle.load(file_pic)
    specialty_names = [group.specialty.name for group in groups]
    return set(specialty_names)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_pic:
        students = pickle.load(file_pic)
    return students
