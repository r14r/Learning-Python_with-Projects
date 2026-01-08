# Pflichtenheft: TODO List App

## Expected Functionality
A command-line TODO list manager with persistent JSON storage. Features include adding tasks with priorities, marking as complete, deleting tasks, and searching by keyword.

## Input
- **Class initialization**: `filename` (str) - JSON file for storage
- **Method parameters**:
  - `task` (str): Task description
  - `priority` (str): Priority level (low, medium, high)
  - `task_id` (int): Task identifier
  - `keyword` (str): Search term
  - `show_completed` (bool): Whether to show completed tasks

## Expected Output
```
TODO List App Demo

Adding tasks...

All tasks:
  ○ [1] Buy groceries (Priority: high)
  ○ [2] Write report (Priority: medium)
  ○ [3] Call dentist (Priority: low)

Completing task 1...

Remaining tasks:
  ○ [2] Write report (Priority: medium)
  ○ [3] Call dentist (Priority: low)

Searching for 'report':
  Found: Write report
```

## Tests

### Test 1: Add Task
**Input:** `todo_list.add("Test task", "high")`  
**Expected Output:** Task ID (integer)

### Test 2: List Tasks
**Input:** `todo_list.list(show_completed=False)`  
**Expected Output:** List of incomplete tasks

### Test 3: Complete Task
**Input:** `todo_list.complete(1)`  
**Expected Output:** `True` (success)

### Test 4: Delete Task
**Input:** `todo_list.delete(1)`  
**Expected Output:** `True` (success)

### Test 5: Search Tasks
**Input:** `todo_list.find("groceries")`  
**Expected Output:** List of tasks containing "groceries"

### Test 6: Persistence
**Input:** Create TodoList, add task, create new TodoList with same file  
**Expected Output:** Second instance loads the saved task

## Dependencies
- Standard library only (json, os, datetime)

## Usage
```bash
python script.py
```
