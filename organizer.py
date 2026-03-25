#!/usr/bin/env python3
"""
File Organizer - A CLI tool to automatically organize files in directories.
"""

import os
import shutil
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import yaml

# Default file categories
DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".tsv"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".php", ".rb", ".go", ".rs"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".appimage", ".deb", ".rpm"],
}

CONFIG_FILE = Path.home() / ".file-organizer.yml"
HISTORY_FILE = Path.home() / ".file-organizer-history.json"


def load_config():
    """Load user configuration if it exists."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return yaml.safe_load(f) or {}
    return {}


def save_history(operations):
    """Save operation history for undo functionality."""
    history = []
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    
    history.append({
        "timestamp": datetime.now().isoformat(),
        "operations": operations
    })
    
    # Keep only last 10 operations
    history = history[-10:]
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)


def get_category(filename, categories):
    """Determine the category of a file based on its extension."""
    ext = Path(filename).suffix.lower()
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return "Others"


def organize_by_type(directory, dry_run=False, config=None):
    """Organize files by their type/category."""
    directory = Path(directory).expanduser().resolve()
    
    if not directory.exists():
        print(f"❌ Directory does not exist: {directory}")
        return
    
    categories = config.get('categories', DEFAULT_CATEGORIES) if config else DEFAULT_CATEGORIES
    exclude_patterns = config.get('exclude', []) if config else []
    
    operations = []
    stats = defaultdict(int)
    
    print(f"📁 {'[DRY RUN] ' if dry_run else ''}Organizing {directory}...\n")
    
    for item in directory.iterdir():
        if item.is_file():
            # Check exclude patterns
            if any(item.match(pattern) for pattern in exclude_patterns):
                continue
            
            category = get_category(item.name, categories)
            target_dir = directory / category
            target_path = target_dir / item.name
            
            # Handle duplicates
            counter = 1
            original_target = target_path
            while target_path.exists() and not dry_run:
                stem = original_target.stem
                suffix = original_target.suffix
                target_path = target_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            if not dry_run:
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(target_path))
                operations.append({
                    "source": str(item),
                    "destination": str(target_path)
                })
            
            stats[category] += 1
            print(f"  {'[WOULD MOVE]' if dry_run else '✅'} {item.name} → {category}/")
    
    if not dry_run and operations:
        save_history(operations)
    
    print(f"\n{'─' * 50}")
    print(f"📊 Summary:")
    for category, count in sorted(stats.items()):
        print(f"   {category}: {count} file(s)")
    print(f"{'─' * 50}")
    print(f"🎉 {'Would organize' if dry_run else 'Organized'} {sum(stats.values())} files!\n")


def organize_by_date(directory, dry_run=False, config=None):
    """Organize files by their creation/modification date."""
    directory = Path(directory).expanduser().resolve()
    
    if not directory.exists():
        print(f"❌ Directory does not exist: {directory}")
        return
    
    exclude_patterns = config.get('exclude', []) if config else []
    operations = []
    stats = defaultdict(int)
    
    print(f"📁 {'[DRY RUN] ' if dry_run else ''}Organizing by date: {directory}...\n")
    
    for item in directory.iterdir():
        if item.is_file():
            if any(item.match(pattern) for pattern in exclude_patterns):
                continue
            
            # Get file modification time
            mtime = datetime.fromtimestamp(item.stat().st_mtime)
            date_folder = f"{mtime.year}/{mtime.month:02d}"
            target_dir = directory / date_folder
            target_path = target_dir / item.name
            
            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(target_path))
                operations.append({
                    "source": str(item),
                    "destination": str(target_path)
                })
            
            stats[date_folder] += 1
            print(f"  {'[WOULD MOVE]' if dry_run else '✅'} {item.name} → {date_folder}/")
    
    if not dry_run and operations:
        save_history(operations)
    
    print(f"\n{'─' * 50}")
    print(f"📊 Summary:")
    for date_folder, count in sorted(stats.items()):
        print(f"   {date_folder}: {count} file(s)")
    print(f"{'─' * 50}")
    print(f"🎉 {'Would organize' if dry_run else 'Organized'} {sum(stats.values())} files by date!\n")


def undo_last():
    """Undo the last organization operation."""
    if not HISTORY_FILE.exists():
        print("❌ No history found. Nothing to undo.")
        return
    
    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
    
    if not history:
        print("❌ No operations in history.")
        return
    
    last_operation = history.pop()
    operations = last_operation['operations']
    
    print(f"🔄 Undoing last operation from {last_operation['timestamp']}...\n")
    
    undone = 0
    for op in reversed(operations):
        source = Path(op['destination'])
        dest = Path(op['source'])
        
        if source.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(dest))
            print(f"  ↩️  {source.name} → {dest.parent}")
            undone += 1
        else:
            print(f"  ⚠️  Skipped (not found): {source}")
    
    # Save updated history
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)
    
    print(f"\n✅ Undone {undone} file move(s)!\n")


def main():
    parser = argparse.ArgumentParser(
        description="File Organizer - Automatically organize your files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  file-organizer organize ~/Downloads          # Organize Downloads folder
  file-organizer organize ~/Pictures --by-date # Organize by date
  file-organizer organize . --dry-run          # Preview changes
  file-organizer undo                          # Undo last operation
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Organize command
    org_parser = subparsers.add_parser('organize', help='Organize files in a directory')
    org_parser.add_argument('directory', nargs='?', default='.', help='Directory to organize (default: current)')
    org_parser.add_argument('--by-date', action='store_true', help='Organize by date instead of type')
    org_parser.add_argument('--dry-run', action='store_true', help='Preview changes without moving files')
    
    # Undo command
    subparsers.add_parser('undo', help='Undo the last organization operation')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    config = load_config()
    
    if args.command == 'organize':
        if args.by_date:
            organize_by_date(args.directory, args.dry_run, config)
        else:
            organize_by_type(args.directory, args.dry_run, config)
    elif args.command == 'undo':
        undo_last()


if __name__ == '__main__':
    main()
