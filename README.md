# File Organizer

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/file-organizer-cli.svg)](https://pypi.org/project/file-organizer-cli/)
[![Tests](https://github.com/StencilwashCoder/file-organizer/workflows/Tests/badge.svg)](https://github.com/StencilwashCoder/file-organizer/actions)

A powerful, yet simple CLI tool to automatically organize your files. Clean up your Downloads folder, Desktop, or any messy directory in seconds!

## ✨ Features

- 📁 **Smart Organization** - Sort files by type, date, or size
- 🗂️ **Category Detection** - Automatically categorizes files (Images, Documents, Videos, etc.)
- 🔒 **Safe Operations** - Dry-run mode to preview changes before executing
- 🔄 **Undo Support** - Made a mistake? Undo your last organization
- ⚡ **Fast & Efficient** - Handles thousands of files in seconds
- 🎯 **Custom Rules** - Define your own organization rules with YAML config

## 🚀 Installation

```bash
# Install from PyPI (when published)
pip install file-organizer-cli

# Or install from source
git clone https://github.com/StencilwashCoder/file-organizer.git
cd file-organizer
pip install -e .
```

## 📖 Quick Start

```bash
# Organize current directory by file type
file-organizer organize

# Organize specific directory
file-organizer organize ~/Downloads

# Organize by date created
file-organizer organize ~/Pictures --by-date

# Preview changes without moving files (dry run)
file-organizer organize ~/Desktop --dry-run

# Undo last organization
file-organizer undo
```

## 📂 Default Categories

| Category | Extensions |
|----------|------------|
| 📸 Images | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp |
| 🎬 Videos | .mp4, .avi, .mkv, .mov, .wmv, .flv |
| 🎵 Audio | .mp3, .wav, .flac, .aac, .ogg, .m4a |
| 📄 Documents | .pdf, .doc, .docx, .txt, .rtf, .odt |
| 📊 Spreadsheets | .xls, .xlsx, .csv, .ods |
| 📈 Presentations | .ppt, .pptx, .odp, .key |
| 📦 Archives | .zip, .rar, .7z, .tar, .gz, .bz2 |
| 💻 Code | .py, .js, .html, .css, .java, .cpp, .c |
| 🎮 Executables | .exe, .msi, .dmg, .pkg, .appimage |

## 🔧 Configuration

Create a `~/.file-organizer.yml` for custom rules:

```yaml
# Custom categories
categories:
  Work:
    - .docx
    - .xlsx
    - .pptx
  Personal:
    - .jpg
    - .mp4
    - .mp3

# Exclude patterns
exclude:
  - "*.tmp"
  - "*.log"
  - ".git"
  - "node_modules"

# Destination paths
destinations:
  Images: ~/Pictures/Organized
  Documents: ~/Documents/Organized
  Videos: ~/Videos/Organized
```

## 🖥️ Usage Examples

### Basic Organization
```bash
# Organize Downloads folder
file-organizer organize ~/Downloads

# Output:
# 📁 Organizing /home/user/Downloads...
# ✅ Moved 15 files to Images/
# ✅ Moved 8 files to Documents/
# ✅ Moved 3 files to Archives/
# 🎉 Organization complete! 26 files organized.
```

### Organize by Date
```bash
file-organizer organize ~/Pictures --by-date
# Creates folders like: 2024/01, 2024/02, etc.
```

### Dry Run (Preview)
```bash
file-organizer organize ~/Desktop --dry-run
# Shows what would happen without moving files
```

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- Inspired by the need to clean up messy Downloads folders everywhere
- Built with ❤️ by [StencilwashCoder](https://github.com/StencilwashCoder)

---

💡 **Pro Tip**: Add `file-organizer organize ~/Downloads` to your crontab for automatic cleanup!
