from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: str


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: set
    course: str
    students: list


def write_groups_information(group_list: list) -> int:
    with open("groups.pickle", "wb") as file_pickle:
        pickle.dump(group_list, file_pickle)
    max_student = 0
    for group in group_list:
        sum_student = len(group.students)
        if sum_student > max_student:
            max_student = sum_student
    return max_student


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(students, file_students)
    return len(students)


def read_groups_information() -> set:
    specialities = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                for student in group:
                    specialities.add(student.specialty.name)
            except EOFError:
                break
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_pickle:
        students = pickle.load(file_pickle)
    return students
