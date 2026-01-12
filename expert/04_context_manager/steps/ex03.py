#!/usr/bin/env python3
"""
Context Manager Script
Custom context manager implementations using both class-based and decorator approaches.
"""

import time
from contextlib import contextmanager
from typing import Any, Optional
import os

class Timer:
    """Context manager to measure execution time."""
    
    def __init__(self, name: str = "Operation"):
        """
        Initialize timer.
        
        Args:
            name: Name of operation being timed
        """
        self.name = name
        self.start_time = None
        self.elapsed = None
    
    def __enter__(self):
        """Start timing."""
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop timing and report.
        
        Args:
            exc_type: Exception type if raised
            exc_val: Exception value if raised
            exc_tb: Exception traceback if raised
        
        Returns:
            False to propagate exceptions
        """
        self.elapsed = time.time() - self.start_time
        print(f"{self.name} took {self.elapsed:.4f} seconds")
        return False

class FileManager:
    """Context manager for safe file operations."""
    
    def __init__(self, filename: str, mode: str = 'r'):
        """
        Initialize file manager.
        
        Args:
            filename: Path to file
            mode: File open mode
        """
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Open file."""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close file."""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        return False

class DatabaseConnection:
    """Context manager simulating database connection."""
    
    def __init__(self, db_name: str):
        """
        Initialize connection.
        
        Args:
            db_name: Database name
        """
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        """Establish connection."""
        print(f"Connecting to {self.db_name}...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection and handle transactions."""
        if exc_type is None:
            print(f"Committing transaction to {self.db_name}")
        else:
            print(f"Rolling back transaction to {self.db_name}")
        
        print(f"Closing connection to {self.db_name}")
        self.connected = False
        return False
    
    def execute(self, query: str):
        """Execute a query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing: {query}")
        return f"Result for: {query}"

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
