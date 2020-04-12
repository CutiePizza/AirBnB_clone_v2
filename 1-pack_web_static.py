#!/usr/bin/python3
"""
Task number one
"""
import os.path
import tarfile
import glob


def do_pack():
    """
    File
    """
    source_dir = "./web_static"
    dest_dir = "./versions"
    archive_name = "./versions/web_static_20200414235157.tgz"
    archive = "web_static_20200414235157.tgz"
    if not os.path.exists("./versions"):
        os.makedirs("./versions")
    try:
        tar = tarfile.open(archive_name, "w:gz")
        for file_name in glob.glob(os.path.join(source_dir, "*")):
            tar.add(file_name, os.path.basename(file_name))
        tar.close()
        return (archive)
    except:
        return (None)
