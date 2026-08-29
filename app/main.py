from datetime import datetime
import pickle
import dataclasses


@dataclasses.dataclass
class Specialty:
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
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(group_lists: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in group_lists:
            pickle.dump(group, pickle_file)
        return (
            max(
                len(group.students) for group in group_lists
            ) if group_lists else 0
        )


def read_groups_information() -> list[Group]:
    specialties = set()

    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.add(group.specialty.name)
            except EOFError:
                break
    return sorted(specialties)


def write_students_information(student_lists: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in student_lists:
            pickle.dump(student, pickle_file)
        return len(student_lists)


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students.append(student)
            except EOFError:
                break

    return students
