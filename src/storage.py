"""
Storage functionality for health check results
"""
import json
from pathlib import Path


def save_results(results, filename='data/monitor_results.json'):
  
    filepath = Path(filename)
    
    # Create directory if it doesn't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing data or start fresh
    if filepath.exists():
        with open(filepath, 'r') as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = []
    else:
        all_data = []
    
    # Append new results
    all_data.extend(results)
    
    # Save back to file
    with open(filepath, 'w') as f:
        json.dump(all_data, f, indent=2)
    
    print(f"💾 Saved {len(results)} results to {filename}")


def load_results(filename='data/monitor_results.json'):
    filepath = Path(filename)
    if not filepath.exists():
        return []
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []