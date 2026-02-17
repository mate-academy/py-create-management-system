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


def write_groups_information(group_list: list[Group]) -> int:
    max_count = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            pickle.dump(group, pickle_file)
            max_count = max(max_count, len(group.students))
    return max_count


def write_students_information(list_of_students: list[Student]) -> int:
    student_count = len(list_of_students)
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)
    return student_count


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break
            name = getattr(group, "specialty", None)
            if name and hasattr(group.specialty, "name"):
                specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students = pickle.load(pickle_file)
            except EOFError:
                break
            for student in students:
                list_of_students.append(student)
    return list_of_students
