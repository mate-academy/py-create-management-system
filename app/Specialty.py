from dataclasses import dataclass


@dataclass
class Specialty:
    def __init__(self,
                 name: str,
                 number: int) -> None:
        self.name = name
        self.number = number
