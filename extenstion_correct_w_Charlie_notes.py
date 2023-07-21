import os

def add_file_extension(filename):
    jpg_header = b'\xFF\xD8\xFF\xE0'
    png_header = b'\x89\x50\x4E\x47'

    with open(filename, 'rb') as file:                                  #   The 'with open' opens the file and only closes the file
        header = file.read(4)                                           #   at the end of the process.  I shifted the code below 
        if header.startswith(jpg_header):                               #   back one tab to allow the file being opened to close 
            new_extension = '.jpg'                                      #   and then be renamed.  The OS won't allow a rename
        elif header.startswith(png_header):                             #   while the file is open.
            new_extension = '.png'                                      #
        else:                                                           #
            print(f"Unrecognized file format. Skipping {filename}")     #
            return                                                      #

    directory_path, old_basename = os.path.split(filename)
    new_basename = os.path.splitext(old_basename)[0] + new_extension
    new_filename = os.path.join(directory_path, new_basename)

    print(f"Detected {new_extension[1:].upper()} file. Renaming to: {new_basename}")
    if not os.path.exists(new_filename):
        # try:
            os.rename(filename, new_filename)                           
        # except OSError as e:                                          
        #     print(f"Error renaming {filename}: {e}")
    else:
        print(f"File {new_basename} already exists. Skipping renaming.")


def process_directory(directory_path):
    print(os.listdir(directory_path))
    for filename in os.listdir(directory_path):
        print(filename)
        full_path = os.path.join(directory_path, filename)
        if os.path.isfile(full_path):
            add_file_extension(full_path)
        else:
            print(f"Skipping {filename} as it is not a regular file.")


if __name__ == "__main__":
    direct_path = input("What is the path to the directory to search? ")
    # print(directory_path)
    process_directory(direct_path)
