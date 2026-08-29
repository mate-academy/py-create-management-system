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
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(list_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_to_write:
        pickle.dump(list_groups, file_to_write)
    if not list_groups:
        return 0

    return max(len(group.students) for group in list_groups)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as file_to_write:
        pickle.dump(students_list, file_to_write)

    return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_to_read:
        list_groups = pickle.load(file_to_read)

    return list({group.specialty.name for group in list_groups})


def read_students_information() -> object:
    with open("students.pickle", "rb") as file_to_read:
        students_list = pickle.load(file_to_read)

    return students_list
