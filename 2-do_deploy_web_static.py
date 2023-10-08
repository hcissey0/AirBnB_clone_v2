#!/usr/bin/python3
"""This script is used as a fabfile"""

from os.path import exists
from datetime import datetime
from fabric.api import env, put, run


env.hosts = ["54.160.68.240", "34.232.71.122"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """This is the deployer"""

    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]
    try:
        # uploading to the temp folder
        put(archive_path, "/tmp/")

        # delete existing folder
        run("rm -fr /data/web_static/releases/{}".format(
            name))

        # creating new folder
        if run("mkdir -p /data/web_static/releases/{}/".format(
                name)).failed:
            return False

        # extracting to the folder
        if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                file_name, name)).failed:
            return False

        # deleting the archive
        if run("rm /tmp/{}".format(file_name)).failed:
            return False

        # copying the data to the uncompressed parent folder
        if run("mv /data/web_static/releases/{}/web_static/* "
               "/data/web_static/releases/{}/".format(name, name)).failed:
            return False

        # deleting the uncompressed folder
        if run("rm -fr /data/web_static/releases/{}/web_static/".format(
                name)).failed:
            return False

        # removing the old symbolic link
        if run("rm -rf /data/web_static/current").failed:
            return False

        # creating a new symbolic link
        if run("ln -s /data/web_static/releases/{}/ "
               "/data/web_static/current".format(name)).failed:
            return False

    except Exception:
        return False
    print("New version deployed!")
    return True
