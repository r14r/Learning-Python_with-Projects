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


def aggregate_csv(data: List[Dict], group_by: str, agg_column: str) -> Dict[str, float]:
    """
    Aggregate CSV data by grouping.
    
    Args:
        data (List[Dict]): Input data
        group_by (str): Column to group by
        agg_column (str): Column to sum
    
    Returns:
        Dict[str, float]: Aggregated results
    """
    results = {}
    for row in data:
        key = row.get(group_by, 'Unknown')
        try:
            value = float(row.get(agg_column, 0))
            results[key] = results.get(key, 0) + value
        except ValueError:
            continue
    return results


def transform_column(data: List[Dict], column: str, func) -> List[Dict]:
    """
    Transform a column using a function.
    
    Args:
        data (List[Dict]): Input data
        column (str): Column to transform
        func: Transformation function
    
    Returns:
        List[Dict]: Transformed data
    """
    result = []
    for row in data.copy():
        new_row = row.copy()
        if column in new_row:
            new_row[column] = func(new_row[column])
        result.append(new_row)
    return result


def main():
    """Main function to demonstrate CSV processing."""
    print("CSV Processor Demo")
    
    # Create sample CSV data
    sample_data = [
        {'name': 'Alice', 'department': 'IT', 'salary': '50000'},
        {'name': 'Bob', 'department': 'HR', 'salary': '60000'},
        {'name': 'Charlie', 'department': 'IT', 'salary': '75000'},
        {'name': 'David', 'department': 'Finance', 'salary': '55000'},
    ]
    
    # Write to file
    temp_file = "/tmp/sample.csv"
    write_csv(temp_file, sample_data)
    print(f"\nCreated sample CSV: {temp_file}")
    
    # Read back
    data = read_csv(temp_file)
    print(f"\nRead {len(data)} rows")
    
    # Filter
    it_dept = filter_csv(data, 'department', 'IT')
    print(f"\nIT department employees: {len(it_dept)}")
    for emp in it_dept:
        print(f"  - {emp['name']}")
    
    # Aggregate
    dept_totals = aggregate_csv(data, 'department', 'salary')
    print("\nTotal salary by department:")
    for dept, total in dept_totals.items():
        print(f"  {dept}: ${total:,.0f}")
    
    # Transform
    transformed = transform_column(data, 'name', str.upper)
    print("\nTransformed names:")
    for row in transformed:
        print(f"  {row['name']}")


if __name__ == "__main__":
    main()
