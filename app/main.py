from typing import List, Union, Any
import dataclasses
import pickle


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups : List[Group]) -> Union[List[Any], int]:
    with open("groups.pickle", "wb") as files:
        pickle.dump(groups, files)
    students_list = []
    if not groups:
        return []
    else:
        for group in groups:
            student = group.students
            if not student:
                return 0
            else:
                students_list.append(len(student))
        return max(students_list)


def write_students_information(students : str) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> Union[List[Any], list]:
    spesiality_list = []
    with open("groups.pickle", "rb") as files:
        users = pickle.load(files)
        for user in users:
            if not user.specialty.name:
                return []
            spesiality_list.append(user.specialty.name)

        return list(set(spesiality_list))


def read_students_information() -> list:
    with open("students.pickle", "rb") as files:
        students = pickle.load(files)
    return students
