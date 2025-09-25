"""
CSV File Analyzer CLI Tool
This script reads a CSV file, displays its summary statistics,
and saves the summary to a JSON file.
Usage: python csv_cli_tool.py <input_csv> <output_json>
"""

import pandas as pd  # Data manipulation library
import json  # JSON handling library
import argparse  # Command-line argument parsing library

# Command-line argument parsing
parser = argparse.ArgumentParser(description="CSV File Analyzer")
parser.add_argument(
    "input_csv", type=str, help="Path to the CSV file"
)  # Input CSV file path
parser.add_argument(
    "output_json", type=str, help="Path to save the JSON summary"
)  # Output JSON file path
args = parser.parse_args()  # Parse arguments

# Load CSV and display summary
df = pd.read_csv(args.input_csv)  # Read CSV file
print(df.head())  # Display first few rows

# Summary statistics
print(
    f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}"
)  # Print total rows and columns
print(f"\nColumns: {df.columns.tolist()}")  # Print column names
print(
    f"\nNumerical Columns: {df.select_dtypes(include=['number']).columns.tolist()}"
)  # Print numerical columns
print(
    f"\nCategorical Columns: {df.select_dtypes(include=['object']).columns.tolist()}"
)  # Print categorical columns

# Save summary to JSON
with open(args.output_json, "w") as f:  # Open output file
    json.dump(
        {
            "Total Rows": len(df),
            "Total Columns": len(df.columns),
            "Columns": df.columns.tolist(),
            "Numerical Columns": df.select_dtypes(include=["number"]).columns.tolist(),
            "Categorical Columns": df.select_dtypes(
                include=["object"]
            ).columns.tolist(),
        },
        f,
        indent=4,
    )  # Write summary to JSON file
