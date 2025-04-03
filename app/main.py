import dataclasses
from datetime import datetime
import pickle
import os


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: int
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    if group_list:
        with open("groups.pickle", "wb") as pickle_file:
            pickle.dump(group_list, pickle_file)
        max_quantity_of_all_groups = len(group_list[0].students)
        for size in group_list:
            if len(size.students) >= max_quantity_of_all_groups:
                max_quantity_of_all_groups = len(size.students)
        return max_quantity_of_all_groups
    return 0


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)
    return len(list_of_students)


def read_groups_information(name_file: str = "groups.pickle") -> list:
    if not os.path.exists("groups.pickle"):
        return []
    with open(name_file, "rb") as pickle_file:
        loaded_groups = pickle.load(pickle_file)
    specialties = set(group.specialty.name for group in loaded_groups)
    return list(specialties)


def read_students_information(name_file: str = "students.pickle") -> list:
    with open(name_file, "rb") as pickle_file:
        loaded_students = pickle.load(pickle_file)
    return [i for i in loaded_students]
