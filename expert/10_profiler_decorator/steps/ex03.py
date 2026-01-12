#!/usr/bin/env python3
"""
Profiler Decorator Script
Performance profiling tool using decorators.
"""

import time
import functools
from typing import Callable, Dict, List
import statistics

class ProfilerStats:
    """Store profiling statistics."""
    
    def __init__(self):
        """Initialize profiler stats."""
        self.calls: Dict[str, List[float]] = {}
        self.memory_usage: Dict[str, List[int]] = {}
    
    def add_call(self, func_name: str, duration: float):
        """
        Record function call duration.
        
        Args:
            func_name: Function name
            duration: Execution time in seconds
        """
        if func_name not in self.calls:
            self.calls[func_name] = []
        self.calls[func_name].append(duration)
    
    def get_stats(self, func_name: str) -> Dict:
        """
        Get statistics for a function.
        
        Args:
            func_name: Function name
        
        Returns:
            dict: Statistics including count, total, average, min, max
        """
        if func_name not in self.calls:
            return {}
        
        durations = self.calls[func_name]
        
        return {
            'count': len(durations),
            'total': sum(durations),
            'average': statistics.mean(durations),
            'median': statistics.median(durations),
            'min': min(durations),
            'max': max(durations),
            'stdev': statistics.stdev(durations) if len(durations) > 1 else 0
        }
    
    def print_report(self):
        """Print profiling report."""
        print("\n" + "=" * 80)
        print("PROFILING REPORT")
        print("=" * 80)
        
        for func_name in sorted(self.calls.keys()):
            stats = self.get_stats(func_name)
            print(f"\nFunction: {func_name}")
            print(f"  Calls:   {stats['count']}")
            print(f"  Total:   {stats['total']:.6f}s")
            print(f"  Average: {stats['average']:.6f}s")
            print(f"  Median:  {stats['median']:.6f}s")
            print(f"  Min:     {stats['min']:.6f}s")
            print(f"  Max:     {stats['max']:.6f}s")
            if stats['stdev'] > 0:
                print(f"  StdDev:  {stats['stdev']:.6f}s")
        
        print("\n" + "=" * 80)

def profile(func: Callable = None, *, name: str = None):
    """
    Decorator to profile function execution.
    
    Args:
        func: Function to profile
        name: Optional custom name for the function
    
    Returns:
        Decorated function
    """
    def decorator(f: Callable) -> Callable:
        func_name = name or f.__name__
        
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = f(*args, **kwargs)
                return result
            finally:
                duration = time.time() - start_time
                profiler.add_call(func_name, duration)
        
        return wrapper
    
    # Allow use as @profile or @profile()
    if func is None:
        return decorator
    else:
        return decorator(func)

def profile_verbose(func: Callable) -> Callable:
    """
    Decorator to profile and print each call.
    
    Args:
        func: Function to profile
    
    Returns:
        Decorated function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[PROFILE] Starting {func.__name__}")
        
        result = func(*args, **kwargs)
        
        duration = time.time() - start_time
        print(f"[PROFILE] {func.__name__} completed in {duration:.6f}s")
        
        profiler.add_call(func.__name__, duration)
        return result
    
    return wrapper

def main():
    try:
        print(profile())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
