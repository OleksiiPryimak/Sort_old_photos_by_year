# README.md

# Sort Old Photos by Year

This project provides a graphical user interface (GUI) application to sort old photos and files by year and analyze file extensions within a specified directory. The application is built using Python's `tkinter` library along with `ttkbootstrap` for enhanced styling.

## GUI
<img src="https://github.com/user-attachments/assets/2bbb0aed-0253-4b6e-8dc9-b049cb3cb4a2" height="250">
<img src="https://github.com/user-attachments/assets/1eba4f99-131b-4c21-b004-3f9df7729a7c" height="250">

## Also you can save txt file with extensions
<img src="https://github.com/user-attachments/assets/56cc70b1-6de9-431f-bed5-c73527415a9a" height="250">

## Features

- **Sort Files by Year**: Organizes images and files based on their creation or modification dates.
- **Analyze File Extensions**: Counts and reports the number of files for each unique extension in a specified directory.
- **User-Friendly GUI**: The application features a clean and intuitive interface with tabs for different functionalities.

## Project Structure

```
Sort_old_photos_by_year  
├── src  
│   ├── FUNCTIONS  
│   │   ├── ANALYZE_extensions.py  
│   │   └── Sorting_ALL_files_by_year.py  
├── GUI  
│   └── gui.py     
├── LICENSE  
├── README.md  
└── requirements.txt  
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Sort_old_photos_by_year
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. **Organizing All Files**:
   - Navigate to the first tab.
   - Enter the directory path containing the files you want to organize.
   - Click the "Organize All Files" button.
   - Click the button to start the sorting process. A progress bar will indicate the progress.
   - The application will sort images, videos, documents, and other files into subfolders within the `Organized Files` folder.


3. **Analyzing File Extensions**:
   - Navigate to the second tab.
   - Enter the directory path you want to analyze.
   - Click the button to start the analysis. A progress bar will indicate the progress.

4. **How to Use**:
   - The third tab provides instructions on how to use the application effectively.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
