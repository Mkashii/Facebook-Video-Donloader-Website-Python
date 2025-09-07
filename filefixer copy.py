import os

def delete_first_line_of_html_files(folder_path, encoding='utf-8'):
    # Loop through all files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is an HTML file
        if filename.endswith('.html'):
            try:
                # Open the file with the specified encoding
                with open(file_path, 'r', encoding=encoding) as file:
                    lines = file.readlines()

                # If the file has more than one line, remove the first line
                if len(lines) > 1:
                    with open(file_path, 'w', encoding=encoding) as file:
                        file.writelines(lines[1:])  # Write the lines excluding the first one
                elif len(lines) == 1:
                    # If the file only has one line, just clear the content
                    open(file_path, 'w', encoding=encoding).close()

                print(f"First line deleted from {filename}")
            except UnicodeDecodeError as e:
                print(f"Error decoding {filename}: {e}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Specify the folder path
folder_path = input("Enter the folder path: ")

# You can change the encoding if 'utf-8' doesn't work
delete_first_line_of_html_files(folder_path, encoding='utf-8')
 