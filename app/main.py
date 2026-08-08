import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: int
    birth_date: int
    average_mark: str
    has_scholarship: int
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(list_of_groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

    count_students = 0
    for group in list_of_groups:
        if len(group.students) > count_students:
            count_students = len(group.students)
    return count_students


def write_students_information(student_list: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student_list, file)
    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        return set(group.specialty.name for group in groups)


def read_students_information() -> Student:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
