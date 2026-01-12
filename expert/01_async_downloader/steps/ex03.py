#!/usr/bin/env python3
"""
Async Downloader Script
Asynchronous file downloader using asyncio and aiohttp.
"""

import asyncio
import aiohttp
from pathlib import Path
from typing import List, Dict
import time

async def download_file(session: aiohttp.ClientSession, url: str, destination: str) -> Dict:
    """
    Download a single file asynchronously.
    
    Args:
        session: aiohttp session
        url: URL to download
        destination: Local file path
    
    Returns:
        dict: Download result with status and info
    """
    start_time = time.time()
    
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                content = await response.read()
                
                # Write to file
                Path(destination).parent.mkdir(parents=True, exist_ok=True)
                with open(destination, 'wb') as f:
                    f.write(content)
                
                elapsed = time.time() - start_time
                return {
                    'url': url,
                    'destination': destination,
                    'status': 'success',
                    'size': len(content),
                    'time': elapsed
                }
            else:
                return {
                    'url': url,
                    'status': 'error',
                    'error': f'HTTP {response.status}'
                }
    except Exception as e:
        return {
            'url': url,
            'status': 'error',
            'error': str(e)
        }

async def download_multiple(urls: List[str], output_dir: str = '/tmp/downloads') -> List[Dict]:
    """
    Download multiple files concurrently.
    
    Args:
        urls: List of URLs to download
        output_dir: Directory to save files
    
    Returns:
        List[Dict]: Results for each download
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for i, url in enumerate(urls):
            filename = f"file_{i}_{Path(url).name}"
            destination = f"{output_dir}/{filename}"
            tasks.append(download_file(session, url, destination))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

def main():
    try:
        print(download_multiple([]))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
