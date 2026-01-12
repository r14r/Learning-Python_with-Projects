#!/usr/bin/env python3
"""
CSV Processor Script
Process and transform CSV data files.
"""

import csv
from typing import List, Dict, Optional
from io import StringIO

def read_csv(filename: str, has_header: bool = True) -> List[Dict]:
    """
    Read CSV file and return as list of dictionaries.
    
    Args:
        filename (str): Path to CSV file
        has_header (bool): Whether CSV has header row
    
    Returns:
        List[Dict]: List of rows as dictionaries
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            if has_header:
                reader = csv.DictReader(f)
                return list(reader)
            else:
                reader = csv.reader(f)
                return [{'col' + str(i): val for i, val in enumerate(row)} 
                        for row in reader]
    except FileNotFoundError:
        return []

def write_csv(filename: str, data: List[Dict], fieldnames: Optional[List[str]] = None):
    """
    Write data to CSV file.
    
    Args:
        filename (str): Output file path
        data (List[Dict]): Data to write
        fieldnames (List[str]): Column names (auto-detected if None)
    """
    if not data:
        return
    
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def filter_csv(data: List[Dict], column: str, value: str) -> List[Dict]:
    """
    Filter CSV data by column value.
    
    Args:
        data (List[Dict]): Input data
        column (str): Column name to filter on
        value (str): Value to match
    
    Returns:
        List[Dict]: Filtered data
    """
    return [row for row in data if row.get(column) == value]

def main():
    try:
        print(read_csv("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
