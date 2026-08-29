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
    students: list


def write_groups_information(list_of_the_group: list[Group]) -> int:
    max_of_students = max((len(group.students) for
                           group in list_of_the_group), default=0)
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_of_the_group, pickle_file)
    return max_of_students


def write_students_information(list_of_the_student: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_the_student, pickle_file)
    return len(list_of_the_student)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as pickle_file:
        list_of_the_group = pickle.load(pickle_file)
        groups_specialties_names = {group.specialty.name for
                                    group in list_of_the_group}
    return groups_specialties_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        list_of_the_student = pickle.load(pickle_file)
    return list_of_the_student
