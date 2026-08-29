from dataclasses import dataclass, asdict
from datetime import date
import pickle
import os
import json


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


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# GROUPS_PATH = os.path.join(BASE_DIR, "groups.pickle")
# STUDENTS_PATH = os.path.join(BASE_DIR, "students.pickle")
GROUPS_PATH = "groups.pickle"
STUDENTS_PATH = "students.pickle"


def write_groups_information(groups_list: list[Group]) -> int:
    with open(GROUPS_PATH, "wb") as groups_file:
        pickle.dump(groups_list, groups_file)

    group_sizes = [len(g.students) for g in groups_list]

    return max(group_sizes) if group_sizes else 0


def write_students_information(students_list: list[Student]) -> int:
    with open(STUDENTS_PATH, "wb") as student_file:
        pickle.dump(students_list, student_file)

    return len(students_list)


def read_groups_information() -> set:
    with open(GROUPS_PATH, "rb") as groups_file:
        groups_information = pickle.load(groups_file)

    speciality_names = {group_name.specialty.name
                        for group_name in groups_information}
    return speciality_names


def read_students_information() -> list:
    with open(STUDENTS_PATH, "rb") as student_file:
        return pickle.load(student_file)


if __name__ == "__main__":
    if os.path.exists(GROUPS_PATH):
        with open(GROUPS_PATH, "rb") as f:
            groups = pickle.load(f)

        groups_as_dicts = [asdict(g) for g in groups]

        for group in groups_as_dicts:
            for student in group["students"]:
                student["birth_date"] = student["birth_date"].isoformat()

        # with open(os.path.join(BASE_DIR, "groups.json"), "w") as json_file:
        with open("groups.json", "w") as json_file:
            json.dump(groups_as_dicts, json_file, indent=4, sort_keys=True)

    else:
        print("File groups.pickle doesn't exist – run tests first.")

    if os.path.exists(STUDENTS_PATH):
        with open(STUDENTS_PATH, "rb") as f:
            students = pickle.load(f)

        students_as_dict = [asdict(s) for s in students]

        for student in students_as_dict:
            student["birth_date"] = student["birth_date"].isoformat()

        # with open(os.path.join(BASE_DIR, "students.json"), "w") as json_file:
        with open("students.json", "w") as json_file:
            json.dump(students_as_dict, json_file, indent=4, sort_keys=True)

    else:
        print("File students.pickle doesn't exist – run tests first.")
