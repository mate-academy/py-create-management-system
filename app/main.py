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
    birth_date: int
    average_mark: int | float
    has_scholarship: bool
    phone_number: int
    address: str

@dataclass
class Group:
    specialty: Specialty
    course: int
    students: [Student]


def write_groups_information(all_info: [Group]) -> int:
    with open ("groups.pickle", "wb") as file:
        pickle.dump(all_info, file)
    total = []
    for el in all_info:
        num = len(el.students)
        total.append(num)
    return max(total)


def write_students_information(all_info: [Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(all_info, file)
    return len(all_info)


def read_groups_information() -> list:
    finlist = []
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                per = pickle.load(file)
                finlist.append(per.specialty.name)
    except EOFError:
        pass
    return list(set(finlist))

def read_students_information() -> list:
    finlist = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                per = pickle.load(file)
                finlist.append(per)
    except EOFError:
        pass
    return finlist
