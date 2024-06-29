from dataclasses import dataclass

@dataclass
class Gene:
    id:int
    cromosoma : int



    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.id}"