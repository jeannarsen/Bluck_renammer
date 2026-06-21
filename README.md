# Bulk File Renamer (Python)

## 📌 Description
This project is a Python-based automation tool designed to streamline file management. It scans a target directory, filters specific file extensions (such as isolating raw images), and renames them in bulk using a structured nomenclature (e.g., `photo_1.jpg`, `photo_2.jpg`).

## 🚀 Features
* **Targeted Scanning**: Utilizes absolute and relative path management to isolate the workspace.
* **Smart Filtering**: Accurately analyzes file extensions using Python's native `pathlib` library.
* **Dynamic Indexing**: Integrates an automatic counter to prevent file overwriting during batch processes.
* **Safe Execution**: Built with a "Dry Run" simulation logic to validate file naming structures before making changes.

## 🛠️ Technologies Used
* **Python 3.x**
* Native Module: `pathlib` (Advanced file system path manipulation)
