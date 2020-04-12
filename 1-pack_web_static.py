#!/usr/bin/python3
"""
Task number one
"""
import datetime
import os.path
import tarfile
import glob


def do_pack():
    """
    File
    """
    now = datetime.datetime.now()
    source_dir = "./web_static"
    dest_dir = "./versions"
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute,
            now.second)
    if not os.path.exists("./versions"):
        os.makedirs("./versions")
    try:
        tar = tarfile.open("./versions/{}".format(archive_name), "w:gz")
        for file_name in glob.glob(os.path.join(source_dir, "*")):
            tar.add(file_name, os.path.basename(file_name))
        tar.close()
        return (archive)
    except:
        return (None)
