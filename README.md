<h1>Sort old photos and other files by year</h1>

<h2> --> ANALYZE_extensions.py <-- </h2>
<p>This Python script analyzes the file extensions within a specified directory and generates a report detailing the count of each unique file extension.</p>

<h3>Usage:</h3>

<p> - Replace the placeholder r"C:\...\PHOTO" with the actual path to the directory you want to analyze.</p>
<p> - Run the script.</p>
<p> - A text file named "extension_counts.txt" will be created in the same directory as the script.</p>
<p> - The file will contain a list of file extensions and their corresponding counts.</p>

<h2>Example Output:</h2>
<p>.jpg: 1000 files</p>
<p>.png: 500 files</p>
<p>.pdf: 200 files</p>
<p>.docx: 100 files</p>
<p>...</p>

<h2> --> Sorting_ALL_files_by_year.py <-- </h2>
<p>This Python script sorts images and files based on their file extensions and creation/modification dates. It organizes files into separate directories based on their type and year of creation or modification.</p>

<h3>Usage:</h3>

<p> - Replace the placeholder paths with your actual source and destination directories.</p>
<p> - Adjust the file extensions lists if necessary.</p>
<p> - Run the script.</p>
 
<h3>Output:</h3>

<p>The script will create separate directories for images, videos, documents, and other files within the specified destination directory.</p>
<p>Files will be organized within these directories based on their year of creation or modification.</p>
<p>Files with errors during EXIF extraction or movement will be placed in the error directory.</p>

![image](https://github.com/user-attachments/assets/ab92b255-e637-4860-876a-f46df980152f) ----->    ![image](https://github.com/user-attachments/assets/974a4ccc-0c3b-4b57-8943-7f2108f57b76)







