import dataclasses
from datetime import datetime
import pickle

@dataclasses.dataclass
class Especialidade:
    name: str
    number: int

@dataclasses.dataclass
class Estudante:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

@dataclasses.dataclass
class Grupo:
    specialty: Especialidade
    course: int
    students: list[Estudante]


def escrever_informações_de_grupos(groups: list[Grupo]) -> int:
    """Grava as instâncias de Grupo no arquivo 'groups.pickle' 
    e retorna o número máximo de alunos entre todos os grupos."""
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def escrever_informações_dos_alunos(students: list[Estudante]) -> int:
    """Grava as instâncias de Estudante no arquivo 'students.pickle' 
    e retorna o total de alunos."""
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
            
    return len(students)


def ler_informações_dos_grupos() -> list[str]:
    """Lê os dados do arquivo 'groups.pickle' e retorna 
    os nomes únicos de todas as especialidades dos grupos."""
    specialty_names = set()
    
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialty_names.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
        
    return list(specialty_names)


def ler_informações_dos_alunos() -> list[Estudante]:
    """Lê os dados do arquivo 'students.pickle' e retorna 
    uma lista com todas as instâncias de Estudante."""
    students = []
    
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []
        
    return students
