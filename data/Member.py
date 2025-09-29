from dataclasses import dataclass


@dataclass
class Member:
    id: int
    costume: str
    full_name: str