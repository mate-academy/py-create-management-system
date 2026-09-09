from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    student_counts = []
    with open("groups.pickle", "wb") as w_group_info:
        for group in groups:
            pickle.dump(group, w_group_info)

            count_of_group_students = len(group.students)
            student_counts.append(count_of_group_students)
    if not student_counts:
        return 0

    return max(student_counts)


def write_students_information(students: list[Student]) -> int:
    count_of_students = 0
    with open("students.pickle", "wb") as w_student_info:
        for student in students:
            pickle.dump(student, w_student_info)
            count_of_students = count_of_students + 1

    return count_of_students


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as r_group_info:
        specialty_names = set()

        while True:
            try:
                group = pickle.load(r_group_info)
                specialty_names.add(group.specialty.name)

            except EOFError:
                break
    return list(specialty_names)


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as r_student_info:

        while True:
            try:
                student = pickle.load(r_student_info)
                students_list.append(student)
            except EOFError:
                break
    return students_list
