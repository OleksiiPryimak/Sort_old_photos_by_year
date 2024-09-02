import os
import exifread
import shutil
from datetime import datetime

def sort_images_by_year(source_directory, destination_dir, extensions, unknown_year_folder, error_folder):
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(tuple(extensions)):
                file_path = os.path.join(root, file)

                # modified year
                modified_time = os.path.getmtime(file_path)
                modified_year = datetime.fromtimestamp(modified_time).year

                # EXIF year
                try:
                    with open(file_path, 'rb') as f:
                        tags = exifread.process_file(f)
                        datetime_original = tags.get('EXIF DateTimeOriginal')
                        if datetime_original:
                            taken_year = int(datetime_original.values.split(':')[0])
                        else:
                            taken_year = modified_year
                except (AttributeError, KeyError, ValueError):
                    year = error_folder
                else:
                    # Choose a lower year
                    year = min(modified_year, taken_year)

                dest_dir = os.path.join(destination_dir, str(year))
                os.makedirs(dest_dir, exist_ok=True)

                base_name, ext = os.path.splitext(file)
                i = 1
                while True:
                    new_file_name = f"{base_name}_{i}{ext}"
                    new_file_path = os.path.join(dest_dir, new_file_name)
                    if not os.path.exists(new_file_path):
                        break
                    i += 1

                shutil.move(file_path, new_file_path)


def sort_and_move_files(source_directory, target_dir, extensions):

  for root, _, files in os.walk(source_directory):
    for file in files:
      if file.endswith(tuple(extensions)):
        file_path = os.path.join(root, file)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        year = mod_time.year
        target_year_dir = os.path.join(target_dir, str(year))

        os.makedirs(target_year_dir, exist_ok=True)

        base_name, extension = os.path.splitext(file)
        i = 1
        while True:
            new_file_name = f"{base_name}_{i}{extension}"
            new_file_path = os.path.join(target_year_dir, new_file_name)
            if not os.path.exists(new_file_path):
                break
            i += 1

        shutil.move(file_path, new_file_path)


def move_other_files(source_directory, target_dir):

  for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            base_name, extension = os.path.splitext(file)
            i = 1
            while True:
                new_file_name = f"{base_name}_{i}{extension}"
                new_file_path = os.path.join(target_dir, new_file_name)
                if not os.path.exists(new_file_path):
                    break
                i += 1
            shutil.move(file_path, new_file_path)


extensions_images = ('jpg', 'JPG', 'jpeg', 'png', 'bmp')
# extensions_to_sort = ['jpg', 'JPG', 'jpeg', 'png', 'bmp']
extensions_videos = ('mp4', 'AVI', 'MTS', 'avi', 'MOV', 'MP4', 'WAV', '3GP', '3gp', 'ASF', 'MPG')
extensions_docs = ('docx', 'doc', 'pdf', 'psd', 'rar', 'zip', 'odt', 'DOC', 'mp3')
unknown_year_folder = "Brak_Roku"
error_folder = "error"


source_directory = r"C:\...\OLD_PHOTOS"
dir_img = r"C:\...\1_Photos"
dir_vid = r"C:\...\2_Videos"
dir_docs = r"C:\...\3_Docs"
dir_other = r"C:\...\4_Other"


sort_images_by_year(source_directory, dir_img, extensions_images, unknown_year_folder, error_folder)
# sort_images_by_year(source_directory, destination_directory, extensions_to_sort, unknown_year_folder, error_folder)
sort_and_move_files(source_directory, dir_vid, extensions_videos)
sort_and_move_files(source_directory, dir_docs, extensions_docs)
move_other_files(source_directory, dir_other)