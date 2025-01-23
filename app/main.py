from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass(frozen=True, order=True)
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
    course: str
    students: list[Student]


def write_groups_information(group_input: list[Group]) -> int:
    group_len_list = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_input:
            pickle.dump(group, pickle_file)
            group_len_list.append(len(group.students))
        if not group_len_list:
            return 0
        return max(group_len_list)


def write_students_information(students_input: list[Student]) -> int:
    number_of_students = len(students_input)
    with open("students.pickle", "wb") as pickle_file:
        for student in students_input:
            pickle.dump(student, pickle_file)
        return number_of_students


def read_groups_information() -> list:
    list_of_specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
                if obj.specialty.name not in list_of_specialties:
                    list_of_specialties.append(obj.specialty.name)
            except EOFError:
                break
    return sorted(list_of_specialties)


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                obj = pickle.load(pickle_file)
                list_of_students.append(obj)
            except EOFError:
                break
    return list_of_students
