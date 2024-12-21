from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    number_of_student = 0
    for group in groups:
        if number_of_student < len(group.students):
            number_of_student += len(group.students)
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(groups, file_group)

    return number_of_student


def write_students_information(students: list[Student]) -> int:
    number_of_student = len(students)

    with open("students.pickle", "wb") as file_student:
        pickle.dump(students, file_student)

    return number_of_student


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_group:
        data = pickle.load(file_group)
        return_set = [specialty.specialty.name for specialty in data]
    return set(return_set)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_group:
        data = pickle.load(file_group)
    return data
