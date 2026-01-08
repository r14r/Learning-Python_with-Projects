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


def group_analysis(df: pd.DataFrame, group_by: str, agg_column: str) -> pd.DataFrame:
    """
    Perform group-based analysis.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        group_by (str): Column to group by
        agg_column (str): Column to aggregate
    
    Returns:
        pd.DataFrame: Grouped statistics
    """
    return df.groupby(group_by)[agg_column].agg(['mean', 'sum', 'count'])


def filter_data(df: pd.DataFrame, column: str, operator: str, value) -> pd.DataFrame:
    """
    Filter DataFrame based on condition.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column (str): Column to filter on
        operator (str): Operator ('>', '<', '==', '>=', '<=')
        value: Value to compare against
    
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    if operator == '>':
        return df[df[column] > value]
    elif operator == '<':
        return df[df[column] < value]
    elif operator == '==':
        return df[df[column] == value]
    elif operator == '>=':
        return df[df[column] >= value]
    elif operator == '<=':
        return df[df[column] <= value]
    else:
        return df


def main():
    """Main function to demonstrate data analysis."""
    print("Data Analyzer Demo")
    
    # Create sample data
    df = create_sample_dataframe()
    print("\nSample Data:")
    print(df)
    
    # Basic statistics
    print("\nSalary Statistics:")
    stats = basic_statistics(df, 'salary')
    for key, value in stats.items():
        print(f"  {key}: {value:,.2f}" if isinstance(value, float) else f"  {key}: {value}")
    
    # Group analysis
    print("\nDepartment Analysis:")
    grouped = group_analysis(df, 'department', 'salary')
    print(grouped)
    
    # Filtering
    print("\nEmployees with salary > 60000:")
    filtered = filter_data(df, 'salary', '>', 60000)
    print(filtered[['name', 'salary']])


if __name__ == "__main__":
    main()
