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


def write_groups_information(grope_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(grope_list, pickle_file)
        students = [len(grope.students) for grope in grope_list]
        if not students:
            return 0
    return max(students)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)
    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        grope_list = pickle.load(pickle_file)
        return list(set([grope.specialty.name for grope in grope_list]))


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students_list = pickle.load(pickle_file)
        return students_list
