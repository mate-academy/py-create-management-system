from dataclasses import dataclass
from datetime import datetime
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
    students: list


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    with open("groups.pickle", "wb") as group_file:
        for group in groups:
            pickle.dump(group, group_file)

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students:
            pickle.dump(student, student_file)

    return len(students)


def read_groups_information() -> set:
    specialty_names = set()
    try:
        with open("groups.pickle", "rb") as read_groups:
            try:
                while True:
                    group = pickle.load(read_groups)
                    specialty_names.add(group.specialty.name)
            except EOFError:
                pass
    except FileNotFoundError:
        pass

    return specialty_names


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as read_students:
        try:
            while True:
                student = pickle.load(read_students)
                students.append(student)
        except EOFError:
            pass

    return students
