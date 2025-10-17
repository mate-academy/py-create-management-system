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
    max_students = 0
    students_dict = {}
    for group in groups:
        if group.students:
            for student in group.students:
                students_dict[student.first_name] = student

    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)

    for _ in students_dict:
        max_students += 1
    return max_students


def write_students_information(students: list[Student]) -> int:
    students_num = len(students)

    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)

    return students_num


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_file:
        groups = pickle.load(groups_file)
        specialties_list = []
        for group in groups:
            specialties_list.append(group.specialty.name)
        result_list = list(set(specialties_list))
        return result_list


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        students = pickle.load(students_file)
        return students
