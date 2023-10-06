#!/usr/bin/python3
"""This script is used as a fabfile"""

import os
from datetime import datetime
from fabric.api import local


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
