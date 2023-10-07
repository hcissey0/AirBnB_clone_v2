#!/usr/bin/python3
"""This script is used as a fabfile"""

from os.path import exists
from datetime import datetime
from fabric.api import env, put, run


env.hosts = ["54.160.68.240", "34.232.71.122"]


def do_deploy(archive_path):
    """This is the deployer"""

    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    try:
        # uploading to the temp folder
        put(archive_path, "/tmp/")

        # creating new folder
        run("mkdir -p /data/web_static/releases/{}/".format(name))

        # extracting to the folder
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name, name))

        # deleting the archive
        run("rm /tmp/{}".format(file_name))

        # copying the data to the uncompressed parent folder
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))

        # deleting the uncompressed folder
        run("rm -fr /data/web_static/releases/{}/web_static".format(
            name))

        # removing the old symbolic link
        run("rm -rf /data/web_static/current")

        # creating a new symbolic link
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(name))
        return True
    except Exception:
        return False
