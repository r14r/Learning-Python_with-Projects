#!/usr/bin/env python3
"""
API Client Script
Interacts with REST APIs to fetch and manipulate data.
"""

import requests
import json
from typing import Dict, List, Optional


class APIClient:
    """Simple REST API client."""
    
    def __init__(self, base_url: str):
        """
        Initialize API client.
        
        Args:
            base_url (str): Base URL for the API
        """
        self.base_url = base_url.rstrip('/')
        self.headers = {'Content-Type': 'application/json'}
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request.
        
        Args:
            endpoint (str): API endpoint
            params (dict): Query parameters
        
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def post(self, endpoint: str, data: Dict) -> Dict:
        """
        Make a POST request.
        
        Args:
            endpoint (str): API endpoint
            data (dict): Data to send
        
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def put(self, endpoint: str, data: Dict) -> Dict:
        """
        Make a PUT request.
        
        Args:
            endpoint (str): API endpoint
            data (dict): Data to send
        
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.put(url, json=data, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
    
    def delete(self, endpoint: str) -> Dict:
        """
        Make a DELETE request.
        
        Args:
            endpoint (str): API endpoint
        
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.delete(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json() if response.text else {"success": True}
        except requests.RequestException as e:
            return {"error": str(e)}


def main():
    """Main function to demonstrate API client."""
    # Using JSONPlaceholder as a demo API
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    print("API Client Demo")
    
    # GET example
    print("\n1. Fetching a post:")
    post = client.get("posts/1")
    print(f"Title: {post.get('title', 'N/A')}")
    
    # POST example
    print("\n2. Creating a new post:")
    new_post = {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    }
    created = client.post("posts", new_post)
    print(f"Created post ID: {created.get('id', 'N/A')}")
    
    # GET with parameters
    print("\n3. Fetching posts by user:")
    posts = client.get("posts", params={"userId": 1})
    print(f"Found {len(posts)} posts" if isinstance(posts, list) else "Error")


if __name__ == "__main__":
    main()
