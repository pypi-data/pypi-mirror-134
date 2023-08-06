#!/usr/bin/env python3
""" A program that will encrypt and archive a file or directory.
        - Uses GnuPG
"""
import os
from termcolor import cprint
import gnupg  # type: ignore
from .utils import full_path, zip_directory  # type: ignore
from sys import exit


def _encrypt(z: str, e: str) -> None:
    """Encrypts an archive file for a specifid recipient using GPG.

    Args:
        z: str - absolute path to zip archive file you want to encrypt.
    Returns:
        e: str - absolute path to encrypted zip archive file (.zip.gpg).
    """
    # Begin encryption of data
    gpg = gnupg.GPG(gnupghome=os.path.expanduser("~/.gnupg"))
    with open(z, mode="rb") as f:
        # output = [file_name].gpg
        status = gpg.encrypt_file(f, recipients=e, output=z + ".gpg")
        status_msg = f"{z}: {status.status}"
        cprint(status_msg, "green")


def backup(path: str, dest: str, email: str) -> None:
    """Backup and encrypt a file or directory to a destination.
    *Backed up data is encrypted for the email user provided*.

    Args:
        path: str - relative path to original data.
        dest: str - relative path to desination directory.
        email: str - email of GPG recipient.
    """

    # TODO: start with checking if pub key exists locally

    # Expand ~/ or ensure absolute path
    orig_dir = full_path(path)
    _dest = full_path(dest)

    # if orig_dir{path}; zip and backup to dest
    # TODO: wrap if in try. Except = os.path.exists. Move else after except as catchall error
    if os.path.isdir(orig_dir):
        # TODO: check if backup zip already exists before z
        #   overwrite = input('Selection [Y/N]: ')
        #   if not overwrite.upper() in 'Y':
        os.chdir(orig_dir)

        # backup(orig_dir, dest)
        # dest_name = name for backup directory
        zip_dir = zip_directory(orig_dir, _dest)
        # encrypt zip then delete it
        os.chdir(_dest)
        _encrypt(zip_dir, email)
        print(f'SUCCESS! Backup File: {_dest+"/"+zip_dir+".gpg"}')
        os.remove(zip_dir)
        exit(0)

    # File backup if no dir found
    elif os.path.exists(orig_dir):
        dir_path = os.path.dirname(orig_dir)
        fname = orig_dir.split("/")[-1]
        ename = fname + ".gpg"
        print(f"Encrypting and moving File: {fname}")
        os.chdir(dir_path)
        _encrypt(fname, email)
        os.rename(ename, dest + "/" + ename)
        print(f'SUCCESS! Backup file: {dest+"/"+ename}')
        exit(0)
    else:
        exit(1)
