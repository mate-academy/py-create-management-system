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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups: list[Group] = pickle.load(file)
            specialty_names = {group.specialty.name for group in groups}
            return list(specialty_names)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students: list[Student] = pickle.load(file)
            return students
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    specialty = Specialty(name="Computer Science", number=101)
    student1 = Student(
        first_name="John",
        last_name="Doe",
        birth_date=datetime(2000, 5, 15),
        average_mark=85.5,
        has_scholarship=True,
        phone_number="123-456-7890",
        address="123 Main St, Anytown"
    )
    student2 = Student(
        first_name="Jane",
        last_name="Smith",
        birth_date=datetime(2001, 3, 22),
        average_mark=90.0,
        has_scholarship=False,
        phone_number="098-765-4321",
        address="456 Elm St, Othertown"
    )
    group = Group(specialty=specialty, course=1, students=[student1, student2])

    groups = [group]
    max_students = write_groups_information(groups)
    num_students = write_students_information([student1, student2])

    print(f"Max students in any group: {max_students}")
    print(f"Total number of students written: {num_students}")

    unique_specialties = read_groups_information()
    all_students = read_students_information()

    print(f"Unique specialty names: {unique_specialties}")
    print(f"All students: {all_students}")
