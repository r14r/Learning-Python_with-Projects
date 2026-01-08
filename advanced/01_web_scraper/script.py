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


def extract_headings(html: str) -> Dict[str, List[str]]:
    """
    Extract all headings from HTML content.
    
    Args:
        html (str): HTML content
    
    Returns:
        Dict[str, List[str]]: Headings grouped by level (h1, h2, etc.)
    """
    soup = BeautifulSoup(html, 'html.parser')
    headings = {}
    
    for level in range(1, 7):
        tag = f'h{level}'
        headings[tag] = [h.get_text(strip=True) for h in soup.find_all(tag)]
    
    return headings


def main():
    """Main function to demonstrate web scraping."""
    # Example with a simple HTML string
    sample_html = """
    <html>
        <head><title>Sample Page</title></head>
        <body>
            <h1>Main Title</h1>
            <h2>Subtitle 1</h2>
            <p>Some content here.</p>
            <h2>Subtitle 2</h2>
            <a href="https://example.com">Link 1</a>
            <a href="/page2">Link 2</a>
        </body>
    </html>
    """
    
    print("Web Scraper Demo")
    print("\nExtracting headings:")
    headings = extract_headings(sample_html)
    for level, texts in headings.items():
        if texts:
            print(f"{level}: {texts}")
    
    print("\nExtracting links:")
    links = extract_links(sample_html, "https://example.com")
    for link in links:
        print(f"  - {link}")


if __name__ == "__main__":
    main()
