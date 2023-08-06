#!/usr/bin/env python3
""" A program that will encrypt and archive a file or directory.
        - Uses GnuPG
"""
import os
import shutil
import re


def full_path(path: str) -> str:
    """Expand a relative path and return the absolute path.

    Args:
        path (str): the relative path to a file.
    Returns:
        path (str): the absolute path to a file
    """
    if re.search("^~", path):
        path = os.path.expanduser(path)
    else:
        path = os.path.abspath(path)
    return path

def zip_directory(path: str, dest: str) -> str:
    """Create a zipped copy of a directory.

    Args:
        p: str - full path to file or directory to backup.
        d: str - full path to the destination for the backup archive file.
    Returns:
        z: str - full path to backup archive OR archive object.
    """
    # dest_name = name for backup directory
    dest_name = path.split("/")[-1] + "-backup"
    # create zip
    zip = shutil.make_archive(dest_name, "zip")
    # move zip from cwd to dest
    os.rename(zip, dest + "/" + zip)
    # encrypt zip then delete it
    os.chdir(dest)
    return zip