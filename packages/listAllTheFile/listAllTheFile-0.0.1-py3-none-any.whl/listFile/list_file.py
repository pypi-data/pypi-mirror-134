
import os
import sys
def find_files(dir_name):
    """
    :param dir_name: The directory to search for regular expressions in
    :return: A list of filenames in the given directory 
    """
    try:
        result = os.listdir(dir_name)
    except Exception:
        result = []
    return result
    
def extract():
    dir_name = sys.argv[1]
    if os.path.isfile(dir_name):
        print(dir_name)
    else:
        print_files(dir_name)

def print_files(dir_name):
    for fname in find_files(dir_name):
        fpath = os.path.join(dir_name, fname)
        if os.path.isdir(fpath):
            print_files(fpath)
        else:
            print(fpath)
