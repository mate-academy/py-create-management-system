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
    average_mark : float | int
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    num_of_studes = []
    with open("groups.pickle", "wb") as new_file:
        pickle.dump(groups, new_file)
        for elem in groups:
            num_of_studes.append(len(elem.students))
        if num_of_studes == []:
            return 0
        return max(num_of_studes)


def write_students_information(studs_list: list[Student]) -> int:
    with open("students.pickle", "wb") as new_file_two:
        pickle.dump(studs_list, new_file_two)
    return len(studs_list)


def read_groups_information() -> list:
    specs = []
    with open("groups.pickle", "rb") as n_read_file:
        reed_file = pickle.load(n_read_file)
        for elem in reed_file:
            specs.append(elem.specialty.name)
        return list(set(specs))


def read_students_information() -> list:
    instances = []
    with open("students.pickle", "rb") as opened_file:
        worked_up_file = pickle.load(opened_file)
        for elem in worked_up_file:
            instances.append(elem)
        return instances
