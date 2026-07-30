"""
Data models and schemas for the outreach tracker pipeline.
Utilizes standard library dataclasses for clean, typed data structures.
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ContactRecord:
    id: str
    name: str
    email: str
    company: str
    role: str
    source: str
    status: str
    tags: List[str] = field(default_factory=list)
    last_contacted: Optional[str] = None
    next_follow_up: Optional[str] = None
    notes: str = ""
    priority: str = "Low"

    def flatten_tags(self, delimiter: str = "|") -> str:
        """Flattens the list of tags into a single string for CSV export."""
        return delimiter.join(self.tags) if self.tags else ""
