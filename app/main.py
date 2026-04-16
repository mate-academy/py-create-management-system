import pickle
from app.models import Specialty, Student, Group  # noqa: F401


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            return list(set(group.specialty.name for group in groups))
    except (FileNotFoundError, EOFError):
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []


def main() -> None:
    pass


if __name__ == "__main__":
    main()
