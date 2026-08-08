# write your code here
import dataclasses
import pickle
from typing import List


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
    students: List[Student]


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
    return len(students_list)


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    return max([len(group.students) for group in groups])


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_group:
        groups = pickle.load(file_group)
        if not file_group:
            return set()
    return set([group.specialty.name for group in groups])


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as student_info:
        students = pickle.load(student_info)
    return students
