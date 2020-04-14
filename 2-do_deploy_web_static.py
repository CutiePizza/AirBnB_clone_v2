#!/usr/bin/python3
"""
Task number one
"""
import datetime
import os.path
import tarfile
import glob
from fabric.api import env
from fabric.operations import run, put, env


env.hosts = ["35.243.214.205", "3.92.79.221"]
env.user = ["ubuntu"]


def do_deploy(archive_path):
    """
    Deploy
    """
    if not os.path.exists(archive_path):
        return (None)
    try:
        put(archive_path, "/tmp/")
    except:
        return False
    try:
        archive_name = archive_path.split('/')[1]
        archive_without_ext = archive_name.split('.')[0]
        run
        ("tar --extract --file /tmp/{} -C /data/web_static/releases/{}".format(
            archive_name,
            archive_without_ext
            ))
    except:
        return False
    try:
        archive_name = archive_path.split('/')[1]
        run("rm /tmp/{}".format(archive_name))
    except:
        return False
    try:
        run("rm data/web_static/current")
    except:
        return False
    try:
        archive_name = archive_path.split('/')[1]
        archive_without_ext = archive_name.split('.')[0]
        run
        ("ln -s /data/web_static/releases/{} /data/web_static/current".format(
            archive_without_ext))
    except:
        return False
    return True
