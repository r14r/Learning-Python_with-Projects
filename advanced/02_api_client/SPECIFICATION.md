# Pflichtenheft: API Client

## Expected Functionality
A REST API client class that handles HTTP requests (GET, POST, PUT, DELETE) with proper error handling. Demonstrates interaction with a public API (JSONPlaceholder).

## Input
- **Class initialization**: `base_url` (str) - Base URL of the API
- **Method parameters**:
  - `endpoint` (str): API endpoint path
  - `params` (dict, optional): Query parameters for GET
  - `data` (dict): Request body for POST/PUT

## Expected Output
```
API Client Demo

1. Fetching a post:
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

2. Creating a new post:
Created post ID: 101

3. Fetching posts by user:
Found 10 posts
```

## Tests

### Test 1: GET Request
**Input:** `client.get("posts/1")`  
**Expected Output:** Dictionary with post data including 'id', 'title', 'body'

### Test 2: POST Request
**Input:** `client.post("posts", {"title": "Test", "body": "Content", "userId": 1})`  
**Expected Output:** Dictionary with created resource including 'id'

### Test 3: PUT Request
**Input:** `client.put("posts/1", {"title": "Updated"})`  
**Expected Output:** Dictionary with updated data

### Test 4: DELETE Request
**Input:** `client.delete("posts/1")`  
**Expected Output:** Dictionary indicating success

### Test 5: Error Handling
**Input:** `client.get("invalid-endpoint")`  
**Expected Output:** Dictionary with 'error' key

## Dependencies
```
requests
```

## Usage
```bash
pip install requests
python script.py
```
