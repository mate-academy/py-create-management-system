import dataclasses
import pickle
from datetime import datetime


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


def read_students_information():
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)
    return data


def write_students_information(students_list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        all_groups = pickle.load(f)

    names = []
    for g in all_groups:
        cur_name = g.specialty.name
        if cur_name not in names:
            names.append(cur_name)
    return names


def write_groups_information(groups_data):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups_data, f)

    if not groups_data:
        return 0

    counts = []
    for group in groups_data:
        counts.append(len(group.students))

    return max(counts)