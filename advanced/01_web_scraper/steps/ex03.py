#!/usr/bin/env python3
"""
Web Scraper Script
Scrapes data from web pages using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def fetch_page(url: str) -> str:
    """
    Fetch HTML content from a URL.
    
    Args:
        url (str): The URL to fetch
    
    Returns:
        str: HTML content or empty string on error
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_links(html: str, base_url: str = "") -> List[str]:
    """
    Extract all links from HTML content.
    
    Args:
        html (str): HTML content
        base_url (str): Base URL for relative links
    
    Returns:
        List[str]: List of URLs
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):
            links.append(href)
        elif base_url and href.startswith('/'):
            links.append(base_url + href)
    
    return links

def main():
    try:
        print(fetch_page("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
