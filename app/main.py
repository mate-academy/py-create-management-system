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
    average_mark: float | int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: [Student]


def write_groups_information(groups: list[Student]) -> int:
    with open("groups.pickle", "wb") as file_pickle:
        pickle.dump(groups, file_pickle)

    size_group_students = [len(group.students) for group in groups]
    if size_group_students:
        return max(size_group_students)
    return 0


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file_pickle:
        pickle.dump(students, file_pickle)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_pickle:
        groups = pickle.load(file_pickle)

    specialtys = list({group.specialty.name for group in groups})
    return specialtys


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_pickle:
        students = pickle.load(file_pickle)

    return students


if __name__ == "__main__":
    spec1 = Specialty(name="math", number=101)
    spec2 = Specialty(name="fisic", number=102)
    spec3 = Specialty(name="fisic", number=102)
    student1 = Student(
        "ana",
        "silva",
        "2005-01-12",
        8.2,
        True,
        "123",
        "Rua A"
    )

    student2 = Student(
        "ana1",
        "silva",
        "2005-03-12",
        7.2,
        False,
        "456",
        "Rua A"
    )

    student3 = Student(
        "ana2",
        "silva",
        "2005-06-12",
        9.2,
        True,
        "789",
        "Rua A"
    )

    student4 = Student(
        "ana2",
        "silva",
        "2005-06-12",
        9.2,
        True,
        "789",
        "Rua A"
    )

    group1 = Group(
        specialty=spec1,
        course=1,
        students=[student1, student2, student4]
    )
    group2 = Group(
        specialty=spec2,
        course=2,
        students=[student3]
    )
    group3 = Group(
        specialty=spec3,
        course=3,
        students=[student4]
    )

    saida = write_groups_information(
        [
            group1,
            group2,
            group3
        ]
    )
    print(saida)
    saida = write_students_information(
        [
            student1,
            student2,
            student3,
            student4
        ]
    )
    print(saida)
    saida = read_groups_information()
    print(saida)
    saida = read_students_information()
    print(saida)
