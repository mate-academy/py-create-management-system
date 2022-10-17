import dataclasses
import pickle
import datetime


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
    students: list


def write_groups_information(group_list: Group) -> int:
    with open("groups.pickle", "wb") as group_students:
        pickle.dump(group_list, group_students)
    for group_check in group_list:
        return len(group_check.students)


def write_students_information(students_list: Student) -> int:
    with open("students.pickle", "wb") as student_students:
        pickle.dump(students_list, student_students)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as group_students:
        group = pickle.load(group_students)
    speciality = []
    for group_check in group:
        if group_check.specialty.name not in speciality:
            speciality.append(group_check.specialty.name)
    return speciality


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_students:
        student = pickle.load(student_students)
    return student
