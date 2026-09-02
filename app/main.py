from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float | int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    try:
        return max(len(group.students) for group in groups)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_groups_information() -> list:
    groups_list = []
    with open("groups.pickle", "rb") as group_file:
        while True:
            try:
                groups_list.append(pickle.load(group_file).specialty.name)
            except EOFError:
                break
    return list(set(groups_list))


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as student_file:
        while True:
            try:
                students_list.append(pickle.load(student_file))
            except EOFError:
                break

    return students_list
