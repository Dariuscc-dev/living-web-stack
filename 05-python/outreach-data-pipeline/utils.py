"""
Utility functions for data validation, date parsing, and file handling.
"""
import datetime
from pathlib import Path

def ensure_directory_exists(filepath: str) -> None:
    """Ensures that the directory for a given filepath exists."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

def parse_iso_date(date_str: str) -> datetime.date | None:
    """
    Safely parses an ISO format date string (YYYY-MM-DD).
    Returns None if the string is empty or invalid.
    """
    if not date_str:
        return None
    try:
        return datetime.date.fromisoformat(date_str)
    except ValueError:
        return None

def is_date_overdue(date_str: str, reference_date: datetime.date = None) -> bool:
    """
    Checks if a given date string is in the past relative to a reference date.
    Defaults to today if no reference date is provided.
    """
    target_date = parse_iso_date(date_str)
    if not target_date:
        return False
    
    if reference_date is None:
        reference_date = datetime.date.today()
        
    return target_date < reference_date
