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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_file:

        for group in group_list:
            if len(group.students) > max_students:
                max_students = len(group.students)
        pickle.dump(group_list, groups_file)

    return max_students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_file:
        specialties = [group.specialty.name for group in pickle.load(groups_file)]

    return set(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        return [student for student in pickle.load(students_file)]
