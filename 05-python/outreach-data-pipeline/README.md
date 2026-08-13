# Data Pipeline: Micro-CRM Outreach Tracker

A comprehensive Python data pipeline that extracts nested JSON contact data, flattens and validates it, loads it into a clean CSV format, and performs automated metric analysis. 

## Overview

While interactive scripts are useful for manual entry, enterprise environments require automated data processing. This project demonstrates a core **ETL (Extract, Transform, Load)** workflow. 

By flattening complex hierarchical JSON data into a strictly structured CSV, the output becomes instantly ingestible by BI (Business Intelligence) tools like Power BI or Tableau for quantitative analysis and dashboarding. It is highly optimized for tracking automated outreach campaigns (e.g., via LinkedIn Sales Navigator).

## Python Concepts Demonstrated

* **CLI Architecture:** Utilizing `argparse` for flexible command-line arguments and flags.
* **Data Modeling:** Using `dataclasses` to strictly type and enforce structure on raw data.
* **File I/O & Path Management:** Safe reading/writing using Context Managers (`with`) and `pathlib` for OS-agnostic directory handling.
* **Data Flattening:** Converting lists (tags) into delimited strings for flat-file storage.
* **Analytical Processing:** Utilizing `collections.Counter` and `datetime` for fast aggregations and temporal logic (e.g., overdue follow-ups).

## Project Structure

```text
outreach-data-pipeline/
 ┣ data/
 ┃ ┗ contacts.json      # Source data (Nested)
 ┣ models.py            # Dataclass schemas
 ┣ json_to_csv.py       # Extraction and Transformation logic
 ┣ csv_processor.py     # Analytical logic
 ┣ utils.py             # Date parsing and directory management
 ┗ main.py              # Application entry point and CLI router
```

## How to Run It

This project uses the Python Standard Library exclusively. No `pip install` is required.

**Basic Execution:**
```bash
python main.py --input data/contacts.json --output data/contacts.csv
```

**Advanced Execution (Verbose logging, sorting, and exporting analysis):**
```bash
python main.py --input data/contacts.json --output data/contacts.csv --analysis-output data/analysis.csv --sort-by next_follow_up --verbose
```

## Example Output

```plaintext
========================================
OUTREACH PIPELINE METRICS
========================================
Total Contacts Processed:  4
Overdue Follow-ups:        1
Incomplete Records:        0

--- Top Lead Sources ---
  • LinkedIn Sales Navigator: 2
  • Direct Email: 1
  • University Network: 1

--- Pipeline Status ---
  • Meeting Scheduled: 1
  • Follow-up Required: 1
  • Closed: 1
  • Initial Outreach: 1
========================================
```

## Future Improvements & Version Watch

* **v1.1:** Add a SQLite database integration to replace CSV storage for highly scalable querying.
* **v1.2:** Implement an automated daily email summary using the `smtplib` module for overdue follow-ups.

### 3. Detailed Setup Instructions

1. Create the root directory `outreach-data-pipeline/`.
2. Inside, create a `data/` subdirectory and save the `contacts.json` file there.
3. Save all remaining `.py` files and this `README.md` in the root directory.
4. Open your terminal, navigate to the root directory, and run the complete command to see the magic in action:
   ```bash
   python main.py --input data/contacts.json --output data/contacts.csv --analysis-output data/analysis.csv --sort-by priority --verbose
   ```
