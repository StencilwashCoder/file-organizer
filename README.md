# 📁 File Organizer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/pypi/v/file-organizer-cli.svg?style=flat-square&color=blue" alt="PyPI">
  <img src="https://github.com/StencilwashCoder/file-organizer/workflows/CI/badge.svg?style=flat-square" alt="CI">
  <img src="https://img.shields.io/codecov/c/github/stencilwashcoder/file-organizer?style=flat-square" alt="Coverage">
</p>

<p align="center">
  <b>A powerful, yet simple CLI tool to automatically organize your files.</b><br>
  Clean up your Downloads folder, Desktop, or any messy directory in seconds!
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 **Smart Organization** | Sort files by type, date, size, or custom rules |
| 🗂️ **Category Detection** | Automatically categorizes files (Images, Documents, Videos, etc.) |
| 🔒 **Safe Operations** | Dry-run mode to preview changes before executing |
| 🔄 **Undo Support** | Made a mistake? Undo your last organization |
| ⚡ **Fast & Efficient** | Handles thousands of files in seconds |
| 🎯 **Custom Rules** | Define your own organization rules with YAML config |
| 📊 **Progress Tracking** | Visual progress bar for large operations |
| 🔍 **Duplicate Detection** | Find and handle duplicate files |

## 🚀 Installation

### From PyPI (Recommended)

```bash
pip install file-organizer-cli
```

### From Source

```bash
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

# Show help
file-organizer --help
```

## 📂 Default Categories

| Category | Extensions | Icon |
|----------|------------|------|
| 📸 Images | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .ico | 🖼️ |
| 🎬 Videos | .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm | 🎥 |
| 🎵 Audio | .mp3, .wav, .flac, .aac, .ogg, .m4a, .wma | 🎧 |
| 📄 Documents | .pdf, .doc, .docx, .txt, .rtf, .odt, .md | 📄 |
| 📊 Spreadsheets | .xls, .xlsx, .csv, .ods | 📈 |
| 📈 Presentations | .ppt, .pptx, .odp, .key | 🎯 |
| 📦 Archives | .zip, .rar, .7z, .tar, .gz, .bz2, .xz | 📦 |
| 💻 Code | .py, .js, .ts, .html, .css, .java, .cpp, .c, .go, .rs | 💾 |
| 🎮 Executables | .exe, .msi, .dmg, .pkg, .appimage, .deb, .rpm | ⚙️ |
| 🎨 Design | .psd, .ai, .sketch, .fig, .xd | 🎨 |

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

# Exclude patterns (regex supported)
exclude:
  - "^\\."           # Hidden files
  - "node_modules"   # Node modules
  - "__pycache__"    # Python cache

# Organization options
options:
  create_date_folders: true    # Create YYYY/MM folders for date organization
  remove_empty_folders: true   # Clean up empty directories after move
  duplicates_action: ask       # ask | skip | move | delete
```

## 🛠️ Advanced Usage

```bash
# Organize by file size (small/medium/large)
file-organizer organize ~/Downloads --by-size

# Custom output directory
file-organizer organize ~/Messy --output ~/Organized

# Include hidden files
file-organizer organize ~/Project --include-hidden

# Flatten directory structure
file-organizer organize ~/Nested --flatten

# Find duplicates only
file-organizer duplicates ~/Photos
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=organizer --cov-report=html

# Run specific test
pytest tests/test_organizer.py::test_basic_organization -v
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Run tests (`pytest`)
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the need to clean up messy Downloads folders everywhere
- Built with ❤️ by [Stencilwashcoder](https://github.com/stencilwashcoder)

---

<p align="center">
  <sub>⭐ Star this repo if it helped you clean up your digital mess! ⭐</sub>
</p>
