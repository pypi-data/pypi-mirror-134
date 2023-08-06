#!/usr/bin/python3

""" The CLI for the backpack backup program.
"""

from argparse import ArgumentParser
from .backpack import backup  # type: ignore
from gnupg import GPG  # type: ignore

# TODO: will require gnupg export / import
# INFO: https://docs.red-dove.com/python-gnupg/#generating-keys
def new_key(**kwargs: str) -> dict:
    """Creates a new GPG key.

    Args:
        name = str
        email = str
        password = str
    """
    key_default = {
        "name": "Backpack Backup",
        "email": "backpack@unkwn1.dev",
        "key_type": "RSA",
        "key_length": 4096,
        "comment": "default generated GPG key by Backpack Backup",
        "password": ("no_protection", False),
    }
    # If 3 args provided merge dicts
    if len(kwargs) > 0:
        if "name" and "email" and "password" in kwargs:
            key_default = key_default | kwargs
    gpg = GPG()
    key_data = gpg.gen_key_input(**key_default)

    # No args or not 3 required -> use default
    return key_default


def main():
    """Collects and parses arguments for backpack.

    Required Args:
        p: str -
            A full or relative path to a file or directory.
        d: str -
            A full or relative path to directory.
        e: str -
            The email address for a local GPG public key.
    """
    parser = ArgumentParser(description="Backpack, an easy way to backup a directory.")
    parser.add_argument(
        "-p",
        help="Path to file or directory",
        type=str,
        metavar="<PATH>",
        required=True,
    )
    parser.add_argument(
        "-d",
        help="Path to destination directory",
        type=str,
        metavar="<PATH>",
        required=True,
    )
    parser.add_argument(
        "-e",
        help="GPG Email for encryption",
        type=str,
        metavar="<john@gmail.com>",
        required=True,
    )
    args = parser.parse_args()
    path: str = args.p
    dest: str = args.d
    email: str = args.e
    backup(path, dest, email)
