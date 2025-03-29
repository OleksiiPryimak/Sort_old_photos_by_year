# python ico_converter\png_2_ico_converter.py

from PIL import Image
import os

def convert_png_to_ico(png_file_path, ico_file_path):
    """
    Convert a .png file to a .ico file.

    :param png_file_path: Path to the .png file
    :param ico_file_path: Path to save the .ico file
    """
    try:
        img = Image.open(png_file_path)
        img.save(ico_file_path, format='ICO')
        print(f"Successfully converted {png_file_path} to {ico_file_path}")
    except Exception as e:
        print(f"Error converting {png_file_path} to {ico_file_path}: {e}")

def main():
    # Example usage
    base_path = input("Enter the base path where your .png file is located: ")
    png_file_path = os.path.join(base_path, '1.png')  # Replace with your .png file name
    ico_file_path = os.path.join(base_path, '1.ico')  # Replace with your desired .ico file name
    convert_png_to_ico(png_file_path, ico_file_path)


if __name__ == "__main__":
    main()

