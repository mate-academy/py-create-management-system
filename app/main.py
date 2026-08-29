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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    students = 0
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups_list:
            if len(group.students) > students:
                students = len(group.students)
            pickle.dump(group, pickle_file)
    return students


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students_list:
            pickle.dump(student, pickle_file)
    return len(students_list)


def read_groups_information() -> list:
    groups_specialities = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                if group.specialty.name not in groups_specialities:
                    groups_specialities.append(group.specialty.name)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                break
    return groups_specialities


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                break
    return students
