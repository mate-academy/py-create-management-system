import pickle


from dataclasses import dataclass
from datetime import date


@dataclass
class Specialty:
    name: str
    number: int | float


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int | str
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    count_of_students = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            count_of_students += [len(group.students)]
            pickle.dump(group, pickle_file)
    return max(count_of_students) if count_of_students else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
    return len(students_list)


def read_groups_information() -> set:
    specialty_list = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
            except EOFError:
                break
            else:
                specialty_list.append(group.specialty.name)
    return set(specialty_list)


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
            except EOFError:
                break
            else:
                list_of_students += [student]
    return list_of_students
