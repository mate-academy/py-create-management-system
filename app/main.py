import pickle
from dataclasses import dataclass
from datetime import datetime


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


def write_groups_information(input_info: list[Group]) -> int:
    maximum_number_of_students = 0
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(input_info, group_file)
    for group in input_info:
        maximum_number_of_students = (
            max(maximum_number_of_students, len(group.students)))

    return maximum_number_of_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students_list, student_file)

    return len(students_list)


def read_groups_information() -> list:
    all_specialties_without_reps = []
    with open("groups.pickle", "rb") as group_file:
        src = pickle.load(group_file)

        for group in src:
            if group.specialty.name not in all_specialties_without_reps:
                all_specialties_without_reps.append(group.specialty.name)

    return all_specialties_without_reps


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_file:
        src = list(pickle.load(student_file))

    return src
