"""
Module responsible for extracting data from JSON, transforming it, 
and loading it into a flattened CSV format.
"""
import json
import csv
from typing import List
from models import ContactRecord
from utils import ensure_directory_exists

def load_json_contacts(filepath: str) -> List[ContactRecord]:
    """Reads a JSON file and instantiates a list of ContactRecord objects."""
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_data = json.load(file)
    
    contacts = []
    for item in raw_data:
        record = ContactRecord(
            id=item.get("id", ""),
            name=item.get("name", ""),
            email=item.get("email", ""),
            company=item.get("company", ""),
            role=item.get("role", ""),
            source=item.get("source", ""),
            status=item.get("status", ""),
            tags=item.get("tags", []),
            last_contacted=item.get("last_contacted", ""),
            next_follow_up=item.get("next_follow_up", ""),
            notes=item.get("notes", ""),
            priority=item.get("priority", "Low")
        )
        contacts.append(record)
    return contacts

def export_to_csv(contacts: List[ContactRecord], output_path: str, delimiter: str = ',') -> None:
    """Flattens ContactRecord objects and writes them to a CSV file."""
    ensure_directory_exists(output_path)
    
    headers = [
        "id", "name", "email", "company", "role", "source", 
        "status", "tags", "last_contacted", "next_follow_up", 
        "notes", "priority"
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=delimiter)
        writer.writeheader()
        
        for contact in contacts:
            row = {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "company": contact.company,
                "role": contact.role,
                "source": contact.source,
                "status": contact.status,
                "tags": contact.flatten_tags(), 
                "last_contacted": contact.last_contacted,
                "next_follow_up": contact.next_follow_up,
                "notes": contact.notes,
                "priority": contact.priority
            }
            writer.writerow(row)
