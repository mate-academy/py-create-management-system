from dataclasses import dataclass
from datetime import datetime
import pickle
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(lyceum_groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as work_file_gr:
        pickle.dump(lyceum_groups, work_file_gr, pickle.HIGHEST_PROTOCOL)
    count_students = 0
    for work_group in lyceum_groups:
        if len(work_group.students) > count_students:
            count_students = len(work_group.students)
    return count_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as work_file_st:
        pickle.dump(students, work_file_st, pickle.HIGHEST_PROTOCOL)

    return len(students)


def read_groups_information(file_groups: str = "groups.pickle") -> List[Group]:
    with open(file_groups, "rb") as r_work_file_gr:
        read_groups = pickle.load(r_work_file_gr)
    name_groups = []
    for work_read_groups in read_groups:
        if work_read_groups.specialty.name not in name_groups:
            name_groups.append(work_read_groups.specialty.name)
    return name_groups


def read_students_information(
        file_students: str = "students.pickle"
) -> List[Student]:
    with open(file_students, "rb") as r_work_file_st:
        read_student = pickle.load(r_work_file_st)
    return read_student
