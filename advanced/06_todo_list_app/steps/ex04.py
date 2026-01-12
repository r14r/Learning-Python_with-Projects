#!/usr/bin/env python3
"""
TODO List App Script
A command-line TODO list manager with persistent storage.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class TodoList:
    """Simple TODO list manager."""
    
    def __init__(self, filename: str = "todos.json"):
        """
        Initialize TODO list.
        
        Args:
            filename (str): File to store TODOs
        """
        self.filename = filename
        self.todos = self.load()
    
    def load(self) -> List[Dict]:
        """Load TODOs from file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save(self):
        """Save TODOs to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add(self, task: str, priority: str = "medium") -> int:
        """
        Add a new task.
        
        Args:
            task (str): Task description
            priority (str): Priority level (low, medium, high)
        
        Returns:
            int: Task ID
        """
        task_id = len(self.todos) + 1
        todo = {
            'id': task_id,
            'task': task,
            'priority': priority,
            'completed': False,
            'created': datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save()
        return task_id
    
    def list(self, show_completed: bool = True) -> List[Dict]:
        """
        List all tasks.
        
        Args:
            show_completed (bool): Whether to show completed tasks
        
        Returns:
            List[Dict]: List of tasks
        """
        if show_completed:
            return self.todos
        return [t for t in self.todos if not t['completed']]
    
    def complete(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id (int): Task ID
        
        Returns:
            bool: Success status
        """
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().isoformat()
                self.save()
                return True
        return False
    
    def delete(self, task_id: int) -> bool:
        """
        Delete a task.
        
        Args:
            task_id (int): Task ID
        
        Returns:
            bool: Success status
        """
        original_length = len(self.todos)
        self.todos = [t for t in self.todos if t['id'] != task_id]
        if len(self.todos) < original_length:
            self.save()
            return True
        return False
    
    def find(self, keyword: str) -> List[Dict]:
        """
        Search for tasks containing keyword.
        
        Args:
            keyword (str): Search keyword
        
        Returns:
            List[Dict]: Matching tasks
        """
        return [t for t in self.todos if keyword.lower() in t['task'].lower()]


def main():
    """Main function to demonstrate TODO list."""
    print("TODO List App Demo")
    
    # Use a temporary file for demo
    todo_list = TodoList("/tmp/demo_todos.json")
    
    # Add tasks
    print("\nAdding tasks...")
    todo_list.add("Buy groceries", "high")
    todo_list.add("Write report", "medium")
    todo_list.add("Call dentist", "low")
    
    # List tasks
    print("\nAll tasks:")
    for todo in todo_list.list(show_completed=False):
        status = "✓" if todo['completed'] else "○"
        print(f"  {status} [{todo['id']}] {todo['task']} (Priority: {todo['priority']})")
    
    # Complete a task
    print("\nCompleting task 1...")
    todo_list.complete(1)
    
    # List again
    print("\nRemaining tasks:")
    for todo in todo_list.list(show_completed=False):
        status = "✓" if todo['completed'] else "○"
        print(f"  {status} [{todo['id']}] {todo['task']} (Priority: {todo['priority']})")
    
    # Search
    print("\nSearching for 'report':")
    results = todo_list.find("report")
    for todo in results:
        print(f"  Found: {todo['task']}")
    
    # Cleanup
    if os.path.exists("/tmp/demo_todos.json"):
        os.remove("/tmp/demo_todos.json")


if __name__ == "__main__":
    main()
