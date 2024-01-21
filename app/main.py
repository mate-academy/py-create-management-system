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


def read_groups_information(groups_file="groups.pickle") -> set:
    all_groups = list()
    specialities = set()
    with open(groups_file, "rb") as file:
        try:
            while True:
                all_groups.append(pickle.load(file))
        except EOFError:
            for group in all_groups:
                specialities.add(group.specialty)
    return specialities


def write_groups_information(groups=None) -> int:
    counter = 0
    if groups is None:
        groups = Group.list_of_group_instances
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    total_student_counter = 0
    for group in Group.list_of_group_instances:
        total_student_counter += len(group.students)

    return total_student_counter


def write_students_information(students=None) -> int:
    counter = 0
    if students is None:
        students = Student.list_of_student

    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            counter += 1
    return counter


def read_students_information(students_file="students.pickle") -> list:
    all_student = list()
    with open(students_file, "rb") as file:
        try:
            while True:
                all_student.append(pickle.load(file))
        except EOFError:
            return all_student
