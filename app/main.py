from dataclasses import dataclass
from datetime import datetime, date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    students_in_group = []

    with open("groups.pickle", "wb") as pickle_file:
        for group in group_list:
            students_in_group.append(len(group.students))
        pickle.dump(group, pickle_file)

    return max(students_in_group)


def write_students_information():
    pass


def read_groups_information():
    pass


def read_students_information():
    pass


if __name__ == "__main__":
    kwargs = [Group(specialty=Specialty("Math and Physic", 1),
                    course=1,
                    students=[])]
    print(write_groups_information(kwargs))
