#!/usr/bin/env python3
"""
Data Analyzer Script
Performs data analysis using pandas.
"""

import pandas as pd
import statistics
from typing import Dict, List

def create_sample_dataframe() -> pd.DataFrame:
    """Create a sample DataFrame for analysis."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'salary': [50000, 60000, 75000, 55000, 70000],
        'department': ['IT', 'HR', 'IT', 'Finance', 'IT']
    }
    return pd.DataFrame(data)

def basic_statistics(df: pd.DataFrame, column: str) -> Dict:
    """
    Calculate basic statistics for a column.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column (str): Column name
    
    Returns:
        dict: Statistics including mean, median, std, min, max
    """
    if column not in df.columns:
        return {"error": f"Column {column} not found"}
    
    data = df[column].dropna()
    
    return {
        'mean': float(data.mean()),
        'median': float(data.median()),
        'std': float(data.std()),
        'min': float(data.min()),
        'max': float(data.max()),
        'count': int(data.count())
    }

def main():
    try:
        print(create_sample_dataframe())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
