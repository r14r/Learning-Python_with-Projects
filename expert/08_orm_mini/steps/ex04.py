#!/usr/bin/env python3
"""
Mini ORM Script
Minimal Object-Relational Mapping implementation.
"""

import sqlite3
from typing import Any, List, Dict, Optional, Type
from dataclasses import dataclass, fields

class Database:
    """Simple database connection manager."""
    
    def __init__(self, db_path: str = ':memory:'):
        """
        Initialize database connection.
        
        Args:
            db_path: Path to database file or :memory:
        """
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
    
    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        Execute SQL query.
        
        Args:
            query: SQL query
            params: Query parameters
        
        Returns:
            Cursor with results
        """
        return self.connection.execute(query, params)
    
    def commit(self):
        """Commit transaction."""
        self.connection.commit()
    
    def close(self):
        """Close database connection."""
        self.connection.close()

class Model:
    """Base class for ORM models."""
    
    _db: Optional[Database] = None
    _table_name: Optional[str] = None
    
    @classmethod
    def set_database(cls, db: Database):
        """Set database connection."""
        cls._db = db
    
    @classmethod
    def table_name(cls) -> str:
        """Get table name."""
        if cls._table_name:
            return cls._table_name
        return cls.__name__.lower()
    
    @classmethod
    def create_table(cls):
        """Create table for this model."""
        if not cls._db:
            raise RuntimeError("Database not set")
        
        # Get field definitions
        field_defs = []
        for field in fields(cls):
            field_type = field.type
            sql_type = cls._python_to_sql_type(field_type)
            field_defs.append(f"{field.name} {sql_type}")
        
        # Add id as primary key
        field_defs.insert(0, "id INTEGER PRIMARY KEY AUTOINCREMENT")
        
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name()} ({', '.join(field_defs)})"
        cls._db.execute(query)
        cls._db.commit()
    
    @staticmethod
    def _python_to_sql_type(python_type) -> str:
        """Map Python types to SQL types."""
        type_map = {
            'int': 'INTEGER',
            'str': 'TEXT',
            'float': 'REAL',
            'bool': 'INTEGER'
        }
        type_name = python_type.__name__ if hasattr(python_type, '__name__') else str(python_type)
        return type_map.get(type_name, 'TEXT')
    
    def save(self) -> int:
        """
        Save model instance to database.
        
        Returns:
            int: ID of saved record
        """
        if not self._db:
            raise RuntimeError("Database not set")
        
        # Get field names and values
        field_names = [f.name for f in fields(self)]
        values = [getattr(self, f.name) for f in fields(self)]
        
        placeholders = ', '.join(['?' for _ in field_names])
        columns = ', '.join(field_names)
        
        query = f"INSERT INTO {self.table_name()} ({columns}) VALUES ({placeholders})"
        cursor = self._db.execute(query, tuple(values))
        self._db.commit()
        
        return cursor.lastrowid
    
    @classmethod
    def find_all(cls) -> List['Model']:
        """
        Find all records.
        
        Returns:
            List of model instances
        """
        if not cls._db:
            raise RuntimeError("Database not set")
        
        query = f"SELECT * FROM {cls.table_name()}"
        cursor = cls._db.execute(query)
        
        results = []
        for row in cursor.fetchall():
            instance = cls._from_row(row)
            results.append(instance)
        
        return results
    
    @classmethod
    def find_by_id(cls, record_id: int) -> Optional['Model']:
        """
        Find record by ID.
        
        Args:
            record_id: Record ID
        
        Returns:
            Model instance or None
        """
        if not cls._db:
            raise RuntimeError("Database not set")
        
        query = f"SELECT * FROM {cls.table_name()} WHERE id = ?"
        cursor = cls._db.execute(query, (record_id,))
        row = cursor.fetchone()
        
        if row:
            return cls._from_row(row)
        return None
    
    @classmethod
    def find_by(cls, **kwargs) -> List['Model']:
        """
        Find records matching criteria.
        
        Args:
            **kwargs: Field-value pairs to match
        
        Returns:
            List of matching instances
        """
        if not cls._db:
            raise RuntimeError("Database not set")
        
        conditions = ' AND '.join([f"{k} = ?" for k in kwargs.keys()])
        values = tuple(kwargs.values())
        
        query = f"SELECT * FROM {cls.table_name()} WHERE {conditions}"
        cursor = cls._db.execute(query, values)
        
        results = []
        for row in cursor.fetchall():
            instance = cls._from_row(row)
            results.append(instance)
        
        return results
    
    @classmethod
    def _from_row(cls, row: sqlite3.Row) -> 'Model':
        """Create instance from database row."""
        kwargs = {f.name: row[f.name] for f in fields(cls)}
        return cls(**kwargs)

class User(Model):
    """Example User model."""
    name: str
    email: str
    age: int

class Post(Model):
    """Example Post model."""
    title: str
    content: str
    user_id: int

def main():
    print("Step 4: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
