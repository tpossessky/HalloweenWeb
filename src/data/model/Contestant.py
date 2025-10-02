from dataclasses import dataclass, field
from typing import List

from src.data.model.Member import Member


@dataclass
class Contestant:
    id: int = 0
    members: List[Member] = field(default_factory=list)
    isGroup: bool = False
    groupCostume: str = ""