from config import SOURCE_DIR

import os

os.chdir(SOURCE_DIR)

for file in os.listdir('.'):
    if ' ' in file:
        new_file_name = file.replace(' ', '_')
        os.rename(file, new_file_name)
