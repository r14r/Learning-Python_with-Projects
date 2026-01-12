#!/usr/bin/env python3
"""
File Organizer Script
Organizes files by type, date, or other criteria.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List

def organize_by_extension(source_dir: str, create_folders: bool = True) -> Dict[str, List[str]]:
    """
    Organize files by their extension.
    
    Args:
        source_dir (str): Directory containing files to organize
        create_folders (bool): Whether to create folders and move files
    
    Returns:
        dict: Dictionary mapping extensions to file lists
    """
    files_by_ext = {}
    source_path = Path(source_dir)
    
    if not source_path.exists():
        return {"error": "Directory does not exist"}
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lower() or '.no_extension'
            
            if ext not in files_by_ext:
                files_by_ext[ext] = []
            
            files_by_ext[ext].append(file_path.name)
            
            if create_folders:
                # Create folder for extension
                ext_folder = source_path / ext.lstrip('.')
                ext_folder.mkdir(exist_ok=True)
                
                # Move file to folder
                dest_path = ext_folder / file_path.name
                if not dest_path.exists():
                    shutil.move(str(file_path), str(dest_path))
    
    return files_by_ext

def organize_by_date(source_dir: str, date_format: str = "%Y-%m") -> Dict[str, List[str]]:
    """
    Organize files by modification date.
    
    Args:
        source_dir (str): Directory containing files
        date_format (str): Date format for folder names (default: YYYY-MM)
    
    Returns:
        dict: Dictionary mapping dates to file lists
    """
    files_by_date = {}
    source_path = Path(source_dir)
    
    if not source_path.exists():
        return {"error": "Directory does not exist"}
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            # Get modification time
            mtime = file_path.stat().st_mtime
            date_str = datetime.fromtimestamp(mtime).strftime(date_format)
            
            if date_str not in files_by_date:
                files_by_date[date_str] = []
            
            files_by_date[date_str].append(file_path.name)
    
    return files_by_date

def main():
    try:
        print(organize_by_extension("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
