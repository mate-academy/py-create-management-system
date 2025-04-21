import dataclasses
import pickle

from datetime import datetime


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_ls: list[Group]) -> int:
    max_amount_student = 0
    with open("groups.pickle", "wb") as pickle_file_group:

        for group in group_ls:
            current_student_count = len(group.students)

            if current_student_count > max_amount_student:
                max_amount_student = current_student_count
            pickle.dump(group, pickle_file_group)

    return max_amount_student


def write_students_information(students_ls: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file_student:

        for student in students_ls:
            pickle.dump(student, pickle_file_student)

    return len(students_ls)


def read_groups_information(file_name: str = "groups.pickle") -> set:
    groups_ls = []
    speciality_names = []

    with open(file_name, "rb") as pickle_file_group:
        while True:

            try:
                group = pickle.load(pickle_file_group)
                speciality_names.append(group.specialty.name)
                groups_ls.append(group)
            except EOFError:
                break

    return set(speciality_names)


def read_students_information(
        file_name: str = "students.pickle"
) -> list[Student]:
    students_ls = []

    with open(file_name, "rb") as pickle_file_student:
        while True:

            try:
                student = pickle.load(pickle_file_student)
                students_ls.append(student)
            except EOFError:
                break

    return students_ls
