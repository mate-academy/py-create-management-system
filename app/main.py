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
    students: list[Student]


def write_groups_information(datas: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for data in datas:
            pickle.dump(data, file)
    if datas:
        return max([len(data.students) for data in datas])
    return 0


def write_students_information(datas: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for data in datas:
            pickle.dump(data, file)
    return len(datas)


def read_groups_information() -> list:
    datas = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                buff = pickle.load(file)
                print("Buff:", buff, "\n")
                datas.append(buff)
            except EOFError:
                break

    if datas:
        return list({data.specialty.name for data in datas})
    return datas


def read_students_information() -> list:
    out = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                out.append(pickle.load(file))
            except EOFError:
                break

    return out
