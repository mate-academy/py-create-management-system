from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    list_of_student = []

    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str

    def __post_init__(self) -> None:
        Student.list_of_student.append(self)


@dataclass
class Group:
    list_of_group_instances = []
    specialty: Specialty
    course: str
    students: list[Student]

    def __post_init__(self) -> None:
        Group.list_of_group_instances.append(self)


def read_groups_information() -> set:
    all_groups = list()
    specialities = set()
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                all_groups.append(pickle.load(file))
        except EOFError:
            for group in all_groups:
                specialities.add(group.specialty)
    return specialities


def write_groups_information() -> int:
    with open("groups.pickle", "wb") as file:
        for group in Group.list_of_group_instances:
            pickle.dump(group, file)

    total_student_counter = 0
    for group in Group.list_of_group_instances:
        total_student_counter += len(group.students)

    return total_student_counter


def write_students_information() -> int:
    with open("students.pickle", "wb") as file:
        for student in Student.list_of_student:
            pickle.dump(student, file)
    return len(Student.list_of_student)


def read_students_information() -> list:
    all_student = list()
    with open("students.pickle", "rb") as file:
        try:
            while True:
                all_student.append(pickle.load(file))
        except EOFError:
            return all_student
