#!/usr/bin/python3
"""
Task number one
"""
from fabric.api import local, lcd, put, env, run


env.hosts = ["35.243.214.205", "3.92.79.221"]


def do_deploy(archive_path):
    """
    Deploy
    """
    archive_name = archive_path.split('/')[1]
    name = archive_name.split('.')[0]
    try:
        put(archive_path, "/tmp/")
    except:
        return False

    try:
        path = '/data/web_static/releases/' + name
        run('mkdir -p %s' % path)
    except:
        return False

    try:
        run('tar -xzf /tmp/%s -C /data/web_static/releases/%s/' % (
            archive_name,
            name
            ))
    except:
        return False

    try:
        run('rm /tmp/%s' % archive_name)
    except:
        return False
    try:
        run('sudo mv /data/web_static/releases/%s/web_static/*\
                /data/web_static/releases/%s' % (
                    name,
                    name
                    ))
    except:
        return False

    try:
        run('rm -rf /data/web_static/releases/%s/web_static' % name)
    except:
        return False

    try:
        run('rm -rf /data/web_static/current')
    except:
        return False

    try:
        run('ln -s /data/web_static/releases/%s\
                /data/web_static/current' % name)
    except:
        return False
    return True
