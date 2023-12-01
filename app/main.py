import dataclasses
import pickle
import os


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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_pickle:
        if groups:
            pickle.dump(groups, groups_pickle)
            return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students, students_pickle)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups_pickle:
        if os.path.getsize("groups.pickle") == 0:
            return set()
        return set([
            group.specialty.name
            for group in pickle.load(groups_pickle)
        ])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_pickle:
        return [student for student in pickle.load(students_pickle)]
