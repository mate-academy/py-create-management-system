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


def write_groups_information(groups: list[Group]) -> int:
    """Escreve a lista de grupos em 'groups.pickle' e retorna o maior número de alunos."""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    """Escreve a lista de estudantes em 'students.pickle' e retorna o total de estudantes."""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    """Lê os grupos e retorna uma lista com os nomes das especialidades (sem repetição)."""
    try:
        with open("groups.pickle", "rb") as f:
            groups: list[Group] = pickle.load(f)

        # Usamos set para garantir a unicidade e depois convertemos para list
        specialty_names = {group.specialty.name for group in groups}
        return list(specialty_names)
    except (FileNotFoundError, EOFError):
        return []


def read_students_information() -> list[Student]:
    """Lê e retorna a lista de estudantes do arquivo 'students.pickle'."""
    try:
        with open("students.pickle", "rb") as f:
            students: list[Student] = pickle.load(f)
        return students
    except (FileNotFoundError, EOFError):
        return []


# Exemplo de uso (opcional para teste):
if __name__ == "__main__":
    # 1. Criar especialidade
    eng = Specialty("Engenharia de Software", 101)

    # 2. Criar estudantes
    s1 = Student("João", "Silva", datetime(2005, 5, 15), 8.5, True, "123456", "Rua A")
    s2 = Student("Maria", "Souza", datetime(2004, 3, 10), 9.0, False, "654321", "Rua B")

    # 3. Criar grupo
    g1 = Group(eng, 1, [s1, s2])

    # Testar funções de escrita
    max_students = write_groups_information([g1])
    total_students = write_students_information([s1, s2])

    print(f"Máximo de alunos por grupo: {max_students}")
    print(f"Total de alunos salvos: {total_students}")

    # Testar funções de leitura
    names = read_groups_information()
    all_students = read_students_information()

    print(f"Especialidades encontradas: {names}")
    print(f"Primeiro estudante lido: {all_students[0].first_name if all_students else 'Nenhum'}")
