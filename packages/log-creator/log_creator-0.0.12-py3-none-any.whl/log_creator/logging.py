"""
This module implements the main functionality of log_creator.
Author: Nethan Quinn Jael from lUckYtHRteeN13
Email: nethanquinnjael13@gmail.com
"""

__author__ = "Nethan Quinn Jael, lUckYtHRteeN13"
__email__ = "nethanquinnjael13@gmail.com"
__status__ = "planning"

from time import strftime
from os import path, getcwd, makedirs, remove, listdir, walk

#TODO: DOCTSTRINGS PLSS and Comments
#TODO: Proper Error Handling


class InvalidPathError(Exception):
    pass


# class Log:
    
def __init__(self, file_name: str = None, file_directory: str = None) -> None:
    """[summary]

    Args:
        file_name (str, optional): [description]. Defaults to None.
        file_directory (str, optional): [description]. Defaults to None.

    Raises:
        InvalidPathError: [description]
    """

    self.current_directory = getcwd()
    self.time = strftime("%d-%m-%y %H:%M:%S").partition(" ")

    if file_name is None: 
        self.file_name = self.time[0] + ".txt"
    else:
        if file_name.lower().endswith(".txt"):
            self.file_name = file_name
        else: 
            self.file_name = file_name + ".txt"

    if file_directory is None: 
        log_directory = path.join(self.current_directory, "Logs")
    elif not path.isdir(file_directory):
        raise InvalidPathError("Invalid Directory: %s" % file_directory)
    else:
        if file_directory.lower().endswith("logs"):
            log_directory = file_directory
        else: 
            log_directory = path.join(file_directory, "Logs")
    
    self.file_directory = unexisting_dir_creator(log_directory)
    self.file_path = path.join(self.file_directory, self.file_name)
    self.files = []
    
    for root, folder, files in walk(self.file_directory): 
        for file in files:
            self.files.append(path.join(root, file))
            
    print(self.file_name)
    print(self.file_directory)
    print(self.files)

def create_log(self):
    """[summary]
    """
    if not path.isfile(self.file_path): open(self.file_path, "w")   

def write_log(self, text:str) -> None:
    """[summary]
    """
    with open(path.join(self.file_directory, self.file_name), "a") as f:
        f.write(f"{self.time[2]} {text}\n")
        
#TODO: Create an Erase or Delete Function
def delete_log(self, file_name: str = None) -> None:
    try:
        remove(path.join(self.file_directory, file_name))
    except Exception as e:
        print(e)


def unexisting_dir_creator(dir: str) -> str:
    if not path.exists(dir):
        makedirs(dir)
    else:
        print("This path is already created. (%s)" % dir)
    
    return dir