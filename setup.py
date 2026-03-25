from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file-organizer-cli",
    version="1.0.0",
    author="StencilwashCoder",
    author_email="stencilwashcoder@example.com",
    description="A powerful CLI tool to automatically organize your files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StencilwashCoder/file-organizer",
    py_modules=["organizer"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "file-organizer=organizer:main",
        ],
    },
)
