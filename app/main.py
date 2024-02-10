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
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    max_len = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > max_len:
                max_len = len(group.students)
            pickle.dump(group, file)
    return max_len


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    result_list = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                if group.specialty.name not in result_list:
                    result_list.append(group.specialty.name)
            except EOFError:
                return result_list


def read_students_information() -> list:
    result_list = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                result_list.append(student)
        except EOFError:
            return result_list
