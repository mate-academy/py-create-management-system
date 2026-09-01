import pickle
from dataclasses import dataclass


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students_group = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if len(group.students) > max_students_group:
                max_students_group = len(group.students)

    return max_students_group


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> list[str]:
    unique_specialities = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group_instance = pickle.load(f)
                unique_specialities.add(group_instance.specialty.name)
            except EOFError:
                break

    return list(unique_specialities)


def read_students_information() -> list[Student]:
    result_list = list()
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student_instance = pickle.load(f)
                result_list.append(student_instance)
            except EOFError:
                break

    return result_list
