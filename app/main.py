import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Speciality:
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
    adress: str


@dataclasses.dataclass
class Group:
    speciality: Speciality
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    number_of_students = 0
    for group in list_of_groups:
        number_of_students += len(group.students)

    with open("groups.pickle", "a") as file:
        pickle.dump(list_of_groups, file)

    return number_of_students


def write_students_information(list_of_students: list[Student]) -> int:

    with open("students.pickle", "a") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as file:
        list_of_groups = pickle.load(file)

        list_of_groups = list_of_groups.sort(
            key=lambda group: group.speciality.name)

        return list_of_groups


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        list_of_students = pickle.load(file)

        return list_of_students
