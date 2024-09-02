import os

def analyze_extensions(directory):

    extensions = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            if extension:
                extensions[extension] = extensions.get(extension, 0) + 1

    # Sort Items
    extensions = dict(sorted(extensions.items(), key=lambda item: item[1], reverse=True))

    return extensions

def save_to_txt(extensions, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_directory, filename)

    with open(file_path, 'w') as f:
        for extension, count in extensions.items():
            f.write(f"{extension}: {count} files\n")

directory = r"C:\...\PHOTO" # your path
extensions_data = analyze_extensions(directory)
filename = "extension_counts.txt"

save_to_txt(extensions_data, filename)