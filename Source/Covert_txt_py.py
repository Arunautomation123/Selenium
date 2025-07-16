import os

# Set the directory path
directory = r'D:\Users\M12378A\PycharmProjects\Selenium\Source'  # Make sure to adjust this path

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with .txt
    if filename.endswith('.txt'):
        # Construct old and new file names
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, filename[:-4] + '.py')
        # Rename the file
        os.rename(old_file, new_file)