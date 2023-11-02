import dataclasses

import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int | str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list["Group"]) -> int:
    with open("groups.pickle", "wb") as file:
        max_student_in_group = 0
        for value in list_of_groups:
            if len(value.students) > max_student_in_group:
                max_student_in_group = len(value.students)
            pickle.dump(value, file)
    return max_student_in_group


def write_students_information(list_of_student: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_student:
            pickle.dump(student, pickle_file)
    return len(list_of_student)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        res_set = set()
        while True:
            try:
                group = pickle.load(pickle_file)
                res_set.add(group.specialty.name)
            except EOFError:
                break
    return list(res_set)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        res_list = []
        while True:
            try:
                student = pickle.load(pickle_file)
                res_list.append(student)
            except EOFError:
                break
    return res_list
