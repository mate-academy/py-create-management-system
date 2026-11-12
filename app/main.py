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
    specialty: "Specialty"
    course: int
    students: list["Student"]


def write_groups_information(lyceum_groups: list["Group"]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_students = 0
        for group in lyceum_groups:
            pickle.dump(group, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
            students = len(group.students)
            if students > max_students:
                max_students = students

        return max_students


def write_students_information(student_list: list["Student"]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_list:
            pickle.dump(student, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        return len(student_list)


def read_groups_information() -> set:
    specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.append(group.specialty.name)
            except EOFError:
                break
        return set(specialties)


def read_students_information() -> list:
    student_list = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                student_list.append(student)
            except EOFError:
                break
        return student_list
