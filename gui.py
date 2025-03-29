from ttkbootstrap import Window, Style, ttk
from tkinter import StringVar, Text, messagebox
from ttkbootstrap.widgets import Frame, Label, Entry, Button, Progressbar
import threading
import os
from src.FUNCTIONS.Sorting_ALL_files_by_year import sort_images_by_year
from src.FUNCTIONS.ANALYZE_extensions import analyze_extensions, save_to_txt
import shutil
from src.FUNCTIONS.Sorting_ALL_files_by_year import extensions_images, extensions_videos, extensions_docs

class App:
    def __init__(self, root):
        self.root = root
        self.app_title = "Organize Old Photos & Files"
        self.root.title(self.app_title)
        self.root.geometry("1000x1000")

        # self.root.iconbitmap("custom_icon.ico")
        self.root.iconbitmap(os.path.join("png2ico", "1.ico"))
        # for macOS and Linux
        # self.root.iconphoto(True, ttk.PhotoImage(file=os.path.join("png2ico", "1.png"))

        # Initialize the style
        self.style = Style(theme="solar")

        # Add header with app name, theme selection text, and combobox
        header_frame = Frame(root)
        header_frame.pack(pady=5, fill='x')

        Label(header_frame, text=self.app_title, font=("Helvetica", 16, "bold")).pack(side="left", padx=10)
        Label(header_frame, text="Select Theme:").pack(side="top", padx=5, anchor="e")
        self.theme_var = StringVar(value="solar")
        self.theme_selector = ttk.Combobox(header_frame, textvariable=self.theme_var, values=["solar", "united"], state="readonly")
        self.theme_selector.pack(side="right", padx=5)
        self.theme_selector.bind("<<ComboboxSelected>>", self.change_theme)

        self.tab_control = ttk.Notebook(root)

        self.tab_sort = Frame(self.tab_control)
        self.tab_analyze = Frame(self.tab_control)
        self.tab_help = Frame(self.tab_control)

        self.tab_control.add(self.tab_sort, text='Organize Files')
        self.tab_control.add(self.tab_analyze, text='Analyze Extensions')
        self.tab_control.add(self.tab_help, text='How to Use')

        self.tab_control.pack(expand=1, fill='both')

        self.create_sort_tab()
        self.create_analyze_tab()
        self.create_help_tab()

    def change_theme(self, event):
        """Change the ttkbootstrap theme dynamically."""
        selected_theme = self.theme_var.get()
        self.style.theme_use(selected_theme)

    def create_sort_tab(self):
        Label(self.tab_sort, text="Directory to Sort:").pack(pady=10)
        self.sort_directory = StringVar()
        Entry(self.tab_sort, textvariable=self.sort_directory, width=50).pack(pady=5)
        self.sort_directory.set("Enter directory path here...")
        Label(self.tab_sort, text="Progress bar").pack(pady=5)
        self.sort_progress = Progressbar(self.tab_sort, orient='horizontal', length=400, mode='determinate')
        self.sort_progress.pack(pady=10)
        self.sort_status = Label(self.tab_sort, text="")
        self.sort_status.pack(pady=5)

        Button(self.tab_sort, text="Organize All Files", command=self.run_sort_all).pack(pady=20)

        # Add a Labelframe for extensions
        extensions_frame = ttk.Labelframe(self.tab_sort, text="Extensions Information", padding=(10, 10), bootstyle="primary")
        extensions_frame.pack(pady=20, fill="x", padx=10)

        # Display extensions from Sorting_ALL_files_by_year
        from src.FUNCTIONS.Sorting_ALL_files_by_year import extensions_images, extensions_videos, extensions_docs

        Label(extensions_frame, text=f"Image Extensions: {', '.join(extensions_images)}").pack(anchor="w", padx=10, pady=2)
        Label(extensions_frame, text=f"Video Extensions: {', '.join(extensions_videos)}").pack(anchor="w", padx=10, pady=2)
        Label(extensions_frame, text=f"Document Extensions: {', '.join(extensions_docs)}").pack(anchor="w", padx=10, pady=2)

    def create_analyze_tab(self):
        Label(self.tab_analyze, text="Directory to Analyze:").pack(pady=10)
        self.analyze_directory = StringVar()
        Entry(self.tab_analyze, textvariable=self.analyze_directory, width=50).pack(pady=5)
        self.analyze_directory.set("Enter directory path here...")

        Label(self.tab_analyze, text="Progress bar").pack(pady=5)
        self.analyze_progress = Progressbar(self.tab_analyze, orient='horizontal', length=400, mode='determinate')
        self.analyze_progress.pack(pady=10)
        self.analyze_status = Label(self.tab_analyze, text="")
        self.analyze_status.pack(pady=5)

        Button(self.tab_analyze, text="1. Analyze Extensions", command=self.run_analysis).pack(pady=20)
        Button(self.tab_analyze, text="2. Save to TXT", command=self.save_analysis_to_txt).pack(pady=20)

        Label(self.tab_analyze, text="Output:").pack(pady=10)
        self.output_text = Text(self.tab_analyze, wrap='word', height=10, width=70)
        self.output_text.pack(pady=10)
        self.output_text.config(state='disabled')

    def create_help_tab(self):
        help_text = Text(self.tab_help, wrap='word', height=40, width=70)
        help_text.pack(pady=10)
        help_text.insert('1.0', f"How to Use the '{self.app_title}' App:\n\n"
              "Overview:\n"
              "This application helps you organize your files by sorting them into folders based on their type and year, "
              "analyzing file extensions, and providing helpful information about the process.\n\n"
              "Instructions:\n"
              "1. Organize Files Tab:\n"
              "   - Enter the directory path containing the files you want to organize.\n"
              "   - Click the 'Organize All Files' button to start the process.\n"
              "   - Monitor the progress bar and status updates to track the operation.\n"
              "   - The files will be sorted into folders such as Photos, Videos, Documents, and Others.\n\n"
              "2. Analyze Extensions Tab:\n"
              "   - Enter the directory path to analyze file extensions.\n"
              "   - Click the 'Analyze Extensions' button to start the analysis.\n"
              "   - View the results in the output section, which lists file extensions and their counts.\n"
              "   - Optionally, click 'Save to TXT' to save the analysis results to a text file.\n\n"
              "3. How to Use Tab:\n"
              "   - This tab provides detailed instructions on how to use the application.\n"
              "   - Refer to this section for guidance on each feature.")
        help_text.config(state='disabled')

    def run_sorting(self):
        directory = self.sort_directory_entry.get()
        destination_directory = self.destination_directory_entry.get()
        year_error = self.year_error_entry.get()
        error_folder = self.error_folder_entry.get()

        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Invalid directory path.")
            return
        if not os.path.isdir(destination_directory):
            messagebox.showerror("Error", "Invalid destination directory path.")
            return
        if not year_error or not error_folder:
            messagebox.showerror("Error", "Year error folder name and error folder name cannot be empty.")
            return
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Invalid directory path.")
            return
        self.sort_progress['value'] = 0
        self.sort_status.config(text="Starting the process...")
        not_organized_dir = os.path.join(directory, "Only Folders")
        threading.Thread(target=self.sort_files, args=(directory, not_organized_dir)).start()
    def sort_files(self, directory, not_organized_dir):
    # def sort_files(self, directory):
        # Call the sorting function
                counter = 1
                for file in os.listdir(directory):  # Iterate over files in the directory
                    base, ext = os.path.splitext(file)
                while os.path.exists(target_path):
                    target_path = os.path.join(not_organized_dir, f"{base}_copy{counter}{ext}")
                    counter += 1
                messagebox.showinfo("Success", "Files sorted successfully!")

    def run_sort_all(self):
        directory = self.sort_directory.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Invalid directory path.")
            return

        # Update progress: Start of the process
        self.sort_progress['value'] = 15
        self.sort_status.config(text="Starting the process...")

        # Create 'Not Organized' and 'Organized Files' folders
        not_organized_dir = os.path.join(directory, "Only Folders")
        organized_files_dir = os.path.join(directory, "Organized Files")
        os.makedirs(not_organized_dir, exist_ok=True)
        os.makedirs(organized_files_dir, exist_ok=True)

        # Update progress: Folders created
        self.sort_progress['value'] = 50
        self.sort_status.config(text="Folders created: 'Organized Files' and 'Only Folders'.")

        # Count total files for progress tracking
        self.total_files = 0
        for root, dirs, files in os.walk(directory):
            if root == organized_files_dir or root == not_organized_dir:
                continue
            self.total_files += len(files)

        # Move all files (excluding 'Organized Files') to 'Not Organized'
        self.processed_files = 0
        for root, dirs, files in os.walk(directory, topdown=False):  # Use topdown=False to process subdirectories first
            if root == organized_files_dir or root == not_organized_dir:
                continue

            # Move files to 'Not Organized'
            for file in files:
                file_path = os.path.join(root, file)
                target_path = os.path.join(not_organized_dir, file)

                # Ensure no overwriting of files with the same name
                if os.path.exists(target_path):
                    base, ext = os.path.splitext(file)
                    target_path = os.path.join(not_organized_dir, f"{base}_copy{ext}")

                os.makedirs(not_organized_dir, exist_ok=True)
                try:
                    shutil.move(file_path, target_path)
                    self.processed_files += 1
                except Exception as e:
                    print(f"Error moving file {file_path}: {e}")

            # Move empty directories to 'Not Organized'
            if not os.listdir(root):  # Check if the directory is empty
                try:
                    shutil.move(root, os.path.join(not_organized_dir, os.path.basename(root)))
                except Exception as e:
                    print(f"Error moving directory {root}: {e}")

        # Update progress: Files moved
        self.sort_progress['value'] = 55
        self.sort_status.config(text="All files moved to 'Only Folders'.")

        # Start sorting files
        self.sort_progress['value'] = 100
        self.sort_status.config(text="Starting to sort all files...")
        threading.Thread(target=self.sort_all_files, args=(not_organized_dir, organized_files_dir)).start()

    def sort_all_files(self, source_directory, destination_directory):
        from src.FUNCTIONS.Sorting_ALL_files_by_year import (
            sort_images_by_year,
            sort_and_move_files,
            move_other_files,
            extensions_images,
            extensions_videos,
            extensions_docs,
            unknown_year_folder,
            error_folder,
        )

        # Define target directories within 'Organized Files'
        target_dir_images = os.path.join(destination_directory, "1_Photos")
        target_dir_videos = os.path.join(destination_directory, "2_Videos")
        target_dir_docs = os.path.join(destination_directory, "3_Docs")
        target_dir_other = os.path.join(destination_directory, "4_Other")

        # Create target directories if they don't exist
        os.makedirs(target_dir_images, exist_ok=True)
        os.makedirs(target_dir_videos, exist_ok=True)
        os.makedirs(target_dir_docs, exist_ok=True)
        os.makedirs(target_dir_other, exist_ok=True)

        # Perform sorting
        try:
            # Sort images by year
            self.sort_status.config(text="Sorting images...")
            sort_images_by_year(source_directory, target_dir_images, extensions_images, unknown_year_folder, error_folder)
            self.processed_files += len(os.listdir(target_dir_images))
            self.update_progress()

            # Sort and move videos
            self.sort_status.config(text="Sorting videos...")
            sort_and_move_files(source_directory, target_dir_videos, extensions_videos)
            self.processed_files += len(os.listdir(target_dir_videos))
            self.update_progress()

            # Sort and move documents
            self.sort_status.config(text="Sorting documents...")
            sort_and_move_files(source_directory, target_dir_docs, extensions_docs)
            self.processed_files += len(os.listdir(target_dir_docs))
            self.update_progress()

            # Move other files
            self.sort_status.config(text="Moving other files...")
            move_other_files(source_directory, target_dir_other)
            self.processed_files += len(os.listdir(target_dir_other))
            self.update_progress()

            self.sort_status.config(text="Sorting completed successfully!")
            messagebox.showinfo("Success", "All files sorted successfully!")

            # Reset progress bar to 0%
            self.sort_progress['value'] = 0
            self.sort_status.config(text="Ready for the next operation.")
        except Exception as e:
            self.sort_status.config(text="An error occurred during sorting.")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def run_analysis(self):
        directory = self.analyze_directory.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "Invalid directory path.")
            return
        self.analyze_progress['value'] = 0
        self.analyze_status.config(text="Starting the process...")
        threading.Thread(target=self.analyze_extensions, args=(directory,)).start()
    def analyze_extensions(self, directory):
        self.extensions_data = analyze_extensions(directory)
        self.analyze_progress['value'] = 100
        self.analyze_status.config(text="The end of the process")
        self.display_output(self.extensions_data)
        messagebox.showinfo("Success", "Analysis completed!")

    def display_output(self, data):
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', 'end')
        for ext, count in data.items():
            self.output_text.insert('end', f"{ext}: {count}\n")
        self.output_text.config(state='disabled')


    def save_analysis_to_txt(self):
        if hasattr(self, 'extensions_data'):
            directory = self.analyze_directory.get()  # Get the directory from the input field
            if not os.path.isdir(directory):
                messagebox.showerror("Error", "Invalid directory path.")
                return
            save_to_txt(self.extensions_data, directory, filename=os.path.join(directory, "extension_counts.txt"))
            self.sort_progress['value'] = 85  # Update progress to 100%
            self.sort_status.config(text="Analysis saved successfully!")
            messagebox.showinfo("Success", "Analysis saved to extension_counts.txt!")
            self.sort_progress['value'] = 0  # Reset progress bar
        else:
            messagebox.showerror("Error", "No analysis data to save. Please run the analysis first.")

    def update_progress(self):
        if self.total_files > 0:
            progress = (self.processed_files / self.total_files) * 100
            self.sort_progress['value'] = progress
            self.sort_status.config(text=f"Progress: {int(progress)}%")

if __name__ == "__main__":
    root = Window(themename="solar")
    app = App(root)
    root.mainloop()

