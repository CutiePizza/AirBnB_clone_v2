#!/usr/bin/python3
"""
Task number one
"""
import datetime
import os.path
import tarfile
import glob
from fabric.operations import local
from fabric.context_managers import lcd


def do_pack():
    """
    File
    """
    local('mkdir -p versions')
    now = datetime.datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute,
            now.second)
    try:
        local("tar -cvzf versions/{} web_static".format(archive_name))
    except:
        return None

    'versions/' + tar_name
    return "versions/" + archive_name
