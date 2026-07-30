"""
Module responsible for reading the generated CSV, analyzing the dataset,
and outputting actionable metrics.
"""
import csv
from collections import Counter
from typing import Dict, Any, List
from utils import ensure_directory_exists, is_date_overdue

def read_csv_data(filepath: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """Reads a CSV file and returns a list of dictionaries."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

def analyze_contacts(data: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Performs data analysis on the CSV records to generate CRM insights.
    """
    total_contacts = len(data)
    status_counts = Counter()
    source_counts = Counter()
    tag_counts = Counter()
    overdue_follow_ups = 0
    missing_fields_count = 0

    for row in data:
        # Tally distributions
        status_counts[row["status"]] += 1
        source_counts[row["source"]] += 1
        
        # Process flattened tags
        if row["tags"]:
            tags = row["tags"].split("|")
            for tag in tags:
                tag_counts[tag] += 1

        # Check for missing critical data
        if not row["email"] and not row["last_contacted"]:
            missing_fields_count += 1

        # Calculate overdue follow-ups based on the current date
        if row["next_follow_up"] and is_date_overdue(row["next_follow_up"]):
            overdue_follow_ups += 1

    return {
        "total_contacts": total_contacts,
        "status_distribution": dict(status_counts),
        "source_distribution": dict(source_counts),
        "top_tags": dict(tag_counts.most_common(5)),
        "overdue_follow_ups": overdue_follow_ups,
        "records_missing_critical_data": missing_fields_count
    }

def export_analysis(metrics: Dict[str, Any], output_path: str) -> None:
    """Exports the generated metrics to a summary CSV file."""
    ensure_directory_exists(output_path)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        
        writer.writerow(["Total Contacts", metrics["total_contacts"]])
        writer.writerow(["Overdue Follow-ups", metrics["overdue_follow_ups"]])
        writer.writerow(["Records Missing Data", metrics["records_missing_critical_data"]])
        
        writer.writerow([])
        writer.writerow(["--- Status Distribution ---", ""])
        for status, count in metrics["status_distribution"].items():
            writer.writerow([status, count])
            
        writer.writerow([])
        writer.writerow(["--- Source Distribution ---", ""])
        for source, count in metrics["source_distribution"].items():
            writer.writerow([source, count])
