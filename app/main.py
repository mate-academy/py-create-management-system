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
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups_: list):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_, file)
    stud_list_ = []
    for user_ in groups_:
        stud_list_.append(len(user_.students))
    if stud_list_:
        return max(stud_list_)
    return 0


def write_students_information(students):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    students_len = len(students)
    return students_len


def read_groups_information():
    with open("groups.pickle", "rb") as file_groups:
        users = pickle.load(file_groups)
    s = []
    sp = []
    for spec in users:
        s.append(spec.specialty)
    for special in s:
        sp.append(special.name)
    return set(sp)


def read_students_information():
    with open("students.pickle", "rb") as file_student:
        user = pickle.load(file_student)
        return user
