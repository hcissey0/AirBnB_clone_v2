#!/usr/bin/python3
"""This script is used as a fabfile"""

import os
from datetime import datetime
from fabric.api import local, env, put, run


def do_pack():
    """This fucntion is used as the fabric command to pack the files"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if not os.path.exists("versions"):
        if local("mkdir -p versions").failed is True:
            return None
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """This is the deployer"""

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = os.path.basename(archive_path)
        name, ext = os.path.splitext(file_name)
        run("mkdir -p /data/web_static/releases/{}/".format(
            name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name, name))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_startic/releases/{}/".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))
        return True
    except Exception:
        return False
