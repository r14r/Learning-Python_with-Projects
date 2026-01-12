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

def get_file_info(file_path: str) -> Dict:
    """
    Get detailed information about a file.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: File information
    """
    path = Path(file_path)
    
    if not path.exists():
        return {"error": "File does not exist"}
    
    stats = path.stat()
    
    return {
        'name': path.name,
        'size': stats.st_size,
        'created': datetime.fromtimestamp(stats.st_ctime).isoformat(),
        'modified': datetime.fromtimestamp(stats.st_mtime).isoformat(),
        'extension': path.suffix,
        'is_file': path.is_file(),
        'is_dir': path.is_dir()
    }

def main():
    """Main function to demonstrate file organization."""
    print("File Organizer Demo")
    
    # Create a temporary test directory
    test_dir = Path("/tmp/file_organizer_test")
    test_dir.mkdir(exist_ok=True)
    
    # Create sample files
    sample_files = [
        "document.txt",
        "image.jpg",
        "script.py",
        "data.csv",
        "photo.jpg"
    ]
    
    for filename in sample_files:
        (test_dir / filename).touch()
    
    print(f"\nCreated test files in {test_dir}")
    
    # Organize by extension (without moving)
    print("\nFiles by extension:")
    files_by_ext = organize_by_extension(str(test_dir), create_folders=False)
    for ext, files in files_by_ext.items():
        print(f"  {ext}: {files}")
    
    # Get file info
    print(f"\nFile info for {sample_files[0]}:")
    info = get_file_info(str(test_dir / sample_files[0]))
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Cleanup
    shutil.rmtree(test_dir)

def main():
    try:
        print(organize_by_extension("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
