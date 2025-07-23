import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
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


def write_groups_information(groups: list[Group]) -> int:
    max_number_students = 0
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)

    for group in groups:
        if len(group.students) > max_number_students:
            max_number_students = len(group.students)

    return max_number_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)

    return len(students)


def read_groups_information() -> list[str]:
    specialty_list = []
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        for group in groups:
            specialty_list.append(group.specialty.name)
    return list(set(specialty_list))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as student_file:
        student_list = pickle.load(student_file)
        return student_list
