import dataclasses
from datetime import datetime
import pickle


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


groups = [
    Group(Specialty("Math and Physic", 1),
          1,
          [
              Student(
                  first_name="Petya",
                  last_name="Philosophy",
                  birth_date=datetime(2001, 5, 1),
                  average_mark=3.0,
                  has_scholarship=True,
                  phone_number="+91123456789",
                  address="123 Main St"
              ),
              Student(
                  first_name="Vasya",
                  last_name="Vikolaev",
                  birth_date=datetime(2001, 6, 1),
                  average_mark=3.0,
                  has_scholarship=True,
                  phone_number="+91123456789",
                  address="123 Main St"
              ),
              Student(
                  first_name="Taya",
                  last_name="Krasina",
                  birth_date=datetime(2001, 6, 1),
                  average_mark=3.0,
                  has_scholarship=True,
                  phone_number="+91123456789",
                  address="123 Main St"
              )]
          ),
    Group(Specialty("English", 2),
          2,
          [
              Student(
                  first_name="Katya",
                  last_name="Katina",
                  birth_date=datetime(2001, 5, 1),
                  average_mark=3.0,
                  has_scholarship=True,
                  phone_number="+91123456789",
                  address="123 Main St"
              ),
              Student(
                  first_name="Sanya",
                  last_name="Petin",
                  birth_date=datetime(2001, 6, 1),
                  average_mark=3.0,
                  has_scholarship=True,
                  phone_number="+91123456789",
                  address="123 Main St"
              )]
          )
]


students = [student for group in groups for student in group.students]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    if len(groups) == 0:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> set:
    specialty = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group = pickle.load(f)
            except EOFError:
                break

            specialty.add(group.specialty.name)

    return specialty


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
            except EOFError:
                break

            students.append(student)

    return students
