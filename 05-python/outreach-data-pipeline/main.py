"""
Main entry point for the Outreach Data Pipeline.
Handles CLI arguments, orchestrates the ETL process, and displays output.
"""
import argparse
import sys
from json_to_csv import load_json_contacts, export_to_csv
from csv_processor import read_csv_data, analyze_contacts, export_analysis

def setup_argparse() -> argparse.ArgumentParser:
    """Configures command-line interface arguments."""
    parser = argparse.ArgumentParser(
        description="Micro-CRM Data Pipeline: Convert JSON to CSV and analyze professional outreach data."
    )
    parser.add_argument("--input", required=True, help="Path to the source JSON file.")
    parser.add_argument("--output", required=True, help="Path to save the generated CSV file.")
    parser.add_argument("--analysis-output", help="Optional path to save the analysis summary as CSV.")
    parser.add_argument("--delimiter", default=",", help="Delimiter for the CSV files (default: ',').")
    parser.add_argument("--sort-by", choices=["next_follow_up", "name", "priority"], 
                        help="Sort the output CSV by a specific column.")
    parser.add_argument("--verbose", action="store_true", help="Print detailed logs to the console.")
    
    return parser

def main():
    parser = setup_argparse()
    args = parser.parse_args()

    # --- EXTRACT & TRANSFORM ---
    if args.verbose:
        print(f"[*] Reading JSON data from {args.input}...")
    
    try:
        contacts = load_json_contacts(args.input)
    except FileNotFoundError:
        print(f"[!] Error: The input file {args.input} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading JSON: {e}")
        sys.exit(1)

    # Optional Sorting
    if args.sort_by:
        if args.verbose:
            print(f"[*] Sorting records by {args.sort_by}...")
        
        if args.sort_by == "next_follow_up":
            # Sort missing dates to the end
            contacts.sort(key=lambda c: c.next_follow_up or "9999-12-31")
        elif args.sort_by == "name":
            contacts.sort(key=lambda c: c.name.lower())
        elif args.sort_by == "priority":
            priority_map = {"High": 1, "Medium": 2, "Low": 3}
            contacts.sort(key=lambda c: priority_map.get(c.priority, 4))

    # --- LOAD (Write to CSV) ---
    if args.verbose:
        print(f"[*] Exporting flattened data to {args.output}...")
    export_to_csv(contacts, args.output, args.delimiter)

    # --- PROCESS & ANALYZE ---
    if args.verbose:
        print("[*] Reading generated CSV for analysis...")
    
    csv_data = read_csv_data(args.output, args.delimiter)
    metrics = analyze_contacts(csv_data)

    # --- OUTPUT RESULTS ---
    print("\n" + "="*40)
    print("📊 OUTREACH PIPELINE METRICS 📊")
    print("="*40)
    print(f"Total Contacts Processed:  {metrics['total_contacts']}")
    print(f"Overdue Follow-ups:        {metrics['overdue_follow_ups']}")
    print(f"Incomplete Records:        {metrics['records_missing_critical_data']}")
    
    print("\n--- Top Lead Sources ---")
    for source, count in metrics["source_distribution"].items():
        print(f"  • {source}: {count}")
        
    print("\n--- Pipeline Status ---")
    for status, count in metrics["status_distribution"].items():
        print(f"  • {status}: {count}")
    print("="*40 + "\n")

    if args.analysis_output:
        if args.verbose:
            print(f"[*] Saving analysis metrics to {args.analysis_output}...")
        export_analysis(metrics, args.analysis_output)
        print(f"[+] Analysis successfully saved to {args.analysis_output}.")

if __name__ == "__main__":
    main()
