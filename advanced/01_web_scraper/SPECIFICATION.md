# Pflichtenheft: Web Scraper

## Expected Functionality
This script demonstrates web scraping techniques using the `requests` library to fetch web pages and `BeautifulSoup` to parse HTML and extract information like links and headings.

## Input
- **Function parameters**:
  - `url` (str): URL to scrape
  - `html` (str): HTML content to parse
  - `base_url` (str): Base URL for resolving relative links

## Expected Output
```
Web Scraper Demo

Extracting headings:
h1: ['Main Title']
h2: ['Subtitle 1', 'Subtitle 2']

Extracting links:
  - https://example.com
  - https://example.com/page2
```

## Tests

### Test 1: Fetch Page Successfully
**Input:** `fetch_page("https://example.com")`  
**Expected Output:** HTML content string (non-empty)

### Test 2: Extract Links - Absolute URLs
**Input:** `extract_links("<a href='https://test.com'>Link</a>")`  
**Expected Output:** `['https://test.com']`

### Test 3: Extract Links - Relative URLs
**Input:** `extract_links("<a href='/page'>Link</a>", "https://test.com")`  
**Expected Output:** `['https://test.com/page']`

### Test 4: Extract Headings
**Input:** `extract_headings("<h1>Title</h1><h2>Sub</h2>")`  
**Expected Output:** `{'h1': ['Title'], 'h2': ['Sub'], ...}`

### Test 5: Handle Empty HTML
**Input:** `extract_links("")`  
**Expected Output:** `[]`

## Dependencies
```
requests
beautifulsoup4
```

## Usage
```bash
pip install requests beautifulsoup4
python script.py
```
