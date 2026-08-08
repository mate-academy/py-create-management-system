from dataclasses import dataclass
from datetime import date
from typing import List, Iterable
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
    average_mark: float | int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_groups: List[Group]) -> int | None:
    with open("groups.pickle", "wb") as groups_data:
        pickle.dump(list_of_groups, groups_data)
        try:
            return max(
                len(group.students)
                for group in list_of_groups
                if list_of_groups
            )
        except ValueError:
            return


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as studant_data:
        pickle.dump(list_of_students, studant_data)

        return len(list_of_students)


def read_groups_information(groups_file: pickle = "groups.pickle") -> Iterable:
    with open(groups_file, "rb") as group_data:
        groups_specialties = list(
            {group.specialty.name for group in pickle.load(group_data)}
        )

        return groups_specialties


def read_students_information(
    studets_file: pickle = "students.pickle",
) -> List[Student]:
    with open(studets_file, "rb") as file:
        students = pickle.load(file)

    return students
